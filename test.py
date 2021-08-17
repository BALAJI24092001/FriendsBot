import requests
url = 'https://api.telegram.org/bot1966604778:AAFaH4Y3jmupxYGt324_1Uf6xRfy4ZseUvo/'


def send_message(url, chat_id, message):
    if message == 'hi':
        reply = ' hello, how are you..?'
        send = requests.post(url+'sendMessage?chat_id=' +
                             str(chat_id)+'&text='+reply)
        print(send)
        # return send
    elif message == '/start':
        reply = '''
        hello this is a telegram bot to download friends sitcom enter the required video in this format S**E** (ex: S02E21)
        '''
        send = requests.post(url+'sendMessage?chat_id=' +
                             str(chat_id)+'&text='+reply)
        print(send)
        # return send
    elif message == 's05e20':
        requests.post(url + 'sendMessage?chat_id='+str(chat_id) +
                      '&text='+'https://t.me/friends25yrs/151')
    elif message == 'friends':
        requests.post(url + 'sendMessage?chat_id='+str(chat_id) +
                      '&text= https://mega.nz/file/4VswUaIB#wGvdagunBcgb6cVyU4VkSakP23kq4kFBP_5CCnu21Gs')
        requests.post(url + 'sendMessage?chat_id='+str(chat_id)+'&text=' +
                      'Decryption key = wGvdagunBcgb6cVyU4VkSakP23kq4kFBP_5CCnu21Gs')


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
