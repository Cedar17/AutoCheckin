import requests, json, os

if __name__ == '__main__':
    # 环境变量缺失直接抛出 KeyError
    cookie = os.environ["MY_COOKIE"]
    
    # 域名更新
    domain = "glados.cloud"
    base_url = f"https://{domin}"
    
    headers = {
        'cookie': cookie,
        'referer': f'{base_url}/console/checkin',
        'origin': base_url,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        'content-type': 'application/json;charset=UTF-8'
    }

    # 1. 签到
    # 使用 raise_for_status() 让 HTTP 4xx/5xx 直接报错
    checkin = requests.post(f'{base_url}/api/user/checkin', headers=headers, data=json.dumps({'token': glados.cloud}))
    checkin.raise_for_status()
    print("Checkin:", checkin.json())

    # 2. 查询状态
    state = requests.get(f'{base_url}/api/user/status', headers=headers)
    state.raise_for_status()
    print("State:", state.json())
