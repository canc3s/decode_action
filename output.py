#2024-08-20 03:03:49
from requests import post, get
from time import sleep, time
from hashlib import md5 as md5Encode
from datetime import datetime, timedelta
from random import randint, uniform, choice
from sys import stdout, exit
from base64 import b64encode
from json import dumps
import threading
import pytz
import os
import urllib.request
import json
import sys
import random

"""主类"""
try:
    from Crypto.Cipher import AES, DES, DES3
except:
    print("检测到还未安装 pycryptodome 请按照md的方法安装")
    exit(0)
from binascii import b2a_hex, a2b_hex
from base64 import b64encode, b64decode


class Crypt:
    def __init__(self, crypt_type: str, key, iv=None, mode="ECB"):
        """

        :param crypt_type: 对称加密类型 支持AES, DES, DES3
        :param key: 密钥 (aes可选 16/32(24位暂不支持 以后遇到有需要再补)  des 固定为8 des3 24(暂不支持16 16应该也不会再使用了) 一般都为24 分为8长度的三组 进行三次des加密
        :param iv: 偏移量
        :param mode: 模式 CBC/ECB
        """
        if crypt_type.upper() not in ["AES", "DES", "DES3"]:
            raise Exception("加密类型错误, 请重新选择 AES/DES/DES3")
        self.crypt_type = AES if crypt_type.upper() == "AES" else DES if crypt_type.upper() == "DES" else DES3
        self.block_size = self.crypt_type.block_size
        if self.crypt_type == DES:
            self.key_size = self.crypt_type.key_size
        elif self.crypt_type == DES3:
            self.key_size = self.crypt_type.key_size[1]
        else:
            if len(key) <= 16:
                self.key_size = self.crypt_type.key_size[0]
            elif len(key) > 24:
                self.key_size = self.crypt_type.key_size[2]
            else:
                self.key_size = self.crypt_type.key_size[1]
                print("当前aes密钥的长度只填充到24 若需要32 请手动用 chr(0) 填充")
        if len(key) > self.key_size:
            key = key[:self.key_size]
        else:
            if len(key) % self.key_size != 0:
                key = key + (self.key_size - len(key) % self.key_size) * chr(0)
        self.key = key.encode("utf-8")
        if mode == "ECB":
            self.mode = self.crypt_type.MODE_ECB
        elif mode == "CBC":
            self.mode = self.crypt_type.MODE_CBC
        else:
            raise Exception("您选择的加密模式错误")
        if iv is None:
            self.cipher = self.crypt_type.new(self.key, self.mode)
        else:
            if isinstance(iv, str):
                iv = iv[:self.block_size]
                self.cipher = self.crypt_type.new(self.key, self.mode, iv.encode("utf-8"))
            elif isinstance(iv, bytes):
                iv = iv[:self.block_size]
                self.cipher = self.crypt_type.new(self.key, self.mode, iv)
            else:
                raise Exception("偏移量不为字符串")

    def encrypt(self, data, padding="pkcs7", b64=False):
        """

        :param data: 目前暂不支持bytes 只支持string 有需求再补
        :param padding: pkcs7/pkck5 zero
        :param b64: 若需要得到base64的密文 则为True
        :return:
        """
        pkcs7_padding = lambda s: s + (self.block_size - len(s.encode()) % self.block_size) * chr(
            self.block_size - len(s.encode()) % self.block_size)
        zero_padding = lambda s: s + (self.block_size - len(s) % self.block_size) * chr(0)
        pad = pkcs7_padding if padding == "pkcs7" else zero_padding
        data = self.cipher.encrypt(pad(data).encode("utf8"))
        encrypt_data = b64encode(data) if b64 else b2a_hex(data)  # 输出hex或者base64
        return encrypt_data.decode('utf8')

    def decrypt(self, data, b64=False):
        """
        对称加密的解密
        :param data: 支持bytes base64 hex list 未做填充 密文应该都是数据块的倍数 带有需求再补
        :param b64: 若传入的data为base64格式 则为True
        :return:
        """
        if isinstance(data, list):
            data = bytes(data)
        if not isinstance(data, bytes):
            data = b64decode(data) if b64 else a2b_hex(data)
        decrypt_data = self.cipher.decrypt(data).decode()
        # 去掉padding
        # pkcs7_unpadding = lambda s: s.replace(s[-1], "")
        # zero_unpadding = lambda s: s.replace(chr(0), "")
        # unpadding = pkcs7_unpadding if padding=="pkcs7" else zero_unpadding
        unpadding = lambda s: s.replace(s[-1], "")
        return unpadding(decrypt_data)


