#fixture固件参数化
import pytest

def paramss():
    return [{"name":"chen","sex":"girl"},{"school":"unniversity"}]

@pytest.fixture(scope="class",params=paramss())
def func_fixture(request):
    yield request.param  # 固定写法
    print("fixture over")

@pytest.fixture(scope="function",params=paramss(),ids=['abababab','galagala'])
def func_ids(request):
    yield request.param
    print("ids@!!")

@pytest.fixture(scope="session",params=paramss(),name="paramss_list")
def func_name(request):
    print("全局conftest开启-alisa名称paramss_list")
    yield request.param
    print("全局conftest结束-alisa名称paramss_list")

