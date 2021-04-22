from qyweixin.page.basepage import BasePage
from qyweixin.page.add_editmember import Add_EditMember


class AddMember(BasePage):
    def addmember_bymenual(self):
        self.action("../page/addmember.yaml", "bymenual")
        return Add_EditMember(self.driver)

    def goto_contactlist(self):
        from qyweixin.page.contactlist import ContactListPage
        self.action("../page/addmember.yaml", "contactlist")
        return ContactListPage(self.driver)
