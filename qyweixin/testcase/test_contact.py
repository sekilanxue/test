import logging

from qyweixin.page.app import App


class TestContact:
    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.stop()

    def test_addcontact(self):
        name_list = self.main.goto_contactlist().goto_addmember().addmember_bymenual().edit_member().goto_contactlist().get_names()
        assert "宋蓝雪" in name_list
        # logging.FileHandler("../test.log")

    def test_delmember(self):
        name_list = self.main.goto_contactlist().goto_member().goto_member_action().goto_edit_member().del_member().get_names()
        assert "宋蓝雪" not in name_list
        # logging.FileHandler("../test.log")

    def test_get_list(self):
        name_list = self.main.goto_contactlist().get_names()
        assert "宋蓝雪" in name_list
