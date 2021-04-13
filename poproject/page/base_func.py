from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

class BaseFunc:
    def __init__(self,base_driver=None):
        if base_driver != None:
            self.driver = base_driver
        else:
            chrome_arg = webdriver.ChromeOptions()
            chrome_arg.debugger_address = '127.0.0.1:9888'
            self.driver = webdriver.Chrome(options=chrome_arg)
            self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
            self.driver.implicitly_wait(5)
    def find(self,locator):
        return self.driver.find_element_by_css_selector(locator)
    # base_url = "https://work.weixin.qq.com/"
