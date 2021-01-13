#
# The best things you can do
# Don't play with GhOSt
#
import requests, uuid
from time import sleep
from threading import Thread
import os, signal, socket
qq = requests.session()
print('\x1b[38;5;31m             ~ Socket version  \x1b[0m')
print('\x1b[38;5;31m             ~ ProG by @0.xa  \x1b[0m')
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
print('ip address = ' + ip)
g = requests.get('https://pastebin.com/raw/B4Yu82i7')
if ip in g.text:
    print('Active')
else:
    print('unactive')
    exit()
uid = str(uuid.uuid4())
count = 0
thrdrun = 0
save = True
mode = ''
email = ''
cok = ''
nump = ''
ful_name = ''
userACC = ''
passACC = ''
ATT = False

def tel():
    global thrdd
    requests.post(f'https://api.telegram.org/bot1302705094:AAFd-YpMRLBksr2_YdRiBfFUH-4P8xmoHuU/sendMessage?chat_id=852468783"+ "&text=~ Swapped successfully @{thrdd} 1cs')


headers1 = {'accept':'*/*', 
 'accept-encoding':'gzip, deflate, br', 
 'accept-language':'en-US,en;q=0.9', 
 'content-length':'267', 
 'content-type':'application/x-www-form-urlencoded', 
 'cookie':'ig_did=0897491F-B736-4E7E-A657-37438D0967B8; csrftoken=xvAQoMiz2eaU4RrcmRp2hqinDVMfgkpe; rur=FTW; mid=XxTPfgALAAGHGReE-x_i1ISMG4Xr', 
 'origin':'https://www.instagram.com', 
 'referer':'https://www.instagram.com/', 
 'sec-fetch-dest':'empty', 
 'sec-fetch-mode':'cors', 
 'sec-fetch-site':'same-origin', 
 'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Mobile Safari/537.36 Edg/86.0.622.63', 
 'x-csrftoken':'xvAQoMiz2eaU4RrcmRp2hqinDVMfgkpe', 
 'x-ig-app-id':'1217981644879628', 
 'x-ig-www-claim':'0', 
 'x-instagram-ajax':'180c154d218a', 
 'x-requested-with':'XMLHttpRequest'}
hd_login = {'X-IG-Connection-Type':'WIFI',  'X-IG-Capabilities':'3brTBw==', 
 'User-Agent':'Instagram 100.0.0.17.129 Android (28/9; 320dpi; 720x1422; HUAWEI; MRD-LX1F; HWMRD-M1; mt6761; ar_EG; 16147866)', 
 'Accept-Language':'en-US', 
 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
 'Accept-Encoding':'gzip, deflate', 
 'Host':'i.instagram.com', 
 'Connection':'keep-alive', 
 'Accept':'*/*'}

def get_info():
    global cok
    global email
    global ful_name
    global hd_login
    global nump
    try:
        txt = requests.get('https://i.instagram.com/api/v1/accounts/current_user/?edit=true', headers=hd_login, cookies=cok).json()
        email = txt['user']['email']
        nump = txt['user']['phone_number']
        ful_name = txt['user']['full_name']
    except:
        pass


def login_api(username, password):
    global cok
    login_url = 'https://www.instagram.com/accounts/login/ajax/'
    data_login = {'username':username,  'enc_password':'#PWD_INSTAGRAM_BROWSER:0:&:' + password}
    loginc = requests.post(login_url, data=data_login, headers=headers1)
    login1 = loginc.text
    if '"authenticated": true' in login1:
        cok = loginc.cookies
        return True
    print(login1)


def cheakspamblock():
    global do
    global userACC
    edit_url = 'https://i.instagram.com/api/v1/accounts/set_username/'
    d2 = {'_uuid':uid,  '_uid':uid,  '_csrftoken':'missing', 
     'first_name':ful_name, 
     'is_private':'false', 
     'phone_number':nump, 
     'biography':'Try', 
     'username':userACC, 
     'gender':'3', 
     'email':email, 
     'external_url':''}
    do = requests.post(edit_url, data=d2, headers=hd_login, cookies=cok)
    if do.status_code == 200:
        return True
    print('Acc Block ,spam')
    print(do.text)
    os.kill(os.getpid(), signal.SIGKILL)


def edit():
    global ATT
    global count
    global d2

    while True:
        got = ''
        edit_url = 'https://i.instagram.com/api/v1/accounts/set_username/'
        while True:
            if ATT:
                go = requests.post(edit_url, data=d2, headers=hd_login, cookies=cok)
                got = go.text
                if f'"username": "{thrdd}"' in got:
                    ATT = False
                    sleep(0.1)
                    print(f"\x1b[0;36mSwapped successfully : @{thrdd}")
                    tel()
                    os.kill(os.getpid(), signal.SIGKILL)
                else:
                    if '{"message": {"errors": ["This username isn\'t available' in got:
                        count += 1
                        print(f"{count} - {got}")
                if '"message": "Please wait a few minutes before you try again."' in got:
                    print('Blocked')
                    os.kill(os.getpid(), signal.SIGKILL)


userACC = input('Username: ')
passACC = input('Password: ')
print('')

def go():
    global ATT
    global thrd
    global d2
    global headers1
    threads = []
    for _ in range(int(thrd)):
        t = Thread(target=edit)
        t.start()
        threads.append(t)
    else:
        input('Ready?')
        ATT = True


if login_api(userACC, passACC):
    get_info()
    if cheakspamblock():
        print('Login Success')
        print('')
    else:
        print('Blocked')
        print(do.text)
        exit(0)
    thrdd = input('Target: ')
    d2 = {'_uuid':uid,  '_uid':uid,  '_csrftoken':'missing', 
     'first_name':ful_name, 
     'is_private':'false', 
     'phone_number':nump, 
     'biography':'', 
     'username':thrdd, 
     'gender':'3', 
     'email':email, 
     'external_url':''}
    cok = login.cookies
    txt = qq.get('https://i.instagram.com/api/v1/accounts/current_user/?edit=true', headers=hd_login).json()
    email = txt['user']['email']
    nump = txt['user']['phone_number']
    ful_name = txt['user']['full_name']
    d2 = {'_uuid':uid,  '_uid':uid,  '_csrftoken':'missing', 
         'first_name':ful_name, 
         'is_private':'false', 
         'phone_number':nump,
         'biography':'', 
         'username':thrdd, 
         'gender':'3', 
         'email':email, 
         'external_url':''}
    thrd = input('Thread: ')
    go()
