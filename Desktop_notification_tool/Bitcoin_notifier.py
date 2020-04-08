# Import our modules
from plyer import notification
import time
from bs4 import BeautifulSoup
import requests

# We fetch the current price of Bitcoin
url = 'https://coinmarketcap.com/currencies/bitcoin/'

headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/80.0.3987.149 Safari/537.36'
}
page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

price = soup.find('span', {"class": "cmc-details-panel-price__price"}).get_text()
price2 = str(price)

change_percentage = soup.find('span', {"class": "cmc-details-panel-price__price-change"}).get_text()
percent = str(change_percentage)

msg = f'Bitcoin is currently at {price2} increased/decreased by{percent}'

# Send desktop notification
notification.notify(
    title='TODAY\'S BITCOIN PRICE',
    message=msg,
    app_icon=r'C:\Users\antriksh.chourasia\Bitcoin_icon.ico',
    timeout=15
)
