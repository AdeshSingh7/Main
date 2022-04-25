#!/bin/python3
import config

try:
    config.os.system('clear')
    while True:
        print('\033[1;33m'+config.menu)
        user_input = input('\033[1;34mChoose options : ')
        if user_input in ('a','A','1'):
            config.Update()
        elif user_input in ('b','B','2'):
            config.Ngrok()
        elif user_input in ('c','C','3'):
            config.Wine()
        elif user_input in ('d','D','4'):
            config.Anydesk()
        elif user_input in ('e','E','5'):
            config.Whatsapp()
        elif user_input in ('f','F','6'):
            config.VisualStudio()
        elif user_input in ('g','G','7'):
            config.Slack()
        elif user_input in ('h','H','8'):
            config.Clean()
        elif user_input in ('q','Q'):
            exit()
        else:
            config.os.system('clear')
            print('\033[1;31m\n[Warning] Wrong input try again\n')
        pass
except KeyboardInterrupt:
    pass
finally:
    config.os.system('clear')
    print('\033[1;32mThankYou for using this tool.\n\n\033[1;31mVisit : \033[1;33mhttps://github.com/GreyHat9\n')
