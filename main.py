import requests

from bs4 import BeautifulSoup

import lxml

import smtplib

import os
from dotenv import load_dotenv

load_dotenv()


URL="https://www.flipkart.com/apple-2020-macbook-air-m1-8-gb-ssd-256-gb-ssd-mac-os-big-sur-mgn63hn-a/p/itm3c872f9e67bc6?pid=COMFXEKMGNHZYFH9&lid=LSTCOMFXEKMGNHZYFH9P56X45&marketplace=FLIPKART&q=macbook+air+m1&store=6bo%2Fb5g&spotlightTagId=BestsellerId_6bo%2Fb5g&srno=s_1_3&otracker=AS_QueryStore_OrganicAutoSuggest_2_4_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_4_na_na_na&fm=search-autosuggest&iid=4640a7b7-aa49-4e8f-8703-d565d3938fef.COMFXEKMGNHZYFH9.SEARCH&ppt=sp&ppn=sp&ssid=dopy9o1pa80000001719382974695&qH=be9862f704979d6e"

# PRICE_TO_BUY=60000

PRICE_TO_BUY="68990.0"

EMAIL_PROVIDER_SMTP_ADDRESS=os.environ.get("EMAIL_PROVIDER_SMTP_ADDRESS")

MY_EMAIL=os.environ.get("MY_EMAIL")

MY_EMAIL_PASSWORD=os.environ.get("MY_EMAIL_PASSWORD")


# TO_EMAIL=["lingesh.91918@gmail.com","lingalingesh91918@gmail.com",""]
TO_EMAIL="lingesh.91918@gmail.com"


header={

    "Accept-Language":"en-US,en;q=0.9",

    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"

}


response=requests.get(url=URL,headers=header)

# print(response.text)

response_text=response.text


soup=BeautifulSoup(response_text,"lxml")

print(soup.title.getText())

string_price=soup.find(name="div",class_="Nx9bqj CxhGGd").getText().split("₹")[1]

product_price_=string_price.split(',')[0]+string_price.split(',')[1]

product_price=float(product_price_)
print(product_price)



if float(product_price)<=float(PRICE_TO_BUY):

    print("LOW ")

    # for i in TO_EMAIL:

    with smtplib.SMTP("smtp.gmail.com") as connection:

        msg=f"Subject:LOW PRICE ALTER!\n\nApple 2020 Macbook Air Apple M1(8 GB/SSD/256 GB SSD/Mac OS Big Sur)(13.3 inch, Space Grey, 1.29 kg) is selling at just ₹{product_price}\n{URL}"
        connection.starttls()
        connection.login(user=MY_EMAIL,password=MY_EMAIL_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,to_addrs=TO_EMAIL,msg=msg.encode("utf-8"))



else:

    print("HIGH")

