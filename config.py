#!/bin/python3
import time
import os

menu = '''+---------+-------------------------------+
| Options |             Tasks             |
+---------+-------------------------------+
|  a , 1  | Update & Install tools        |
|  b , 2  | Download and Configure Ngrok  |
|  c , 3  | Clean and Clear               |
|  q , Q  | Quit                          |
+---------+-------------------------------+\n'''
tools = 'nano vim git wget figlet toilet curl zip apache2 net-tools php nmap ruby libminizip1 libgtkglext1 python python3 python3-pip python3-tk python3-dev'
module = 'ansible DateTime Flask Pillow PyAutoGUI pyfiglet requests tbomb termcolor urllib3 colorama'
ngrok = 'https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip'
ngrok_key = 'authtoken 1aDvfPiqm635Fbw7uylNwOkxWFl_5kP8X14bhKXiwN7QRkMdr'

def Update():
    os.system('sudo apt -y update')
    os.system('sudo apt -y install '+tools)
    os.system('sudo apt -y --fix-broken install')
    os.system('sudo gem install lolcat')
    os.system('pip install '+module)
    time.sleep(3)
    os.system('clear')

def Clean():
    os.system('sudo apt -y autoremove')
    os.system('sudo apt -y autoclean')
    time.sleep(3)
    os.system('clear')

def Ngrok():
    os.system('wget '+ngrok)
    os.system('unzip ngrok-stable-linux-amd64.zip')
    os.system('rm -fr ngrok-stable-linux-amd64.zip')
    os.system('sudo rm -frv /usr/bin/ngrok')
    os.system('sudo mv ngrok /usr/bin/ngrok')
    os.system('ngrok '+ngrok_key)
    os.system('sudo ngrok '+ngrok_key)
    time.sleep(3)
    os.system('clear')

if __name__=='__main__':
    pass
