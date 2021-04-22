import yaml

from qyweixin.page.addmember import AddMember
from qyweixin.page.basepage import BasePage
from qyweixin.page.membermain import MemberMain


class ContactListPage(BasePage):
    def goto_addmember(self):
        self.action("../page/contact.yaml", "addmember")
        return AddMember(self.driver)

    def goto_member(self):
        self.action("../page/contact.yaml", "member")
        return MemberMain(self.driver)

    def get_names(self):
        with open("../page/contact.yaml", encoding="utf-8") as f:
            actions = yaml.safe_load(f)
            for action in actions["namelist"]:
                if "by" in action.keys():
                    elements = self.driver.find_elements(action["by"], action["locator"])
        # print(elements)
        name_list = [i.text for i in elements]
        print(name_list)
        return name_list
