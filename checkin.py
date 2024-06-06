import requests,json,os

cookie = os.environ["MY_COOKIE"]

def dailyCheckin():
    checkin_url = "https://glados.rocks/api/user/checkin"
    status_url = "https://glados.rocks/api/user/status"

    referer = 'https://glados.rocks/console/checkin'
    origin = "https://glados.rocks"

    useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
    payload = {
      'token': "glados.one"
    }
    checkin_response = requests.post(checkin_url, headers={
      'cookie': cookie,
      'referer': referer,
      'origin': origin,
      'user-agent': useragent,
      'content-type': 'application/json;charset=UTF-8'}, 
      data=json.dumps(payload))

    state_response = requests.get(status_url, headers={
      'cookie': cookie,
      'referer': referer,
      'origin': origin,
      'user-agent': useragent
    })

    checkin_data = checkin_response.json()
    state_data = state_response.json()
    print('checkin_data:', checkin_data)
    print('state_data:', state_data)


if __name__ == '__main__':
    dailyCheckin()
