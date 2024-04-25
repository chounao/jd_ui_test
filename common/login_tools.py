from common.beasPage_tools import BasePage
from common.read_tools import ReadFileData
from urllib.parse import unquote
from common.driver import WDriver


class read_setData(BasePage):
    def __init__(self, driver):
        self.dir = WDriver()
        BasePage.__init__(self=self, driver=self)
        self.bp = BasePage(driver=self)
        self.driver = driver

    def getLoginData(self, file_path, LOGIN, ELEMENT, HTTP, CHROME, LOCAL_STORAGE):
        """
        获取路径根据标识获取对应的内容
        """
        self.reda_data = ReadFileData()
        self.configData = self.reda_data.load_ini(file_path=file_path)
        self.login = self.configData[LOGIN]
        self.Ele = self.configData[ELEMENT]
        self.url = self.configData[HTTP]
        self.chrome_path = self.configData[CHROME]
        self.local_storage = self.configData[LOCAL_STORAGE]

    def Launch_Chrome(self, path_name):
        self.driver = self.dir.chromeDriver(path_name)
        return self.driver

    def getAndRun_Url(self, URL):
        """
        登陆URL
        """
        login_JDurl = self.url[URL]
        self.open_driver(login_JDurl)
        return self.driver

    def loginDate_get_send(self, element_by, element_value, send_keys):
        """
        输入框定位方法元素及输入内容
        """
        by = self.Ele[element_by]
        value = self.Ele[element_value]
        key = self.login[send_keys]
        print(by, value, key)
        self.insert_value(by, value, key)

    def loginbtn_get_click(self, element_by, element_value):
        """
        点击操作
        """
        by = self.Ele[element_by]
        value = self.Ele[element_value]
        print(by, value)
        self.Touch_Click(by, value)

    def login_And_cookieGetToken(self, application_name, application_key, application_value):
        """
        便利获取到token
        return:
        """
        Name = self.local_storage[application_name]
        key = self.local_storage[application_key]
        Value = self.local_storage[application_value]
        print(Name, key, Value)
        self.cookie = self.get_cookes()
        print(self.cookie)
        for i in self.cookie:
            print(i)
            if i[Name] == key:
                self.fhdjd_token = i[Value]
        self.token = unquote(self.fhdjd_token)
        return self.token

    def login_And_LocalStorageGetToken(self):
        token = self.driver.execute_script('return localStorage.getItem("mars.token")')
        print(token)
        self.token = (eval(token)).get('value')
        print(self.token)
        return self.token