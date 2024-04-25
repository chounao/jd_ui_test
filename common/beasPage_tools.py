from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.driver import WDriver
from selenium.webdriver.common.by import By
import time

class BasePage(object):
    def __init__(self,driver):
        self.driver = driver

    def open_driver(self,url):
        time.sleep(0.5)
        self.driver.get(url)
        return self.driver

    # def find_Element(self,element_by,element_value):
    def find_Element(self, selectors):
        element_by = selectors[0]
        element_value = selectors[1]

        """
        @param element_by: 输入查找元素属性通过属性进行BY.XXXX操作
        @param element_value: 对应值
        @return: 返回查找元素的结果
        """

        try:
            if element_by == 'id':
                try:
                    return WebDriverWait(self.driver,10,0.5).until(EC.visibility_of(self.driver.find_element(By.ID,element_value)))
                except :
                    return False
            elif element_by == 'name':
                try:
                    return WebDriverWait(self.driver, 10, 0.5).until(
                        EC.visibility_of(self.driver.find_element(By.NAME, element_value)))
                except:
                    print("element_by,element_value", (element_by, element_value))
                    return False
            elif element_by == 'class':
                 try:
                     return WebDriverWait(self.driver, 10, 0.5).until(
                         EC.visibility_of(self.driver.find_element(By.CLASS_NAME, element_value)))
                 except:
                     return False
            elif element_by == 'tag':
                try:
                    return WebDriverWait(self.driver, 10, 0.5).until(
                        EC.visibility_of(self.driver.find_element(By.TAG_NAME, element_value)))
                except:
                    return False
            elif element_by == 'link':
                try:
                    return WebDriverWait(self.driver, 10, 0.5).until(
                        EC.visibility_of(self.driver.find_element(By.LINK_TEXT, element_value)))
                except:
                    print("element_by,element_value", (element_by, element_value))
                    return False
            elif element_by == 'plink':
                try:
                    return WebDriverWait(self.driver, 10, 0.5).until(
                        EC.visibility_of(self.driver.find_element(By.PARTIAL_LINK_TEXT, element_value)))
                except:
                    return False
            elif element_by == 'css':
                try:
                    return WebDriverWait(self.driver, 10, 0.5).until(
                        EC.visibility_of(self.driver.find_element(By.CSS_SELECTOR, element_value)))
                except:
                    return False
            elif element_by == 'xpath':
                try:
                    return WebDriverWait(self.driver, 10, 0.5).until(
                        EC.visibility_of(self.driver.find_element(By.XPATH, element_value)))
                except:
                    return False
        except:
            print("找不到该元素")

    def insert_value(self,element_by,element_value,key):
        """
        @param element_by: 和find_element方法一致
        @param element_value: 和find_element方法一致
        @param key: 输入send_keys值进行输入操作
        @return: 页面输入值
        """
        elemnt = self.find_Element(element_by,element_value)
        elemnt.send_keys(key)


    def Touch_Click(self,element_by,element_value):
        """
        @param element_by: 和find_element方法一致
        @param element_value: 和find_element方法一致
        @return: 点击按钮
        """
        elemnt = self.find_Element(element_by, element_value)
        elemnt.click()
    def get_cookes(self):

        cookie = self.driver.get_cookies()
        return cookie