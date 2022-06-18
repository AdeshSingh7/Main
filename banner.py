#!/bin/python3
from termcolor import colored
from random import choice
from os import system, popen

colors=['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m']
banner='''---------------------------------------------------------------------------------
 █████╗ ██████╗ ███████╗███████╗██╗  ██╗   ███████╗██╗███╗   ██╗ ██████╗ ██╗  ██╗
██╔══██╗██╔══██╗██╔════╝██╔════╝██║  ██║   ██╔════╝██║████╗  ██║██╔════╝ ██║  ██║
███████║██║  ██║█████╗  ███████╗███████║   ███████╗██║██╔██╗ ██║██║  ███╗███████║
██╔══██║██║  ██║██╔══╝  ╚════██║██╔══██║   ╚════██║██║██║╚██╗██║██║   ██║██╔══██║
██║  ██║██████╔╝███████╗███████║██║  ██║   ███████║██║██║ ╚████║╚██████╔╝██║  ██║
╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝   ╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝
-------------------------- https://github.com/GreyHat9 --------------------------'''
print(choice(colors))
system('clear')
print(banner)
uptime=popen('uptime -p').read().strip()
uptime1=popen('uptime -s').read().strip()
ip=popen('hostname -I').read()
print(choice(colors))
print(f'Uptime: {uptime} (Since: {uptime1})')
print(choice(colors))
print(f'IP Address: {ip}')
