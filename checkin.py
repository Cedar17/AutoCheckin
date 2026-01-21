import requests
import os

def checkin():
    cookie = os.environ.get("MY_COOKIE")
    if not cookie:
        raise ValueError("❌ 错误: 环境变量 MY_COOKIE 未设置")

    # 核心配置 (已更新为 glados.cloud)
    domain = "glados.cloud"
    base_url = f"https://{domain}/api/user"
    headers = {
        'cookie': cookie,
        'referer': f'https://{domain}/console/checkin',
        'origin': f'https://{domain}',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/102.0.0.0 Safari/537.36',
        'content-type': 'application/json;charset=UTF-8'
    }

    # 1. 执行签到 (直接抛出错误)
    print(f"--- 正在向 {domain} 签到 ---")
    checkin_resp = requests.post(
        f"{base_url}/checkin", 
        headers=headers, 
        json={'token': 'glados.one'}
    )
    checkin_resp.raise_for_status() # 若状态码非200直接报错
    print(f"签到响应: {checkin_resp.json()}")

    # 2. 获取状态
    print("\n--- 获取当前状态 ---")
    state_resp = requests.get(
        f"{base_url}/status", 
        headers=headers
    )
    state_resp.raise_for_status()
    print(f"账号状态: {state_resp.json()}")

if __name__ == '__main__':
    checkin()
