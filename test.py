import requests
url = 'https://api.telegram.org/bot1966604778:AAFaH4Y3jmupxYGt324_1Uf6xRfy4ZseUvo/'

def send_message(url, chat_id, message):
    if message == 'hi':
        reply = ' hello, how are you..?'
        send = requests.post( url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply )
        print(send)
        # return send
    elif message == '/start':
        reply = '''
        Nikal lovde, pehle fursat me nikal, koyi jarurat nayi hindustan ko teri, samjah?
        '''
        send = requests.post( url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply )
        print(send)
        # return send


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
                send_message(url, c_id, message)
            except:
                message = None