import requests, json, os

if __name__ == '__main__':
    # 环境变量缺失直接抛出 KeyError
    cookie = os.environ["MY_COOKIE"]
    
    # 域名更新
    domain = "glados.cloud"
    base_url = f"https://{domain}"
    
    headers = {
        'cookie': cookie,
        'referer': f'{base_url}/console/checkin',
        'origin': base_url,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        'content-type': 'application/json;charset=UTF-8'
    }

    # 1. 签到
    try:
        checkin_resp = requests.post(f'{base_url}/api/user/checkin', headers=headers, data=json.dumps({'token': 'glados.cloud'}))
        checkin_resp.raise_for_status()
        
        # 核心修改：只提取 message 字段
        res_json = checkin_resp.json()
        print(f"✅ 签到结果: {res_json.get('message')}") 

    except Exception as e:
        print(f"❌ Checkin Failed: {e}")

    # 2. 查询状态
    try:
        state_resp = requests.get(f'{base_url}/api/user/status', headers=headers)
        state_resp.raise_for_status()
        
        # 核心修改：只提取 leftDays 并取整
        data = state_resp.json().get('data', {})
        days = float(data.get('leftDays', 0))
        print(f"📅 剩余天数: {int(days)}")

    except Exception as e:
        print(f"❌ Status Check Failed: {e}")