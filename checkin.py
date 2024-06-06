import requests,json,os

sess = 'eyJ1c2VySWQiOjEzMzM2NSwiX2V4cGlyZSI6MTcxNzM4MjEzNTYyMywiX21heEFnZSI6MjU5MjAwMDAwMDB9' # cookie中koa:sess的值
sig = 'd2Ckmilaq5XxwL2iQarkOxW2q64' # cookie中koa:sess.sig的值
cookie = 'koa:sess={0}; koa:sess.sig={1}'.format(sess, sig) # 也可直接复制相同格式的cookie 即cookie = '你的cookie'
print("cookie:",cookie)

def dailyCheckin():
    checkin_url = "https://glados.rocks/api/user/checkin"
    status_url = "https://glados.rocks/api/user/status"

    referer = 'https://glados.rocks/console/checkin'
    origin = "https://glados.rocks"

    useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
    payload = {
      'token': "glados.one"
    }

    checkin = requests.post(checkin_url, headers={'cookie': cookie, 'referer': referer, 'origin': origin,
                            'user-agent': useragent, 'content-type': 'application/json;charset=UTF-8'}, data=json.dumps(payload))

    state_response = requests.get(status_url, headers={
        'cookie': cookie,
        'referer': referer,
        'origin': origin,
        'user-agent': useragent
    })

    state_data = state_response.json()

    print('State Response:', state_data)


if __name__ == '__main__':
    dailyCheckin()
