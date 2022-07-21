import requests
from config import *


def login(username="auto", password="sdfsdfsdf"):
    # 获取请求的URL
    url = f"{HOST}{LOGIN_API_PATH}"
    print(url)
    # 获取请求参数，以字典的格式传递
    payload = {"username": username,
               "password": password}
    # 模拟发送post请求
    res = requests.post(url, data=payload)
    # 返回Cookie
    return res.cookies, res.json()

if __name__ == '__main__':
    print(type(login("auto", "sdfsdfsdf")))
    print(login("auto", "sdfsdfsdf")[1])
    print(login()[0])