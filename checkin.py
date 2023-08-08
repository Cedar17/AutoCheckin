import requests,json,os

sess = 'eyJ1c2VySWQiOjEzMzM2NSwiX2V4cGlyZSI6MTY4OTYwMjAzMzYyNywiX21heEFnZSI6MjU5MjAwMDAwMDB9' # cookie中koa:sess的值
sig = 't9dWD9xMN5aqsp2ZU8biDruUpvg' # cookie中koa:sess.sig的值
cookie = 'koa:sess={0}; koa:sess.sig={1}'.format(sess, sig) # 也可直接复制相同格式的cookie 即cookie = '你的cookie'

def dailyCheckin():
    checkin_url = "https://glados.rocks/api/user/checkin"
    status_url = "https://glados.rocks/api/user/status"
    origin = "https://glados.rocks"
    useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
    payload = {
      'token': "glados.network"
    }

    checkin = requests.post(checkin_url, headers = {
      'cookie': cookie ,
      'origin':origin,
      'user-agent':useragent,
      'content-type':'application/json;charset=UTF-8'
    }, data = json.dumps(payload))

    state =  requests.get(status_url, headers = {
      'cookie': cookie ,
      'user-agent':useragent
    })
    dict = json.loads(checkin.text) # 获取返回的信息，其中message含有结果信息

    print('message: '+json.loads(checkin.text)['message'])
    print('system_date: '+json.loads(state.text)['data']['system_date'])
    print('leftdays: '+json.loads(state.text)['data']['leftDays'].split('.')[0])

if __name__ == '__main__':

    dailyCheckin()   
