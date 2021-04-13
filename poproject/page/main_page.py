from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

from page.add_contact_page import AddContactPage
from page.add_member_page import AddMemberPage
from page.base_func import BaseFunc
from page.contact_page import ContactPage


class MainPage(BaseFunc):
    main_addmember = '.index_service_cnt_item_title'
    main_addcontact = '.index_service_cnt_item_title'
    # main_gotocontact = '.frame_nav_item_title'
    def goto_add_member(self):
        self.find(self.main_addmember).click()
        return AddMemberPage(self.driver)
    def goto_add_contact(self):
        self.find(self.main_addcontact).click()
        return AddContactPage(self.driver)
    def goto_contact(self):
        self.find('#menu_contacts').click()
        return ContactPage(self.driver)
