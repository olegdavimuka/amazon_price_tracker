from bs4 import BeautifulSoup
import requests
import smtplib
import os

link = "https://rozetka.com.ua/apple_macbook_air_13_m1_256gb_2020_space_gray/p245161909/"
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

# Scrapping product Price
response = requests.get(link)
soup = BeautifulSoup(response.text, "html.parser")
price_tag_text = soup.find("p", class_="product-prices__big").getText()
price = int(f"{price_tag_text[:-1].split()[0]}{price_tag_text[:-1].split()[1]}")

if price < 40000:
    title_tag_text = soup.find("h1", class_="product__title").getText()
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Product price is {price}!\n\nBuy it:\n{link}")


