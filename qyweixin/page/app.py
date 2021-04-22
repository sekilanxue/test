from appium import webdriver

from qyweixin.page.basepage import BasePage
from qyweixin.page.main import Main


class App(BasePage):
    def start(self):
        if self.driver is None:
            desired_caps = {
                "platformName": "Android",
                "deviceName": "127.0.0.1:7555",
                "appPackage": "com.tencent.wework",
                "appActivity": ".launch.WwMainActivity",
                "noReset": "true",
                "unicodeKeyboard": True,
                "resetKeyboard": True
            }
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
            self.driver.implicitly_wait(10)
        else:
            self.restart()
            # self.driver.start_activity("com.tencent.wework", ".launch.WwMainActivity")
        return self

    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()

    def stop(self):
        self.driver.quit()

    def goto_main(self):
        return Main(self.driver)
