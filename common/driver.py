from selenium import webdriver
import platform

class WDriver(object):
    def chromeDriver(self):
        '''
        这里判断了当前的系统如果是windows，根据系统调用驱动
        :param path_name: 驱动的路径，可以把驱动放在代码文件里面写死路径
        :return:
        '''

        chrome_options = webdriver.ChromeOptions()
        self.system = platform.system()
        try:
            if self.system == "Windows":
                 chrome_options.binary_location = r'C:\Users\86185\AppData\Local\Programs\Python\Python39\chromedriver.exe'
                 self.driver = webdriver.Chrome()
                #path_name = 'C:/Users/86185/AppData/Local/Programs/Python/Python39/chromedriver.exe'
                #self.driver = webdriver.Chrome(executable_path=path_name, chrome_options=chrome_options)
            elif self.system == "Darwin":
                self.driver = webdriver.Chrome()
        except Exception as e:
            raise ValueError('当前打开的系挺为%s ,所属的驱动无法调用;可能驱动版本问题导致注意版本'% self.system)
        return self.driver
    def firefoxDriver(self):
        try:
            self.driver = webdriver.Firefox()
        except Exception as e:
            raise ValueError ('启用火狐浏览器失败')
        else:
            return self.driver

