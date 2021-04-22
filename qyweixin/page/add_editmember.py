# from qyweixin.page.addmember import AddMember
from qyweixin.page.basepage import BasePage


class Add_EditMember(BasePage):
    def edit_member(self):
        from qyweixin.page.addmember import AddMember
        self.action("../page/add_editmember.yaml")
        return AddMember(self.driver)