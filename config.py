#!/bin/python3
import time
import os

menu = '''+---------+-------------------------------+
| Options |             Tasks             |
+---------+-------------------------------+
|  a , 1  | Update & Upgrade              |
|  b , 2  | Download and Configure Tools  |
|  c , 3  | Download and Configure Ngrok  |
|  d , 4  | Clean and Clear               |
|  q , Q  | Quit                          |
+---------+-------------------------------+\n'''
tools = 'nano vim git wget figlet toilet curl zip php nmap ruby python python3'
module = 'DateTime Pillow pyfiglet requests tbomb termcolor urllib3 colorama'
ngrok = ''
#ngrok_key = 'authtoken 1aDvfPiqm635Fbw7uylNwOkxWFl_5kP8X14bhKXiwN7QRkMdr'

def Update():
    os.system('apt -y update')
    os.system('apt -y upgrade')
    time.sleep(3)
    os.system('clear')

def Tools():
    os.system('apt -y install '+tools)
    os.system('apt -y --fix-broken install')
    os.system('gem install lolcat')
    os.system('pip install '+module)
    time.sleep(3)
    os.system('clear')

def Ngrok():
    os.system('wget '+ngrok)
    os.system('unzip ngrok-stable-linux-amd64.zip')
    os.system('rm -fr ngrok-stable-linux-amd64.zip')
    os.system('mv ngrok /usr/bin/')
    os.system('ngrok '+ngrok_key)
    os.system('ngrok '+ngrok_key)
    time.sleep(3)
    os.system('clear')

def Clean():
    os.system('apt -y autoremove')
    os.system('apt -y autoclean')
    time.sleep(3)
    os.system('clear')

if __name__=='__main__':
    pass
