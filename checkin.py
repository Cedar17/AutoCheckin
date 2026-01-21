import requests
import os

# 提取公共请求头，减少重复代码
COMMON_UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'

def glados_checkin():
    key = os.environ.get("GLADOS_COOKIE")
    if not key: return print("❌ [GLaDOS] 缺少 Cookie")

    try:
        # 使用 Session 复用 TCP 连接
        with requests.Session() as s:
            s.headers.update({'cookie': key, 'user-agent': COMMON_UA})
            base = "https://glados.cloud/api/user"
            
            # 1. 签到 (直接用 json 参数，自动处理 headers 和 dumps)
            checkin = s.post(f'{base}/checkin', json={'token': 'glados.cloud'}).json()
            print(f"✅ [GLaDOS] 签到: {checkin.get('message')}")

            # 2. 查询
            status = s.get(f'{base}/status').json()
            days = int(float(status.get('data', {}).get('leftDays', 0)))
            print(f"📅 [GLaDOS] 剩余: {days} 天")
            
    except Exception as e:
        print(f"❌ [GLaDOS] 错误: {e}")

def pter_checkin():
    key = os.environ.get("PTER_COOKIE")
    if not key: return print("❌ [PTer] 缺少 Cookie")

    headers = {
        'cookie': key,
        'user-agent': COMMON_UA,
        'x-requested-with': 'XMLHttpRequest', # 关键 Header
        'referer': 'https://pterclub.net/index.php'
    }

    try:
        res = requests.get("https://pterclub.net/attendance-ajax.php", headers=headers, timeout=10).json()
        
        icon = "✅" if res.get('status') == "1" else "⚠️"
        print(f"{icon}  [PTer] 消息: {res.get('message')}")

    except Exception as e:
        print(f"❌ [PTer] 错误: {e}")

if __name__ == '__main__':
    print("--- 开始签到 ---")
    glados_checkin()
    pter_checkin()
    print("--- 任务结束 ---")