class China_Unicom:
    def __init__(self, phone_num, run_ua):
        self.phone_num = phone_num
        default_ua = f"Mozilla/5.0 (iPhone; CPU iPhone OS {randint(15, 17)}_{randint(0, 6)} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 unicom{{version:iphone_c@11.0{randint(0, 6)}00}}"
        if run_ua is None or run_ua == "":
            run_ua = default_ua
        # print("使用的UA："+run_ua)

        self.headers = {
            "Host": "10010.woread.com.cn",
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN,zh-Hans;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Content-Type": "application/json;charset=utf-8",
            'accesstoken': "ODZERTZCMjA1NTg1MTFFNDNFMThDRDYw",
            "Origin": "https://10010.woread.com.cn",
            "User-Agent": run_ua,
            "Connection": "keep-alive",
            "Referer": "https://10010.woread.com.cn/ng_woread/",
        }
        self.fail_num = 0

    def timestamp(self):
        return round(time() * 1000)

    def print_now(self, content):
        print(content)
        stdout.flush()

    def md5(self, str):
        m = md5Encode(str.encode(encoding='utf-8'))
        return m.hexdigest()

    def req(self, url, crypt_text, retry_num=2):
        while retry_num > 0:
            body = {"sign": b64encode(
                Crypt(crypt_type="AES", key="woreadst^&*12345", iv="16-Bytes--String", mode="CBC").encrypt(
                    crypt_text).encode()).decode()}
            self.headers["Content-Length"] = str(len(dumps(body).replace(" ", "")))
            try:
                res = post(url, headers=self.headers, json=body)
                data = res.json()
                return data
            except Exception as e:
                retry_num -= 1
                return self.req(url, crypt_text, retry_num)

    def referer_login(self):
        date = datetime.datetime.today().strftime("%Y%m%d%H%M%S")
        timestamp = self.timestamp()
        url = f"https://10010.woread.com.cn/ng_woread_service/rest/app/auth/10000002/{timestamp}/{self.md5(f'100000027k1HcDL8RKvc{timestamp}')}"
        crypt_text = f'{{"timestamp":"{date}"}}'
        body = {
            "sign": b64encode(Crypt(crypt_type="AES", key="1234567890abcdef").encrypt(crypt_text).encode()).decode()}
        self.headers["Content-Length"] = str(len(str(body)) - 1)
        data = post(url, headers=self.headers, json=body).json()
        if data["code"] == "0000":
            self.headers["accesstoken"] = data["data"]["accesstoken"]

        else:
            self.print_now(f"设备登录失败,日志为{data}")
            exit(0)

    def get_userinfo(self):
        date = datetime.today().strftime("%Y%m%d%H%M%S")
        url = "https://10010.woread.com.cn/ng_woread_service/rest/account/login"
        crypt_text = f'{{"phone":"{self.phone_num}","timestamp":"{date}"}}'
        data = self.req(url, crypt_text)
        if data["code"] == "0000":
            self.userinfo = data["data"]
            print(f"登录账号{data['data']['phone']}成功")
        else:
            self.print_now(f"手机号登录失败, 日志为{data}")
            exit(0)

    def lqrenwu(self):
        url = "https://10010.woread.com.cn/ng_woread_service/rest/activity423/receiveActiveTask"
        date = datetime.today().__format__("%Y%m%d%H%M%S")
        crypt_text = f'{{"activeId":{active_id},"taskId":{_240task_id},"timestamp":"{date}","token":"{self.userinfo["token"]}","userId":"{self.userinfo["userid"]}","userIndex":{self.userinfo["userindex"]},"userAccount":"{self.userinfo["phone"]}","verifyCode":"{self.userinfo["verifycode"]}"}}'
        data = self.req(url, crypt_text)
        if 'innercode' in data and (data['innercode']) == "7777":
            self.get_userinfo()
        if 'data' in data:
            print(data['data'])
        else:
            print(data['message'])

    def lqre(self):
        url = "https://10010.woread.com.cn/ng_woread_service/rest/activity423/receiveActiveTask"
        date = datetime.today().__format__("%Y%m%d%H%M%S")
        crypt_text = f'{{"activeId":{active_id},"taskId":{_120task_id},"timestamp":"{date}","token":"{self.userinfo["token"]}","userId":"{self.userinfo["userid"]}","userIndex":{self.userinfo["userindex"]},"userAccount":"{self.userinfo["phone"]}","verifyCode":"{self.userinfo["verifycode"]}"}}'
        data = self.req(url, crypt_text)
        if 'innercode' in data and (data['innercode']) == "7777":
            self.get_userinfo()
        if 'data' in data:
            print(data['data'])
        else:
            print(data['message'])

    def yuedu(self):
        url = "https://10010.woread.com.cn/ng_woread_service/rest/history/addReadTime"
        while True:
            timestamp = self.timestamp()
            date = datetime.today().strftime("%Y%m%d%H%M%S")
            crypt_text = f'{{"timestamp":"{date}","token":"{self.userinfo["token"]}","userId":"{self.userinfo["userid"]}","readTime":2,"cntindex":"409672","cntIndex":"409672","cnttype":"1","cntType":1,"cardid":"11891","catid":"118411","pageIndex":"10683","chapterseno":1,"channelid":"","chapterid":"-1","readtype":1,"isend":"0","signtimestamp":{timestamp}}}'
            data = self.req(url, crypt_text)
            if 'innercode' in data and data['innercode'] == "7777":
                self.get_userinfo()
            if 'data' in data:
                num_times_two = data['data']['num'] * 2
                print(f"{self.phone_num}已经刷了{num_times_two}分钟")
                if num_times_two >= 240:
                    self.cxrenwu()
                    break
                random_time = random.randint(123, 150)
                sleep(random_time)
            else:
                print("刷阅读失败：短时间内请求过多或者网络问题")
                random_time = random.randint(123, 150)
                sleep(random_time)

    def cxrenwu(self):
        url = "https://10010.woread.com.cn/ng_woread_service/rest/activity423/queryCurTaskStatus"
        timestamp = self.timestamp()
        date = datetime.today().__format__("%Y%m%d%H%M%S")
        crypt_text = f'{{"activeIndex":{active_id},"timestamp":"{date}","token":"{self.userinfo["token"]}","userId":"{self.userinfo["userid"]}","userIndex":{self.userinfo["userindex"]},"userAccount":"{self.userinfo["phone"]}","verifyCode":"{self.userinfo["verifycode"]}"}}'
        data = self.req(url, crypt_text)
        try:
            ids = [item['id'] for item in data['data'] if 'id' in item]
            number_of_ids = len(ids)
            for id_value in ids:
                self.liqujl(id_value)
            self.cjrenwu()
            sleep(2)
            self.cxye()
        except Exception as e:
            self.cjrenwu()
            sleep(2)
            self.cxye()

    def liqujl(self, id_value):
        url = "https://10010.woread.com.cn/ng_woread_service/rest/activity423/completeActiveTask"
        timestamp = self.timestamp()
        date = datetime.today().__format__("%Y%m%d%H%M%S")
        crypt_text = f'{{"taskId":{id_value},"timestamp":"{date}","token":"{self.userinfo["token"]}","userId":"{self.userinfo["userid"]}","userIndex":{self.userinfo["userindex"]},"userAccount":"{self.userinfo["phone"]}","verifyCode":"{self.userinfo["verifycode"]}"}}'
        data = self.req(url, crypt_text)
        if (data['code']) == "0000":
            groupName = data['data']['exchangeResult']['materialGroupInfo']['groupName']
            print(f"{self.phone_num}领取{groupName}成功")

    def cjrenwu(self):
        url = "https://10010.woread.com.cn/ng_woread_service/rest/activity423/drawReadActivePrize"
        timestamp = self.timestamp()
        date = datetime.today().__format__("%Y%m%d%H%M%S")
        crypt_text = f'{{"activeIndex":{active_id},"timestamp":"{date}","token":"{self.userinfo["token"]}","userId":"{self.userinfo["userid"]}","userIndex":{self.userinfo["userindex"]},"userAccount":"{self.userinfo["phone"]}","verifyCode":"{self.userinfo["verifycode"]}"}}'
        data = self.req(url, crypt_text)
        if (data['code']) == "0000":
            cjhd = data['data']['prizedesc']
            print(f"{self.phone_num}抽奖获得{cjhd}")

    def cxye(self):
        url = "https://10010.woread.com.cn/ng_woread_service/rest/phone/vouchers/queryTicketAccount"
        timestamp = self.timestamp()
        date = datetime.today().__format__("%Y%m%d%H%M%S")
        crypt_text = f'{{"timestamp":"{date}","token":"{self.userinfo["token"]}","userId":"{self.userinfo["userid"]}","userIndex":{self.userinfo["userindex"]},"userAccount":"{self.userinfo["phone"]}","verifyCode":"{self.userinfo["verifycode"]}"}}'
        data = self.req(url, crypt_text)
        if (data['code']) == "0000":
            hbcx = data['data']['usableNum'] / 100
            print(f"{self.phone_num}阅读区话费红包余额{hbcx}元")

    def main(self):
        # self.referer_login()
        self.get_userinfo()
        current_hour = datetime.now().hour
        if current_hour == 23:
            url = "https://api.m.taobao.com/rest/api3.do?api=mtop.common.getTimestamp"
            try:
                with urllib.request.urlopen(url) as response:
                    datal = response.read().decode('utf-8')
                    json_data = json.loads(datal)
                    wlsjc_str = json_data.get('data', {}).get('t')  # 获取t的字符串值
                    wlsjc = int(wlsjc_str)
            except urllib.error.URLError as e:
                print(f"GET请求失败")
            now = datetime.fromtimestamp(wlsjc / 1000)
            next_day = now + timedelta(days=1)
            next_day = next_day.replace(hour=0, minute=0, second=0, microsecond=0)
            delta = next_day - now
            seconds = delta.total_seconds()
            if wlsjc / 1000 > ymsjc:
                print(gongg)
                exit()
            print(f"距离下一天零点还有 {seconds:.0f} 秒")
            if 'zdf' in locals() and zdf is not None:
                zdyz = int(zdy)
            else:
                zdyz = 3

            sleep(seconds - zdyz)
            threads = []
            for _ in range(dys):
                thread = threading.Thread(target=self.lqrenwu)
                threads.append(thread)
                thread.start()
                sleep(0.1)
            for _ in range(2):
                thread_lqre = threading.Thread(target=self.lqre)
                threads.append(thread_lqre)
                thread_lqre.start()
                sleep(0.1)
            for thread in threads:
                thread.join()
        else:
            self.yuedu()


