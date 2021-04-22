from qyweixin.page.basepage import BasePage
from qyweixin.page.member_action import MemberAction


class MemberMain(BasePage):
    def goto_member_action(self):
        self.action("../page/membermain.yaml")
        return MemberAction(self.driver)