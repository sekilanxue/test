import pytest

def test_search():
    print("搜索")
# @pytest.mark.usefixtures("login")
def test_cart():
    # print(login())标识的用法，return的值无法调用
    print("购物车")

def test_drder(login):
    print(login)

    print("下单")

# def test_cart():
#     print("购物车")