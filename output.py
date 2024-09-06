#2024-09-06 02:40:31
import requests
import json
import os
import time
class HXSS():
    def __init__(self,token,tk):
        self.token = token
        self.tk = tk
    def sign(self):
        print('🏋--> 签到')
        try:
            headers = {
                "accept": "application/json",
                "osversion": "13",
                "release": "1.0.2",
                "version": "2",
                "platform": "1",
                "Authorization": self.token,
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 13; M2012K11AC Build/TKQ1.220829.002)",
                "Host": "hxss.yichengwangluo.net",
                "Connection": "Keep-Alive",
                "Accept-Encoding": "gzip",
                "Content-Length": "0"
            }
            url = "https://hxss.yichengwangluo.net/api/v2/reward/sign"
            response = requests.post(url, headers=headers).json()
            if response['code'] == 0:
                print('🎉{} 获得{}'.format(response['result']['message'],response['result']['coin']))
                time.sleep(5)
            else:
                print('❗{}'.format(response['message']))
                time.sleep(5)
        except Exception as e:
            print('❗{}'.format(e))
    #半小时一次
    def vedio_task(self):
        print('🏋--> 激励视频')
        try:
            headers = {
                "accept": "application/json",
                "osversion": "13",
                "release": "1.0.2",
                "version": "2",
                "platform": "1",
                "Authorization": self.token,
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 13; M2012K11AC Build/TKQ1.220829.002)",
                "Host": "hxss.yichengwangluo.net",
                "Connection": "Keep-Alive",
                "Accept-Encoding": "gzip",
                "Content-Length": "0"
            }
            url = "https://hxss.yichengwangluo.net/api/v2/reward/rain"
            response = requests.post(url, headers=headers).json()
            if response['success'] == True:
                print('🎉半小时运行一次的任务 金币：{}提现券：{}'.format(response['result']['coin'],response['result']['coupon']))
                time.sleep(5)
            else:
                print("❗{}".format(response['message']))
                time.sleep(5)
        except Exception as e:
            print('❗{}'.format(e))

    def vedio(self):
        print('🏋--> 30次视频')
        for i in range(30):
            try:
                headers = {
                    "accept": "application/json",
                    "osversion": "13",
                    "release": "1.0.2",
                    "version": "2",
                    "platform": "1",
                    "Authorization": self.token,
                    "ssaid": "960bb891a494179d",
                    "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 13; M2012K11AC Build/TKQ1.220829.002)",
                    "Host": "hxss.yichengwangluo.net",
                    "Connection": "Keep-Alive",
                    "Accept-Encoding": "gzip"
                }
                url = "https://hxss.yichengwangluo.net/api/v2/ads/action/completed"
                params = {
                    "ticket": self.tk,
                }
                response = requests.get(url, headers=headers, params=params).json()
                if response['success'] == True:
                    print('🎉第{}次视频 金币：{}提现券：{}'.format(i+1,response['result']['reward'], response['result']['coupon']))
                    time.sleep(15)
                else:
                    print("❗{}".format(response['message']))
                    break
                    time.sleep(5)
            except Exception as e:
                print('❗{}'.format(e))
                break

    def read_task(self):
        print('🏋--> 阅读')
        for i in range(10):
            try:
                headers = {
                    "osversion": "13",
                    "release": "1.0.2",
                    "version": "2",
                    "platform": "1",
                    "Authorization": self.token,
                    "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 13; M2012K11AC Build/TKQ1.220829.002)",
                    "Host": "hxss.yichengwangluo.net",
                    "Connection": "Keep-Alive",
                    "Accept-Encoding": "gzip"
                }
                url = "https://hxss.yichengwangluo.net/api/v2/news/sdk/zhuan/count"
                params = {
                    "isfirstopen": "0"
                }
                response = requests.get(url, headers=headers, params=params).json()
                if response['success'] == True:
                    print('🎉第{}次阅读 成功'.format(i + 1))
                    time.sleep(5)
                elif response['result']['cnt'] == 10:
                    print('❗阅读已达上限')
                    time.sleep(5)
                    break
                else:
                    print("❗{}".format(response))
                    time.sleep(5)
                    break
            except Exception as e:
                print('❗{}'.format(e))
                break

    def shua_vedio(self):
        print('🏋--> 刷视频')
        for i in range(10):
            try:
                headers = {
                    "accept": "application/json",
                    "osversion": "13",
                    "release": "1.0.2",
                    "version": "2",
                    "platform": "1",
                    "Authorization": self.token,
                    "ssaid": "960bb891a494179d",
                    "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 13; M2012K11AC Build/TKQ1.220829.002)",
                    "Host": "hxss.yichengwangluo.net",
                    "Connection": "Keep-Alive",
                    "Accept-Encoding": "gzip"
                }
                url = "https://hxss.yichengwangluo.net/api/v2/video/coin"
                params = {
                    "ticket": self.tk
                }
                response = requests.get(url, headers=headers, params=params).json()
                if response['success'] == True:
                    print('🎉第{}次刷视频 成功'.format(i + 1))
                    time.sleep(15)
                elif response['result']['cnt'] == 10:
                    print('❗刷视频任务 已达上限')
                    time.sleep(5)
                    break
                else:
                    print("❗{}".format(response))
                    time.sleep(5)
                    break
            except Exception as e:
                print('❗{}'.format(e))
                break

    def lq(self):
        print('🏋--> 领取奖励')
        headers = {
            "accept": "application/json",
            "device": "1dd9ebe6e0d9db97",
            "oaid": "1dd9ebe6e0d9db97",
            "st": "BUkmerpbDRucQK8RatsX4_oiEFYJFJye1jFOsTFnof9jo7H_eEwCyCdBWns2gV483NsfkzFY0KB96BhfO0HXfK2ojyMM3FaNYF5Xbgvf2qzD4rSKG4HUr5rHs2EINqV4eGVF_R0GwN8X2Pkzlfvs_fwEqbwvkstomd8OULCUaSSI*",
            "store": "website",
            "brand": "Redmi",
            "model": "M2012K11AC",
            "osversion": "13",
            "release": "1.0.2",
            "version": "2",
            "platform": "1",
            "Authorization": "Bearer eyJ0eXAiOiJKV1MiLCJhbGciOiJIUzUxMiJ9.eyJleHAiOjE3NDg1MTU4MzAsImlhdCI6MTcxNjk3OTgzMCwibmJmIjoxNzE2OTc5ODMwLCJpc3MiOiJodHRwOlwvXC9oeHNzLnlpY2hlbmd3YW5nbHVvLm5ldCIsImF1ZCI6Imh0dHA6XC9cL2h4c3MueWljaGVuZ3dhbmdsdW8ubmV0IiwianRpIjoiNjY1NzA4NzY2Y2YyZCIsInN1YiI6NTY2ODgwfQ.MDk2OTU0N2ZkZTIwNmQyMzFhZTRhMDE1MDhkZTNiM2E0OTM5NjQ2Nzk3MTc4MDBiYmI2NjlmNDVhYmVkNGU1Nzc2OTA3OTNhNDRiMWFkY2YyMTU0ZTUxYTFlZDIzYzE1ZDc3MjZhY2JmZTRmMzJlODBjZWIwNzdmNTE1Yjc2Njk",
            "ssaid": "960bb891a494179d",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 13; M2012K11AC Build/TKQ1.220829.002)",
            "Host": "hxss.yichengwangluo.net",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip",
            "Content-Length": "5"
        }
        url = "https://hxss.yichengwangluo.net/api/v2/zhuan/done"
        try:
            data = {
                "id": "24"
            }
            response = requests.post(url, headers=headers, data=data).json()
            if response['success'] == True:
                print('🎉领取 金币：{}提现券：{}'.format(response['result']['coin'], response['result']['coupon']))
                time.sleep(2)
            else:
                print('❗领取上限')
                time.sleep(2)
        except Exception as e:
            print('❗{}'.format(e))
            time.sleep(2)

        try:
            data = {
                "id": "7"
            }
            response = requests.post(url, headers=headers, data=data).json()
            if response['success'] == True:
                print('🎉领取 金币：{}提现券：{}'.format(response['result']['coin'], response['result']['coupon']))
                time.sleep(2)
            else:
                print('❗领取上限')
                time.sleep(2)
        except Exception as e:
            print('❗{}'.format(e))
            time.sleep(2)


if __name__ == '__main__':
    st = os.getenv('tz_hxss')
    if not st:
        print('❗请检查环境变量')
    token_list = os.environ.get('tz_hxss').strip().split('&')
    print('🔔共获取到{}个账号 开始运行欢喜刷刷'.format(len(token_list)))
    for i,item in enumerate(token_list):
        parts = item.split('#')
        token = parts[0]
        tk = parts[1]
        print('👑开始执行第{}个账号'.format(i + 1))
        hxss = HXSS(token,tk)
        hxss.sign()
        hxss.vedio()
        hxss.vedio_task()
        hxss.shua_vedio()
        hxss.read_task()
        hxss.lq()
