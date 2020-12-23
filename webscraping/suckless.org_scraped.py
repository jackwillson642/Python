from bs4 import BeautifulSoup as bs
import requests

headers = {
    "User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) QtWebEngine/5.12.8 Chrome/69.0.3497.128 Safari/537.36'}

URL = 'https://www.amazon.in/NIBOSI-Chronograph-Waterproof-Wristwatches-Silver-Gold/dp/B08263FJWX/ref=sr_1_7_mod_primary_lightning_deal?crid=1099IIDDYFE90&dchild=1&keywords=chronograph+watch+for+men&qid=1605105514&refinements=p_n_feature_sixteen_browse-bin%3A5756156031&rnid=5756152031&s=watches&sbo=Tc8eqSFhUl4VwMzbE4fw%2Fw%3D%3D&smid=A2JUEUK1KD8AZ9&sprefix=chronog%2Caps%2C287&sr=1-7'

source = requests.get(URL, headers=headers)

soup = bs(source.content, 'html.parser')

name = soup.find(id='productTitle').get_text()

price = soup.find(id='priceblock_dealprice').get_text()
converted_price = float(price[2:3]+price[4:7])

print(name.strip()+'\n')
print(price)
print(converted_price)
