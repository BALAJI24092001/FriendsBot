import requests


# token = "1966604778:AAFaH4Y3jmupxYGt324_1Uf6xRfy4ZseUvo"
# chat_id = 775369387
# chat_url = "https://api.telegram.org/bot"+token+'/sendMessage?chat_id='+chat_id+"&text="+msg


# update_url = 'https://api.telegram.org/bot1966604778:AAFaH4Y3jmupxYGt324_1Uf6xRfy4ZseUvo/getupdates'
# chat_url = 'https://api.telegram.org/bot1966604778:AAFaH4Y3jmupxYGt324_1Uf6xRfy4ZseUvo/sendMessage?chat_id=775369387&text=welcome'
url = 'https://api.telegram.org/bot1966604778:AAFaH4Y3jmupxYGt324_1Uf6xRfy4ZseUvo/'


# def get_updates(url):
#     response = requests.get(url+'getUpdates').json()
#     return response['result']


# def get_message(data):
#     # message = data['message']
#     pass


def send_message(url, chat_id, message):
    if message == 'hi':
        reply = ' hello, how are you..?'
        send = requests.post( url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply )
        return send


update_id = None


def get_updates(url, offset):
    url = url+'getUpdates?timeout=100'
    if offset:
        url = url + '&offset={}'.format(offset+1)
    r = requests.get(url).json()
    return r


while True:
    print(".....")
    updates = get_updates(url, offset=update_id)
    print(updates)
    updates = updates['result']
    if updates:
        for item in updates:
            update_id = item['update_id']
            try:
                message = item['message']['text'].lower()
                c_id = item['message']['from']['id']
                send_message(url, message, c_id)
            except:
                message = None

# print(data[0]['message']['text'])
