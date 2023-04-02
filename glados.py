"""
cron: 0 8 * * *
new Env('glados签到');

glados签到(免费梯子)
抓包域名: https://glados.rocks/api/user/checkin
抓包请求头里面: cookie 包含 _ga,_gid..等复制cooker填入变量
环境变量 gladosck = xxxxx
多账号新建变量或者用 & 分开

"""
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


def sign(ck):
    url = "https://glados.rocks/api/user/checkin"
    headers = {
        'Cookie': ck,
        'sec-ch-ua': '"Microsoft Edge";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    }

    data = {
        "token": "glados.network"
    }
    r = requests.post(url, headers=headers, json=data).json()
    xx = "[账号{}]\n[签到]{}\n".format(a, r['message'])
    print(xx)
    msg += "[账号{}]\n[签到]{}\n".format(a, r['message'])


if __name__ == '__main__':
    token = get_environ("gladosck")
    cks = token.split("&")
    print("检测到{}个ck记录\n开始统一快乐星球签到".format(len(cks)))
    print()
    a = 0
    for ck in cks:
        c = ck.split('&')
        msg = "glados通知\n"
        for i in c:
            a += 1
            sign(i)
            print()
    send(msg)
