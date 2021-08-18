import requests
url = 'https://api.telegram.org/bot1974553065:AAGm9ZRmLymL9bWx-inSxEIKLTigQHGgtT4/'


def send_message(url, chat_id, message):
    if message == 'hi':
        reply = ' hello, how are you..?'
        send = requests.post(url+'sendMessage?chat_id=' +
                             str(chat_id)+'&text='+reply)
        print(send)
        # return send
    elif message == '/start':
        reply = '''
        Hey there,
        I know you started me(the bot) probably to download
        the F.R.I.E.N.D.S series, but before you carray on
        with downloading, let me just give you an overview
        of what you can do with me.

        To download use the command `S01E01` to get first
        episode of season 1.

        To download a full season use `s02` (season 2).

        To know number of episodes in each season use
        `episodes` command.

        To get details of the main charecters use their
        first name as the command. eg.. (chandler)

        For any suggestions or complaints to report contact
        @dbalajivaraprasad
        @CHAKRADHAR_GBG
        @abhiramavala

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
