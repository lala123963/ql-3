"""
cron: 0 8 * * *
new Env('glados签到');
glados签到(免费梯子)
地址：https://glados.rocks
抓包域名: https://glados.rocks/api/user/checkin
抓包请求头里面: cookie 包含 _ga,_gid..等复制cookie填入变量
环境变量 gladosck = cookie的值
多账号新建变量或者用 & 分开

"""
import time
import requests
from os import environ, system, path


def load_send():
    global send, mg
    cur_path = path.abspath(path.dirname(__file__))
    if path.exists(cur_path + "/notify.py"):
        try:
            from notify import send
            print("加载通知服务成功！")
        except:
            send = False
            print("加载通知服务失败~")
    else:
        send = False
        print("加载通知服务失败~")


load_send()


def get_environ(key, default="", output=True):
    def no_read():
        if output:
            if key == "gladosck":
                print(f"未填写环境变量 {key} 请添加")
        return default

    return environ.get(key) if environ.get(key) else no_read()


class Glados():
    def __init__(self, ck):
        self.msg = ''
        self.ck = ck

    def sign(self):
        time.sleep(1)
        url = "https://glados.rocks/api/user/checkin"
        headers = {
            'Cookie': self.ck,
            'sec-ch-ua': '"Microsoft Edge";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        }

        data = {
            "token": "glados.network"
        }
        r = requests.post(url, headers=headers, json=data).json()
        xx = "[账号]{}\n[签到]{}\n\n".format(a, r['message'])
        self.msg += xx
        return self.msg


if __name__ == '__main__':
    token = get_environ("gladosck") if environ.get("gladosck") else refresh_token
    msg = ''
    cks = token.split("&")
    print("检测到{}个ck记录".format(len(cks)))
    print()
    a = 0
    for ck in cks:
        a += 1
        run = Glados(ck)
        msg += run.sign()
    send("glados签到通知", msg)
