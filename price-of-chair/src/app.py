import requests
from bs4 import BeautifulSoup
request = requests.get("https://www.johnlewis.com/house-by-john-lewis-whistler-dining-chair/white/p4843125")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("p", {"class": "price price--large"})
string_price = element.text.strip()

price_without_symbol = string_price[1:]

price = float(price_without_symbol)

if price < 200:
    print("You should buy the chair")
    print("The current price is {}".format(string_price))
else:
    print("Do not buy, it's too expensive")