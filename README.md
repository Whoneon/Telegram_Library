# Telegram Library
A bot to manage and visualize a list of book

## WHAT DOES IT DO?
This is a simple program that uses Telegram Bot API to receive text messages from one or more users and search in a list of book, to visualize if a certain book or author is present in my library

## REQUIREMENTS:
- Telegram with @BotFather (just start a conversation with it, generate a new bot and write down the token which is in the form of `XXXXXXXXXX:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX`)
- Python 3 with pip
- Git
- Pandas (to manage .csv files)
- Telepot
- A .csv file containing a list of books (Title, Author, etc...)
```
sudo apt install python3.8 python3-pip git python3-pandas
pip3 install pandas telepot
```

Once you have met the requirements above, just type the following:
```
git clone https://github.com/Whoneon/Telegram_Library.git
cd Telegram_Library/
nano Library.py
```
Now you have to change the string `XXXXXXXXXX:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX` and paste there your token (generated above), then save with `CTRL + O`
## RUN IT!
Just type
```
python3 Library.py
```
Now leave the command window running: this will keep the bot on listen mode. Try to type something in the bot chat (during the set-up phase, it will ask you to choose a @nickname, just start a conversation with that)

## ADJUSTMENT(S)
If you open the code, you will see some useful comments. If you wish to change the language or the speed of voice, just follow the instructions!
