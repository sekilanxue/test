import time

from qyweixin.page.basepage import BasePage


class EditMember(BasePage):
    def del_member(self):
        from qyweixin.page.contactlist import ContactListPage
        self.action("../page/edit_member")
        time.sleep(3)
        return ContactListPage(self.driver)
