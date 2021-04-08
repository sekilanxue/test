import pytest


@pytest.fixture()
def login():
    print("登陆")
    yield "say yes"
    print("logout")

@pytest.fixture()
def connectDB():
    print("链接数据库")