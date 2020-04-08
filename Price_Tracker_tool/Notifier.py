from bs4 import BeautifulSoup
import requests
import smtplib


def check_price():
    url = 'https://www.amazon.in/Surf-Excel-Matic-Detergent-Powder/dp/B00TS88UZW/ref=sr_1_3?dchild=1&pf_rd_p=8c257e3a' \
          '-4eba-4372-b88b-a5dbcdc8773f&pf_rd_r=21KXVJ8HYYV06JK8VRAA&qid=1585849820&refinements=p_85%3A10440599031' \
          '&rps=1&s=hpc&sr=1-3&srs=21246718031'

    headers = {
        'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                     'Chrome/80.0.3987.149 Safari/537.36'
    }

    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id='productTitle').get_text()
    price = soup.find(id='priceblock_ourprice').get_text()
    price2 = float(price[2:5])

    if price2 > 379.0 or price2 < 379.0:
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('antrikshhii17@gmail.com', 'ksqrbrjsgmowseah')

    subject = 'The price of the commodity changed!'
    body = 'Check out the product by clicking on this link below- ' \
           '' \
           'https://www.amazon.in/Surf-Excel-Matic-Detergent-Powder/dp/B00TS88UZW/ref=sr_1_3?dchild=1&pf_rd_p=8c257e3a' \
           '-4eba-4372-b88b-a5dbcdc8773f&pf_rd_r=21KXVJ8HYYV06JK8VRAA&qid=1585849820&refinements=p_85%3A10440599031' \
           '&rps=1&s=hpc&sr=1-3&srs=21246718031'

    msg = f'subject: {subject}\n\n{body}'

    server.sendmail('antrikshhii17@gmail.com', 'antrikshhii17@gmail.com', msg)
    print('An email has been sent to your mailbox')


check_price()
