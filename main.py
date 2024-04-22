import requests
from bs4 import BeautifulSoup
import smtplib


url = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
BUY_PRICE = 100


headers = {
    "User-Agent": USER_AGENT,
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url=url, verify=False, headers=headers)
amazon_web = response.text

soup = BeautifulSoup(amazon_web, "html.parser")
price_tag = soup.find(name="span", class_="a-offscreen")
title = soup.find(id="productTitle").get_text().strip()
price_text = price_tag.getText()[1:]
price = float(price_text)

if price < BUY_PRICE:
    message = f"{title} is now at price ${price}"

    with smtplib.SMTP("mail address", port=587) as connection:
        connection.starttls()
        result = connection.login("mail", "password")
        connection.sendmail(
            from_addr="your mail",
            to_addrs="your mail",
            msg=f"Subject=Amazon Price Alert\n\n{message}\n{url}".encode("utf-8")
        )
