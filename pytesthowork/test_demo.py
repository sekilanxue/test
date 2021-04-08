import allure
import pytest
import yaml
from pytesthowork.calculator import Calculator


# @pytest.fixture()
# def calculate():
#     print("开始计算")
#     cal = Calculator()
#     yield cal
#     print("结束结算")

def get_datas():
    with open("./deomo/data_demo.yaml") as f:
        datas = yaml.safe_load(f)
        print(datas)
        return datas

@allure.feature("计算器")
class TestCal:
    # def setup(self):
    #     print("开始")
    #
    # def teardown(self):
    #     print("结束")
    @allure.story("整数相加")
    @pytest.mark.parametrize("a,b,expect", get_datas()['add_int']['datas'])
    def test_add_int(self, calculate, a, b, expect):
        # cal = Calculator()
        assert expect == calculate.add(a, b)

    @pytest.mark.parametrize("a,b,expect", get_datas()['add_float']['datas'],ids = get_datas()['add_float']['ids'])
    def test_add_float(self, a, b, expect):
        cal = Calculator()
        assert expect == round(cal.add(a, b), 3)
    @allure.story("除数为0的情况")
    def test_div(self):
        cal = Calculator()
        # try:
        #     cal.div(1,0)
        # except ZeroDivisionError:
        #     print("除数为0")
        with pytest.raises(ZeroDivisionError):
            cal.div(1, 0)
