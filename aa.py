import requests

url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=c7a573f8-0a6e-406d-93b2-a0754c25644d"

content = """
武汉现在气温<font color='green'>14℃</font>，<font color='red'>晴</font>，西南风3级，2023年11月17日（今日）气温<font color='green'>4~17℃</font>，空气质量轻度污染，空气质量指数88。

近几日天气信息：

2023-11-16：<font color='red'>晴</font>，<font color='green'>2~15℃</font>，西北风3-4级，空气质量良。

2023-11-17：<font color='red'>晴</font>，<font color='green'>4~17℃</font>，无持续风向<3级，空气质量轻度污染。

2023-11-18：<font color='red'>多云</font>，<font color='green'>5~18℃</font>，东北风<3级，空气质量良。

2023-11-19：<font color='red'>晴</font>，<font color='green'>6~21℃</font>，东北风<3级，空气质量良。

2023-11-20：<font color='red'>晴</font>，<font color='green'>5~22℃</font>，东北风<3级，空气质量良。

2023-11-21：<font color='red'>晴</font>，<font color='green'>7~23℃</font>，东北风<3级，空气质量良。

2023-11-22：<font color='red'>多云</font>，<font color='green'>10~20℃</font>，西南风<3级，空气质量良。

2023-11-23：<font color='red'>晴</font>，<font color='green'>0~23℃</font>，东北风<3级，空气质量良。
"""
requests.post(url, json={"msgtype": "markdown", "markdown": {"content": content}})
