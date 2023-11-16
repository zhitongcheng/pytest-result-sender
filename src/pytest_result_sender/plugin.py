from datetime import datetime

data = {}


def pytest_configure():
    # 配置加载完毕之后执行，所有测试用例执行之前执行
    data["start_time"] = datetime.now()
    print(f"{datetime.now()} pytest开始执行")


def pytest_unconfigure():
    # 配置卸载完毕之后执行，所有测试用例执行之后执行
    data["end_time"] = datetime.now()
    print(f"{datetime.now()} pytest结束执行")

    data["duration"] = data["end_time"] - data["start_time"]
    print(data)
