import requests
import json

id = "ps-pafs-LaOo_Ofm7I0cRE1piAinTmqmmoNtqGzPJjCzFSrQ0A_0R9q1Wb-ybvxfIqvtX5VF-20230322130117083003068525"
sjh = "13108219293"

def sign(id, sjh):
    authinfo = {
        "mobile": "",
        "sessionId": id,
        "tokenId": id,
        "userId": ""
    }
    authinfo = str(authinfo)
    headers = {
        'authinfo': authinfo,
        'user-agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36; unicom{version:android@10.0201,desmobile:' + sjh + '};devicetype{deviceBrand:Xiaomi,deviceModel:Redmi Note 8 Pro};{yw_code:}',
        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
    }
    data = 'drawType=B&bizFrom=225&activityId=TTLXJ20210330'
    infourl = 'https://epay.10010.com/ci-mcss-party-front/v1/ttlxj/unifyDrawNew'
    info = requests.post(infourl, headers=headers, data=data).json()
    print(info['data']['returnMsg'])


if __name__ == '__main__':
    sign(id, sjh)
