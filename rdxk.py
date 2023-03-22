"""
cron: 0 9 * * *
new Env('热度星客');

热度星客签到脚本
地址：https://m.reduxingke.com/down/register.html?spread=279954&incode=XK28995483
抓包域名: m.reduxingke.com
抓包请求: Authori-zation: Bearer XXXXX
环境变量 rdxkck = Bearer XXXXX
仅支持企业微信机器人推送
"""

import requests
from os import environ


def sign(authorization):
    headers = {
        "authori-zation": authorization,
        "User-Agent": "Mozilla/5.0 (Linux; Android 11;Redmi Note 8 Pro Build/RP1A.200720.011;wv)AppleWebKit/537.36(KHTML./like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/4435 MMWEBSDK/20230202 Mobile Safari/537.36 MMWEBID/9516MicroMessenger/8.0.33.2320(0x28002151) WeChat/arm64 Weixin NetType/4G Language/zh_CN ABI/arm64 MiniProgramEnv/android",
    }
    url = 'https://m.reduxingke.com/api/usersign/sign'
    response = requests.post(url, headers=headers).json()

    infourl = 'https://m.reduxingke.com/api/userinfo'
    info = requests.get(infourl, headers=headers).json()

    names = '用户：' + info['data']['nickname']
    print(names)
    yue = response['msg'] + " 余额：" + info['data']['brokerage_price']
    print(yue)
    ts_msg = "热度星客签到\n" + names + "\n" + yue
    QYWX_KEY = get_environ("QYWX_KEY")
    webhook = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=" + QYWX_KEY
    headers = {"Content-Type": "text/plain"}
    data = {
        "msgtype": "text",
        "text": {
            "content": ts_msg
        }

    }
    if QYWX_KEY != "":

        r = requests.post(url=webhook, headers=headers, json=data).json()
        if r["errmsg"] == "ok":
            print("企业微信机器人推送成功")
        else:
            print("企业微信机器人推送失败")
        print()
    else:
        print()


def get_environ(key, default="", output=True):
    def no_read():
        if output:
            if key == "rdxkck":
                print(f"未填写环境变量 {key} 请添加")
        return default

    return environ.get(key) if environ.get(key) else no_read()


if __name__ == '__main__':
    authori_zation = get_environ("rdxkck")

    cks = authori_zation.split("&")
    print("检测到{}个ck记录\n开始热度星客签到".format(len(cks)))
    print()
    for ck in cks:
        try:
            sign(ck)
        except KeyError:
            print("请检查ck是否正确")
            print()