def start(phone, run_ua, ):
    if phone == "":
        exit(0)
    China_Unicom(phone, run_ua).main()


if __name__ == "__main__":
    """读取环境变量"""
    url = "https://gitee.com/kele2233/genxin/raw/master/ltydd.json"
    try:
        with urllib.request.urlopen(url) as response:
            data = response.read()
            json_data = json.loads(data)
            ging = json_data.get('gin')  # 获取 gongg 的值
            fwbbh = json_data.get('fwbbh')  # 获取 gongg 的值
            gonggg = json_data.get('gongg')  # 获取 gongg 的值
            active_id = '18'
            _240task_id = json_data.get('240taskId')
            _120task_id = json_data.get('120taskId')
            ymsjc = json_data.get('ydsjc')
            gongg = json_data.get('gong')
            dys = json_data.get('dys')
            bbh = 2.3
            if bbh >= fwbbh:
                print(f"公告: {ging}\n当前版本号{bbh}最新版号{fwbbh}")  # 在主线程中打印 gongg 的值
            else:
                print(f"{gonggg}\n当前版本号{bbh}最新版号{fwbbh}")
                exit(1)
    except urllib.error.URLError as e:
        exit(1)
    PHONE_NUM = os.getenv("PHONE_NUM", "")
    if PHONE_NUM:
        phone = PHONE_NUM.split("&")[0]
    else:
        phone = ""

    zdy = os.getenv("YDYC")

    if phone:
        print(f'开始执行第1个账号：{phone}')
        p = threading.Thread(target=start, args=(phone, None))
        p.start()
        p.join()  # 等待当前线程完成

