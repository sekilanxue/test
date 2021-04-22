from qyweixin.page.basepage import BasePage
from qyweixin.page.edit_member import EditMember


class MemberAction(BasePage):
    def goto_edit_member(self):
        self.action("../page/member_action.yaml")
        return EditMember(self.driver)
