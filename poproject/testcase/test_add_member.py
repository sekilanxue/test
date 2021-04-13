import pytest
import yaml

from page.main_page import MainPage


class TestAddMember:
    def setup(self):
        self.main = MainPage()
    @pytest.mark.parametrize('name,acctid,phone',yaml.safe_load(open("./memberlist.yaml",encoding='utf-8')))
    def test_add_member(self,name,acctid,phone):
        # self.main = MainPage()
        # 1、首页点击添加【成员】按钮。2、走添加成员保存流程。3、进入通讯路页面取得成员列表确认
        list_member = self.main.goto_add_member().confire_to_contact(name,acctid,phone).get_list_member(name)
        assert name in list_member
    def test_add_member_fail(self):
        # 1、首页点击添加【成员】按钮。2、走添加成员保存流程。3、进入通讯路页面取得成员列表确认
        tip_list = self.main.goto_add_member().confire_to_fail()
        tip = '该手机号已被“宋星辉”占有'
        assert tip in tip_list
    # @pytest.mark.parametrize('departname',['牛哥的UI设计部'])
    # def test_add_depart(self,departname):
    #     self.main.goto_contact().add_depart(departname)