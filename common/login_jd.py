import time
from common.yaml_tools import yaml_tool
from common.path_tools import getPath
from common.login_tools import read_setData
from common.beasPage_tools import BasePage
from common.driver import WDriver

config_path = '\config.ini' #ini文件路径
savetoken_path = '\data\datas.yaml' #yaml文件路径

class login_Steps(WDriver):
    def __init__(self,fhdjd_token):
        self.fhdjd_token = fhdjd_token
        self.token_path= savetoken_path
        self.yanl_tools = yaml_tool()
        self.path = getPath()
        self.configPath = self.path.get_path() + config_path
    def login_steps(self):
        """
        对应的流程：1.获取config内容
                   2.打开浏览器
                   3.发送url
                   4.输入username
                   5.输入password
                   6.勾选agree
                   7.点击登陆按钮
        """
        self.steps = read_setData(driver=self)
        self.steps.getLoginData(self.configPath, 'LOGIN', 'ELEMENT', 'HTTP', 'CHROME','LOCAL_STORAGE')
        print("获取路径")
        self.steps.Launch_Chrome('chromedriver_pata')
        print("打开浏览器")
        self.steps.getAndRun_Url('jd_loginUrl')
        print("发送url")
        self.steps.loginDate_get_send('UserNameBy', 'UserNameElement','UserName')
        print("输入账号")
        self.steps.loginDate_get_send('PassWorldBy','PassWorldElement','PassWorld')
        print("输入密码")
        # self.steps.loginbtn_get_click('AgreeBtnBy','AgreeBtnElement')
        # print("点击同意")
        self.steps.loginbtn_get_click('LoginBtnBy','LoginBtnElement')
        print("点击登陆按钮")
        time.sleep(3)
    def get_path(self):
        """获取存储tokne路径"""
        self.getTPath = self.path.get_tokenpath(self.token_path)
        return self.getTPath
    def save_JDtoken_data(self):
        """进行之前所有的操作并执行获取Token操作"""
        self.login_steps()
        # self.token =  self.steps.login_And_cookieGetToken('Name','Key','Value')
        self.token = self.steps.login_And_LocalStorageGetToken()
        self.token_ditc= {
            "jd_token":self.token
        }
        self.yanl_tools.save_yaml_dict(self.get_path(),self.token_ditc)
        return self.token

if __name__ == '__main__':
    a = login_Steps(BasePage)
    a.save_JDtoken_data()