import yaml
# from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
import logging


class BasePage:
    logging.basicConfig(level=logging.INFO)
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, by, locator):
        element = self.driver.find_element(by, locator)
        return element

    def action_list(self, action):
        logging.info(action["by"])
        logging.info(action["locator"])
        element = self.find(action["by"], action["locator"])
        if "action" in action.keys():
            if "click" == action["action"]:
                element.click()
            if "send" == action["action"]:
                logging.info(action["value"])
                element.send_keys(action["value"])

    def action(self, path, testcase=None):
        with open(path, encoding="utf-8") as f:
            actions = yaml.safe_load(f)
            if testcase is None:
                for action in actions:
                    self.action_list(action)
            else:
                for action in actions[testcase]:
                    self.action_list(action)

    def swipe_find(self, by, locator):
        num = 3
        for i in range(0, 3):
            try:
                return self.find(by, locator)
            except NoSuchElementException:
                print("未找到，滑动")
                size = self.driver.get_window_size()
                width = size['width']
                height = size['height']
                x = width / 2
                starty = height * 0.8
                endy = height * 0.2
                self.driver.swipe(x, starty, x, endy, 2000)
            if i == num - 1:
                raise NoSuchElementException(f"滑动了{i}次，没有找到元素")
    # def action_dict(self, actions, testcase):
    #     element = None
    #     for action in actions[testcase]:
    #         if "by" in action.keys():
    #             element = self.find(action["by"], action["locator"])
    #         if "action" in action.keys():
    #             if "click" == action["action"]:
    #                 element.click()
    #             if "send" == action["action"]:
    #                 element.send_keys(action["value"])
