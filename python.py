import os, sys
import time
import re

re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"

def wait():
    print("Lütfen Bekleyiniz...")
    time.sleep(0.5)
    print("İşlem Tamamlandı!")

def banner():
    os.system('clear')
    print(f"""

{re}.d88888b  {cy}         dP                   {re} .88888.
{re}88.    "' {cy}         88                   {re}d8'   `88
{re}`Y88888b. {cy}.d8888b. 88 .d8888b. dP.  .dP {re}88
{re}      `8b {cy}88ooood8 88 88'  `88  `8bd8'  {re}88   YP88
{re}d8'   .8P {cy}88.  ... 88 88.  .88  .d88b.  {re}Y8.   .88
{re} Y88888P  {cy}`88888P' dP `88888P8 dP'  `dP {re} `88888'

                            t.me/selaxg

    """)
banner()
time.sleep(1)
print("Veritabanından eşleşme bulmak için doldrunuz")
isim = str(input(gr+"$"+cy+"İsim giriniz : "+gr))

if isim =="admin":
    o = open("database.txt", "r")
    for x in o:
        print(x)

else:
    wait()
    text = open("database.txt", "r")
    response = re.find_all(isim)
    if response == True:
        print("İşlem Tamamlandı!")
    else:
        print("Daha Sonra Tekrar Deneyiniz!")
