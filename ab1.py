import asyncio
import logging
import re
import time
import os
import sys
import random

import requests
import json
from urllib.request import urlopen
import pprint
import simplejson

logging.basicConfig(level=logging.ERROR)

from telethon import TelegramClient, events
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest
from datetime import datetime
from colorama import Fore, init as color_ama
color_ama(autoreset=True)



try:
   import colorama
   from colorama import Fore, Back, Style
   colorama.init(autoreset=True)
   hijau = Style.RESET_ALL+Style.BRIGHT+Fore.GREEN
   res = Style.RESET_ALL
   abu2 = Style.DIM+Fore.WHITE
   putih = Style.RESET_ALL+Style.BRIGHT+Fore.WHITE
   ungu2 = Style.NORMAL+Fore.MAGENTA
   ungu = Style.RESET_ALL+Style.BRIGHT+Fore.MAGENTA
   hijau2 = Style.NORMAL+Fore.GREEN
   yellow2 = Style.NORMAL+Fore.YELLOW
   yellow = Style.RESET_ALL+Style.BRIGHT+Fore.YELLOW
   red2 = Style.NORMAL+Fore.RED
   red = Style.RESET_ALL+Style.BRIGHT+Fore.RED
   cyan = Style.RESET_ALL+Style.BRIGHT+Fore.CYAN
   cyan2 = Style.NORMAL+Fore.CYAN

except:
   print ("Please Install Modul Colorama!!\n\n\n")
   sys.exit()

try:
   import requests
   from bs4 import BeautifulSoup
except:
   print ("Please Install Modul Requests & BS4\n\n\n")
   sys.exit()

os.system('cls' if os.name=='nt' else 'clear')

# Get your own values from my.telegram.org
api_id = 717425
api_hash = '322526d2c3350b1d3530de327cf08c07'

data = requests.get("http://toolsmix-id.com/bot/data.json").json()


cname = '@freelite_coin_bot'
crot = "https://t.me/freelite_coin_bot"

def print_msg_time(message):
  print('[' + Fore.CYAN + f'{datetime.now().strftime("%H:%M:%S")}' + Fore.RESET + f'] {message}')

async def main():
   
  rstat = data['status']
  lversi = data['last_versi']
  nversi = data['new_versi']

  if lversi < nversi:
     print("Silakan download versi terbaru di "+data['link'])
     sys.exit()
  
  #print(rstat)
  if rstat == "Aktif":
    print ("""
banner =\033[1;36m                                                                      
        88              88          88  88                       
.d8888b.88  .dP .d8888b.88.d8888b.d8888P88d888b..d8888b.88d888b. 
Y8ooooo.88888"  88ooood88888ooood8  88  88'  `8888'  `8888'  `88 
      8888  `8b.88.  ...8888.  ...  88  88    8888.  .8888    88 
`88888P'dP   `YP`88888P'dP`88888P'  dP  dP    dP`88888P'dP    dP                                                                                                                                   
\033[1;32m≠========================#BY~@XTeMixX#=========================≠
   \033[1;32m╔═════════════════════════════════════════════════════════╗
   \033[1;32m║ Author            : XTeMixX                             ║
   \033[1;32m║ Special Thanks    : Dice Discussion                     ║
   \033[1;32m║ Doge Donate       : DAPUfc13yGnzV22nBKdngxrreraExNTNkh  ║
   \033[1;32m║ Status Server     : Aktif                               ║
   \033[1;32m╚═════════════════════════════════════════════════════════╝
"""+Style.RESET_ALL+Style.BRIGHT+Fore.WHITE+"""
""")
     
  # Check if phone number is not specified
  if len(sys.argv) < 2:
    print('Usage: python start.py phone_number')
    print('-> Input number in international format (example: +94xxxxxxxxxx)\n')
    e = input('Press any key to exit...')
    exit(1)
    
  phone_number = sys.argv[1]
  choice = '💥 litecoin Bonus'
  
  if not os.path.exists("session"):
    os.mkdir("session")
   
    # Connect to client
  client = TelegramClient('session/' + phone_number, api_id, api_hash)
  await client.start(phone_number)
  me = await client.get_me()
  
  # Free_LTC_Robot
  print_msg_time(Fore.GREEN + f'Bot Name: @freelite_coin_bot '  + Fore.RESET)
  print_msg_time(Fore.GREEN + f'Welcome : {me.first_name} - {me.last_name} '  + Fore.RESET)
  print(f'\n')
  print_msg_time(Fore.YELLOW + 'Bot jalan cuk' + '\n' + Fore.RESET)
  
  # Start command /balance

  i = 1
  while(True):
    await client.send_message(crot, choice)
    print_msg_time(Fore.GREEN + ' 0.0001132 Litoshi' + Fore.RESET)
    time.sleep(60) #waktu klik hitungan dalam detik
    i = 1
    
  
    # Message the bot
  @client.on(events.NewMessage(chats=cname, incoming=True))
  async def earned_amount(event):
    message = event.raw_text
    if 'Balance' in message:  
      print_msg_time(Fore.GREEN + event.raw_text + '\n' + Fore.RESET)

      
  await client.run_until_disconnected()
  
asyncio.get_event_loop().run_until_complete(main())

