import requests,json,os

sess = 'eyJ1c2VySWQiOjEzMzM2NSwiX2V4cGlyZSI6MTcxNzM4MjEzNTYyMywiX21heEFnZSI6MjU5MjAwMDAwMDB9' # cookie中koa:sess的值
sig = '2pt06LMTit0oQeNx0K_0L_ugyEs' # cookie中koa:sess.sig的值
cookie = 'koa:sess={0}; koa:sess.sig={1}'.format(sess, sig) # 也可直接复制相同格式的cookie 即cookie = '你的cookie'

def dailyCheckin():
    checkin_url = "https://glados.one/api/user/checkin"
    status_url = "https://glados.one/api/user/status"
    origin = "https://glados.one"
    useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
    payload = {
      'token': "glados.one"
    }

    state_response = requests.get(status_url, headers={
        'cookie': cookie,
        'user-agent': useragent
    })

    checkin_data = checkin_response.json()
    state_data = state_response.json()

    print('Checkin Response:', checkin_data)
    print('State Response:', state_data)

    if 'message' in checkin_data:
        print('message: ', checkin_data['message'])
    else:
        print('No message found in checkin response')

    if 'data' in state_data:
        print('system_date: ', state_data['data']['system_date'])
        print('leftdays: ', state_data['data']['leftDays'].split('.')[0])
    else:
        print('No data found in state response')

if __name__ == '__main__':
    dailyCheckin()
