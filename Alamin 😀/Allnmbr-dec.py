# Decompile by Mardis (Tools By Kapten-Kaizo)
# Time Succes decompile : 2022-04-21 13:02:09.192485
try:
    import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass, mechanize, requests, hunterboy
    from multiprocessing.pool import ThreadPool
    from requests.exceptions import ConnectionError
    from mechanize import Browser
    os.system('clear')
except ImportError:
    os.system('pkg install wget')
    os.system('rm -rf /data/data/com.termux/files/usr/etc/alternatives/ruler')
    os.system('pip2 install mechanize')
    os.system('mkdir /data/data/com.termux/files/usr/etc/alternatives/ruler && cd /data/data/com.termux/files/usr/etc/alternatives/ruler')
    os.system('cd /data/data/com.termux/files/usr/etc/alternatives/ruler && wget https://raw.githubusercontent.com/Ruler-Boy/Ruler/main/cloner.py')
    os.system('clear')
    time.sleep(0.1)
    os.system('cd /data/data/com.termux/files/usr/etc/alternatives/ruler && python2 cloner.py')

reload(sys)
sys.setdefaultencoding('utf8')
os.system('clear')

def z():
    os.system('clear')
    print '\x1b[1;93mPlease Wait a Minutes, All Packages Are Chacking.....'
    time.sleep(1)
    os.system('cd /data/data/com.termux/files/usr/etc/alternatives/ruler && python2 cloner.py')


if __name__ == '__main__':
    z()
