import requests
import json
import os
# -------------------------------------------------------------------------------------------
# github workflows
# -------------------------------------------------------------------------------------------
if __name__ == '__main__':

    cookie = os.environ["MY_COOKIE"]
    if cookie == None:
        print('未获取到COOKIE变量')
        exit(0)
    print("checkin_2 cookie:", cookie)

    url = "https://glados.rocks/api/user/checkin"
    url2 = "https://glados.rocks/api/user/status"

    referer = 'https://glados.rocks/console/checkin'
    origin = "https://glados.rocks"
    useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
    payload = {
        'token': 'glados.one'
    }

    checkin = requests.post(url, headers={'cookie': cookie, 'referer': referer, 'origin': origin,
                            'user-agent': useragent, 'content-type': 'application/json;charset=UTF-8'}, data=json.dumps(payload))
    state = requests.get(url2, headers={
                            'cookie': cookie, 'referer': referer, 'origin': origin, 'user-agent': useragent})

    print(checkin.text)
    print(state.text)
    # --------------------------------------------------------------------------------------------------------#
    # if checkin.status_code == 200:
    #     # 解析返回的json数据
    #     result = checkin.json()     
    #     # 获取签到结果
    #     status = result.get('message')
    #     print(status)
    #     # 获取账号当前状态
    #     result = state.json()
    #     # 获取剩余时间
    #     leftdays = int(float(result['data']['leftDays']))
    #     print(leftdays)
    #     # 获取账号email
    #     email = result['data']['email']

    #     if status == "Checkin! Get 1 Day":
    #         success += 1
    #         message_status = "签到成功，会员天数 + 1"
    #     elif status == "Please Try Tomorrow":
    #         message_status = "今日已签到"
    #     else:
    #         fail += 1
    #         message_status = "签到失败，请检查..."

    #     if leftdays is not None:
    #         message_days = f"{leftdays} 天"
    #     else:
    #         message_days = "无法获取剩余天数信息"
