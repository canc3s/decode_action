#2024-09-02 02:48:43
import json 
import os 
import time 
import requests 
import random 
def get_id(OOOOO00OO0000O000,OO0O00000000O0O00):
 OO00OO00O00O0O00O={"Accept":"*/*","Accept-Encoding":"gzip, deflate, br","Accept-Language":"zh-CN,zh;q=0.9","Connection":"keep-alive","Content-Length":"2","Content-Type":"application/x-www-form-urlencoded","Host":"mili.shensemiao.com","Referer":"https://servicewechat.com/wxec97c88d99c5d385/4/page-frame.html","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"cross-site","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090b19)XWEB/11253","xweb_xhr":"1"}
 OOO0O00O0O00O00OO={"v":"1","appid":"4","appsecret":"PHPCMF19F5DF41B263B","":"","api_auth_code":f"{OOOOO00OO0000O000}","api_auth_uid":f"{OO0O00000000O0O00}","s":"member","app":"yhxcx","c":"qd","m":"sign_in"}
 OOOOO000O00O00O00={}
 O00OOO0O00O0OOO00=requests.post('https://mili.shensemiao.com/index.php',headers=OO00OO00O00O0O00O,json=OOOOO000O00O00O00,params=OOO0O00O0O00O00OO)
 print(O00OOO0O00O0OOO00.status_code)
 if O00OOO0O00O0OOO00.status_code==200:
  O00OOO0O00O0OOO00=O00OOO0O00O0OOO00.json()
  return O00OOO0O00O0OOO00['data']['qdpzData']['llfb']
def liulan(OO00O0OOO0000OOO0,O000O0000O0OO0OO0,O000OOOOO00000OOO):
 O0OOOOO0OOO000O00={"Accept":"*/*","Accept-Encoding":"gzip, deflate, br","Accept-Language":"zh-CN,zh;q=0.9","Connection":"keep-alive","Content-Length":"46","Content-Type":"application/x-www-form-urlencoded","Host":"mili.shensemiao.com","Referer":"https://servicewechat.com/wxec97c88d99c5d385/4/page-frame.html","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"cross-site","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090b19)XWEB/11253","xweb_xhr":"1"}
 O00O000O0O0000OO0={"v":"1","appid":"4","appsecret":"PHPCMF19F5DF41B263B","":"","api_auth_code":f"{OO00O0OOO0000OOO0}","api_auth_uid":f"{O000O0000O0OO0OO0}","s":"Yhxcx","c":"home","m":"fb_detail"}
 OO00OO0OOOOOO00O0=f'id={O000OOOOO00000OOO}&pattern=signin&patternid=1&wcs=0&wdfb='
 O0OO0OOOO0OO0OOOO=requests.post('https://mili.shensemiao.com/index.php',headers=O0OOOOO0OOO000O00,params=O00O000O0O0000OO0,data=OO00OO0OOOOOO00O0)
 if O0OO0OOOO0OO0OOOO.status_code==200:
  print(O0OO0OOOO0OO0OOOO.status_code)
  return True 
def browse(O0O00000O0O000OOO,O0O0O000O00O00O0O,OO0000OO000O0OOOO,t=0):
 OO00O0O0O000O000O={"Accept":"*/*","Accept-Encoding":"gzip, deflate, br","Accept-Language":"zh-CN,zh;q=0.9","Connection":"keep-alive","Content-Length":"43","Content-Type":"application/x-www-form-urlencoded","Host":"mili.shensemiao.com","Referer":"https://servicewechat.com/wxec97c88d99c5d385/4/page-frame.html","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"cross-site","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090b19)XWEB/11253","xweb_xhr":"1"}
 O0OO00OOOO000OO00={"v":"1","appid":"4","appsecret":"PHPCMF19F5DF41B263B","":"","api_auth_code":f"{O0O00000O0O000OOO}","api_auth_uid":f"{O0O0O000O00O00O0O}","s":"member","app":"Yhxcx","c":"qd","m":"sign_in"}
 O000O0O0O00O0OO00=f'id={OO0000OO000O0OOOO}&fblx=1&wcs={t}&theway=signin&search=1'
 OOOO00OOOOO0OOO00=requests.post('https://mili.shensemiao.com/index.php',headers=OO00O0O0O000O000O,params=O0OO00OOOO000OO00,data=O000O0O0O00O0OO00)
 if OOOO00OOOOO0OOO00.status_code==200:
  try:
   OOOO00OOOOO0OOO00=OOOO00OOOOO0OOO00.json()
   if 'llurl'in OOOO00OOOOO0OOO00.get('data',{}):
    OOO0OOO0000O00O00=OOOO00OOOOO0OOO00['data']['llurl']
    O0OO000O00OO000O0=OOO0OOO0000O00O00.split("id=")[-1]
    return O0OO000O00OO000O0 
   else:
    print(OOOO00OOOOO0OOO00)
  except Exception as O00OO000O000OO0OO:
   print(O00OO000O000OO0OO)
def print_ascii_art():
 print("// ┏┓   ┏┓")
 print("// ┏┛┻━━━┛┻┓")
 print("// ┃       ┃")
 print("// ┃   ━   ┃")
 print("// ┃ ┳┛ ┗┳ ┃")
 print("// ┃       ┃")
 print("// ┃   ┻   ┃")
 print("// ┃       ┃")
 print("// ┗━┓   ┏━┛")
 print("// ┃   ┃ 分享群：")
 print("// ┃   ┃ 780261548")
 print("// ┃   ┗━━━┓")
 print("// ┃       ┣┓")
 print("// ┃       ┏┛")
 print("// ┗┓┓┏━┳┓┏┛")
 print("// ┃┫┫ ┃┫┫")
 print("// ┗┻┛ ┗┻┛")
if __name__=='__main__':
 print_ascii_art()
 ck=os.getenv("ddjz")
 if ck:
  if "&"in ck:
   ck=ck.split("&")
  else:
   ck=ck.split(" ")
  for i in ck:
   user,api_auth_code,api_auth_uid=i.split("#")
   print("当前账号{}".format(user))
   print("="*10)
   id=get_id(api_auth_code,api_auth_uid)
   id_list=json.loads(id)
   random_choice=random.choice(id_list[1:])
   if id_list:
    liulan(api_auth_code,api_auth_uid,random_choice)
    print("随机延迟中")
    time.sleep(random.uniform(8,15))
    tmp=browse(api_auth_code,api_auth_uid,random_choice)
    if tmp:
     liulan(api_auth_code,api_auth_uid,tmp)
     print("随机延迟中")
     time.sleep(random.uniform(8,15))
     browse(api_auth_code,api_auth_uid,tmp,t=1)
    else:
     liulan(api_auth_code,api_auth_uid,id_list[0])
     print("w随机延迟中")
     time.sleep(random.uniform(8,15))
     browse(api_auth_code,api_auth_uid,id_list[0],t=1)
   print("="*10)
 else:
  print("变量不存在")
