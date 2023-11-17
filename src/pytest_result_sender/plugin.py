from datetime import datetime

import pytest
import requests

data = {
    "passed": 0,
    "failed": 0,
}


def pytest_collection_finish(session: pytest.Session):
    # 用例加载完成之后执行，包含了全部的用例
    data["total"] = len(session.items)
    print("用例的总数：", data["total"])


def pytest_runtest_logreport(report: pytest.TestReport):
    if report.when == "call":
        data[report.outcome] += 1


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

    data["pass_ratio"] = data["passed"] / data["total"] * 100
    data["pass_ratio"] = f"{data['pass_ratio']:.2f}%"

    # assert timedelta(seconds=3) > data['duration'] >= timedelta(seconds=2.5)
    # assert data['total'] == 3
    # assert data['passed'] == 2
    # assert data['failed'] == 1
    # assert data['pass_ratio'] == "66.67%"

    url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=c7a573f8-0a6e-406d-93b2-a0754c25644d"

    content = f"""
    pytest自动化测试结果

    测试时间：{data['end_time']}
    用例数量：{data['total']}
    执行时长：{data['duration']}
    测试通过数量：<font color='green'>{data['passed']}</font>
    测试失败数量：<font color='red'>{data['failed']}</font>
    测试通过率：{data['pass_ratio']}
    测试报告地址：www.baidu.com
    """
    requests.post(url, json={"msgtype": "markdown", "markdown": {"content": content}})
