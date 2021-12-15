#https://github.com/Whoneon/Telegram_Library
#feel free to use, improve or edit my code! 
# - Whoneon

import time
import sys
import datetime
import telegram_send
import pandas as pd 
import telepot
from telegram import ParseMode

df = pd.read_csv('books.csv') #Apro il database che contiene i miei libri
print(df.head()) #Come prova stampo le prime 5 righe

def on_chat_message(msg):
  content_type, chat_type, chat_id = telepot.glance(msg)
  if content_type == 'text': #Se un utente scrive una stringa di testo, la conservo
    name = msg["from"]["first_name"]
    txt = msg['text']
    res = df[df.apply(lambda r: r.str.contains(txt, case=False).any(), axis=1)] #Cerco nel database il libro che contiene nel titolo o nel nome dell'autore la stringa desiderata	
    print(res) #Nel terminale restituisco la query intera
    table = res.to_string(columns = ['Title', 'Author'], header = False) #Nel mio caso a me importa elencare solo queste due colonne
    telegram_send.send(messages=[table]) #Restituisco le prime due colonne all'utente

bot = telepot.Bot('XXXXXXXXXX:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX') #Token del Bot
bot.message_loop(on_chat_message)

print('Attendo input ...')


while 1:
    time.sleep(10)
