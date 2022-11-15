from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from twilio.rest import Client
import keys2

##############FOR MACS THAT HAVE ERRORS LOOK HERE################
## https://timonweb.com/tutorials/fixing-certificate_verify_failed-error-when-trying-requests_html-out-on-mac/

############## ALTERNATIVELY IF PASSWORD IS AN ISSUE FOR MAC USERS ########################
##  > cd "/Applications/Python 3.6/"
##  > sudo "./Install Certificates.command"


#url = 'https://www.tradingview.com/markets/stocks-usa/market-movers-gainers/'
url = 'https://crypto.com/price'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers= headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')


tr = soup.findAll('tr')


counter = 0

for row in tr[1:6]:
    td = row.findAll("td")
    namecells = soup.findAll("p", attrs={"class":"chakra-text css-rkws3"})
    symbolcells = soup.findAll("span", attrs={"class":"chakra-text css-1jj7b1a"})
    pricecells = soup.findAll("div", attrs={"class":"css-b1ilzc"})
    name = namecells[counter].text
    symbol= symbolcells[counter].text
    price = float(pricecells[counter].text.replace(",","").replace("$",""))
    change=float(td[4].text.replace("%",""))
    corresponding_price = ((100-(change))/100) * (price)
    
    counter+=1

#print
    print(f'Name: {name}')
    print(f'Symbol: {symbol}')
    print(f"Price: ${price:,.2f}")
    print(f"% change on webpage: {change}%")
    print(f'Corresponding Price: ${corresponding_price:,.2f}')
    print()
    print()
    input()

#TextMessage
    client = Client(keys2.accountSID, keys2.authToken)

    TwilioNumber = '+16293488232'
    myCellPhone = '+19152449026'

    BTC = 'Bitcoin price has fallen below $40,000.'
    ETH = 'Ethereum price has fallen below $3,000.'


    if symbol == 'BTC' and float(price) < 40000:
        textmsg = client.messages.create(to=myCellPhone, from_= TwilioNumber, body =BTC)
    if symbol == 'ETH' and float(price) < 3000:
        textmsg = client.messages.create(to=myCellPhone, from_= TwilioNumber, body =ETH)

    print(textmsg.status)





    

    



