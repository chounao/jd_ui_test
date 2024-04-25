from common.BeasPage import BasePage
from common.read_tools import ReadFileData
from common.path_tools import getPath
from common.driver import WDriver
from data.login_data import LoginPageData

def open_browsers():
    derver = WDriver()
    derver.chromeDriver()
    return derver
class login(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
    def read_Data(self,config_path):
        '''
        读取ini文件的内容这里主要石读取账号密码和驱动路径
        :return:
        '''
        # config_path = '\config.ini'  # ini文件路径
        patah = getPath()
        read = ReadFileData()
        file_path = patah.get_path()+config_path
        self.data = read.load_ini(file_path)
        return self.data
    def get_inidata(self,*ini_data):
        '''
        :param ini_data:
        :return:
        '''
        name = ini_data[0]
        key = ini_data[1]
        self.value = self.data.get(name).get(key)
        return self.value


    def Open_browser(self):
        '''
        :return:
        '''
        driver = WDriver()
        try:
            #self.driver = driver.firefoxDriver()
            self.driver = driver.chromeDriver()
        except Exception as e:
            raise ValueError('无法启动浏览器')
        return self.driver

    def login_page(self,*ini_data):
        '''
        打开网页输入url
        :param url:
        :return:
        '''

        try:
            self.value = self.get_inidata(*ini_data)
            BasePage(self.driver).open_driver(self.value)
        except Exception as e:
            raise ValueError('%s 打开登录地址错误，请检查' % self.value)
        return self.driver

    def inPut_data(self,selector,*ini_data):
        '''
        查找输入框塞入数据
        :param selector:
        :param parameter:
        :return:
        '''

        try:
            self.value = self.get_inidata(*ini_data)
            BasePage(self.driver).insert_value(selector,self.value)
        except Exception as e:
            raise ValueError('%s 查找元素错误，请检查' % self.value)
        return self.driver
    def click_data(self,selector):
        '''
        勾选同意/点击登陆按钮
        :param selector:
        :return:
        '''

        try:
            BasePage(self.driver).Touch_Click(selector)
        except Exception as e:
            raise ValueError('%s 查找元素错误，请检查' % selector[1])
        return self.driver



if __name__ == '__main__':

    a = login(BasePage)
    a.read_Data('\config.ini')
    a.Open_browser()
    a.login_page('HTTP', 'jd_loginUrl')
    a.inPut_data(LoginPageData.username_selectors,('LOGIN','UserName'))
    a.inPut_data(LoginPageData.password_selectors,('LOGIN','PassWorld'))
    a.click_data(LoginPageData.agreeBtn_selectors)

