from appium.webdriver.webdriver import WebDriver

from qyweixin.page.basepage import BasePage
from qyweixin.page.contactlist import ContactListPage


class Main(BasePage):
    def goto_contactlist(self):
        self.action("../page/main.yaml")
        return ContactListPage(self.driver)