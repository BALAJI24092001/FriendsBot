from matplotlib.pyplot import text
import requests
from operator import imod
from telegram import message


token = "1966604778:AAFaH4Y3jmupxYGt324_1Uf6xRfy4ZseUvo"
chat_id = 775369387
msg = str()
# chat_url = "https://api.telegram.org/bot"+token+'/sendMessage?chat_id='+chat_id+"&text="+msg


update_url = 'https://api.telegram.org/bot1966604778:AAFaH4Y3jmupxYGt324_1Uf6xRfy4ZseUvo/getupdates'
chat_url = 'https://api.telegram.org/bot1966604778:AAFaH4Y3jmupxYGt324_1Uf6xRfy4ZseUvo/sendMessage?chat_id=775369387&text=welcome'
url = 'https://api.telegram.org/bot1966604778:AAFaH4Y3jmupxYGt324_1Uf6xRfy4ZseUvo/'


def get_updates(url):
    resp = requests.get(url+'getUpdates?').json()
    return resp["result"]


data = get_updates(url)


def get_message(data):
    # message = data['message']
    pass


print(data[0]['message']['text'])
