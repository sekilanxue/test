from selenium import webdriver

from page.base_func import BaseFunc
from page.contact_page import ContactPage


class AddMemberPage(BaseFunc):
    def keep_add_member(self):
        pass
    def cancel_to_contact(self):
        pass
    def confire_to_contact(self,name,acctid,phone):
        # self.driver.get('self.url')
        # self.driver.implicitly_wait(5)
        # self.driver.find_element_by_css_selector('#username').send_keys(name)
        # self.driver.find_element_by_css_selector('#memberAdd_acctid').send_keys(acctid)
        # self.driver.find_element_by_css_selector('#memberAdd_phone').send_keys(phone)
        # self.driver.find_element_by_css_selector('.qui_btn.ww_btn.js_btn_save').click()
        self.find('#username').send_keys(name)
        self.find('#memberAdd_acctid').send_keys(acctid)
        self.find('#memberAdd_phone').send_keys(phone)
        self.find('.qui_btn.ww_btn.js_btn_save').click()
        return ContactPage(self.driver)
    def confire_to_fail(self):
        self.find('#username').send_keys('宋慧星')
        self.find('#memberAdd_acctid').send_keys('NO.00003')
        self.find('#memberAdd_phone').send_keys('18612001362')
        self.find('.qui_btn.ww_btn.js_btn_save').click()
        ele_list = self.driver.find_elements_by_css_selector('.ww_inputWithTips_tips')
        error_list = [i.text for i in ele_list]
        print(error_list)
        return error_list