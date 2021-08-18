import requests
url = 'https://api.telegram.org/bot1974553065:AAGm9ZRmLymL9bWx-inSxEIKLTigQHGgtT4/'

dict1 = {'s01e01': 'https://t.me/friends25yrs/6', 's01e02': 'https://t.me/friends25yrs/7', 's01e03': 'https://t.me/friends25yrs/8', 's01e04': 'https://t.me/friends25yrs/11', 's01e05': 'https://t.me/friends25yrs/13', 's01e06': 'https://t.me/friends25yrs/14', 's01e07': 'https://t.me/friends25yrs/15', 's01e08': 'https://t.me/friends25yrs/16', 's01e09': 'https://t.me/friends25yrs/17', 's01e10': 'https://t.me/friends25yrs/20', 's01e11': 'https://t.me/friends25yrs/21', 's01e12': 'https://t.me/friends25yrs/22',
         's01e13': 'https://t.me/friends25yrs/23', 's01e14': 'https://t.me/friends25yrs/24', 's01e15': 'https://t.me/friends25yrs/25', 's01e16': 'https://t.me/friends25yrs/27', 's01e17': 'https://t.me/friends25yrs/28', 's01e18': 'https://t.me/friends25yrs/29', 's01e19': 'https://t.me/friends25yrs/30', 's01e20': 'https://t.me/friends25yrs/31', 's01e21': 'https://t.me/friends25yrs/32', 's01e22': 'https://t.me/friends25yrs/33', 's01e23': 'https://t.me/friends25yrs/35', 's01e24': 'https://t.me/friends25yrs/37'}

dict2 = {'s02e01': 'https://t.me/friends25yrs/53', 's02e02': 'https://t.me/friends25yrs/54', 's02e03': 'https://t.me/friends25yrs/55', 's02e04': 'https://t.me/friends25yrs/56', 's02e05': 'https://t.me/friends25yrs/57', 's02e06': 'https://t.me/friends25yrs/58', 's02e07': 'https://t.me/friends25yrs/59', 's02e08': 'https://t.me/friends25yrs/60', 's02e09': 'https://t.me/friends25yrs/61', 's02e10': 'https://t.me/friends25yrs/62', 's02e11': 'https://t.me/friends25yrs/63', 's02e12': 'https://t.me/friends25yrs/64',
         's02e13': 'https://t.me/friends25yrs/65', 's02e14': 'https://t.me/friends25yrs/66', 's02e15': 'https://t.me/friends25yrs/67', 's02e16': 'https://t.me/friends25yrs/68', 's02e17': 'https://t.me/friends25yrs/69', 's02e18': 'https://t.me/friends25yrs/70', 's02e19': 'https://t.me/friends25yrs/71', 's02e20': 'https://t.me/friends25yrs/72', 's02e21': 'https://t.me/friends25yrs/73', 's02e22': 'https://t.me/friends25yrs/75', 's02e23': 'https://t.me/friends25yrs/76', 's02e24': 'https://t.me/friends25yrs/77'}

dict3 = {'s03e01': 'https://t.me/friends25yrs/79', 's03e02': 'https://t.me/friends25yrs/82', 's03e03': 'https://t.me/friends25yrs/83', 's03e04': 'https://t.me/friends25yrs/84', 's03e05': 'https://t.me/friends25yrs/85', 's03e06': 'https://t.me/friends25yrs/86', 's03e07': 'https://t.me/friends25yrs/87', 's03e08': 'https://t.me/friends25yrs/88', 's03e09': 'https://t.me/friends25yrs/89', 's03e10': 'https://t.me/friends25yrs/90', 's03e11': 'https://t.me/friends25yrs/91', 's03e12': 'https://t.me/friends25yrs/92',
         's03e13': 'https://t.me/friends25yrs/93', 's03e14': 'https://t.me/friends25yrs/94', 's03e15': 'https://t.me/friends25yrs/95', 's03e16': 'https://t.me/friends25yrs/96', 's03e17': 'https://t.me/friends25yrs/97', 's03e18': 'https://t.me/friends25yrs/98', 's03e19': 'https://t.me/friends25yrs/99', 's03e20': 'https://t.me/friends25yrs/100', 's03e21': 'https://t.me/friends25yrs/101', 's03e22': 'https://t.me/friends25yrs/102', 's03e23': 'https://t.me/friends25yrs/103', 's03e24': 'https://t.me/friends25yrs/104', 's03e25': 'https://t.me/friends25yrs/105'}

dict4 = {'s04e01': 'https://t.me/friends25yrs/108', 's04e02': 'https://t.me/friends25yrs/109', 's04e03': 'https://t.me/friends25yrs/110', 's04e04': 'https://t.me/friends25yrs/111', 's04e05': 'https://t.me/friends25yrs/112', 's04e06': 'https://t.me/friends25yrs/113', 's04e07': 'https://t.me/friends25yrs/114', 's04e08': 'https://t.me/friends25yrs/115', 's04e09': 'https://t.me/friends25yrs/116', 's04e10': 'https://t.me/friends25yrs/117', 's04e11': 'https://t.me/friends25yrs/118', 's04e12': 'https://t.me/friends25yrs/119',
         's04e13': 'https://t.me/friends25yrs/120', 's01e14': 'https://t.me/friends25yrs/121', 's04e15': 'https://t.me/friends25yrs/122', 's04e16': 'https://t.me/friends25yrs/123', 's04e17': 'https://t.me/friends2021complete/1318', 's04e18': 'https://t.me/friends25yrs/124', 's04e19': 'https://t.me/friends25yrs/125', 's04e20': 'https://t.me/friends25yrs/126', 's04e21': 'https://t.me/friends25yrs/127', 's04e22': 'https://t.me/friends25yrs/128', 's04e23': 'https://t.me/friends25yrs/129', 's04e24': ''}

dict5 = {'s05e01': 'https://t.me/friends2021complete/1327', 's05e02': 'https://t.me/friends2021complete/1328', 's05e03': 'https://t.me/friends2021complete/1329', 's05e04': 'https://t.me/friends2021complete/1330', 's05e05': 'https://t.me/friends2021complete/1331', 's05e06': 'https://t.me/friends2021complete/1332', 's05e07': 'https://t.me/friends2021complete/1333', 's05e08': 'https://t.me/friends2021complete/1334', 's05e09': 'https://t.me/friends2021complete/1335', 's05e10': 'https://t.me/friends2021complete/1336', 's05e11': 'https://t.me/friends2021complete/1337', 's05e12': 'https://t.me/friends2021complete/1338',
         's05e13': 'https://t.me/friends2021complete/1339', 's01e14': 'https://t.me/friends2021complete/1340', 's05e15': 'https://t.me/friends2021complete/1341', 's05e16': 'https://t.me/friends2021complete/1342', 's05e17': 'https://t.me/friends2021complete/1343', 's05e18': 'https://t.me/friends2021complete/1344', 's05e19': 'https://t.me/friends2021complete/1345', 's05e20': 'https://t.me/friends2021complete/1346', 's05e21': 'https://t.me/friends2021complete/1347', 's05e22': 'https://t.me/friends2021complete/1348', 's05e23': 'https://t.me/friends2021complete/1349', 's05e24': 'https://t.me/friends2021complete/1350'}

dict6 = {'s06e01': 'https://t.me/friends2021complete/1352', 's06e02': 'https://t.me/friends2021complete/1355', 's06e03': 'https://t.me/friends2021complete/1356', 's06e04': 'https://t.me/friends2021complete/1357', 's06e05': 'https://t.me/friends2021complete/1358', 's06e06': 'https://t.me/friends2021complete/1359', 's06e07': 'https://t.me/friends2021complete/1360', 's06e08': 'https://t.me/friends2021complete/1364', 's06e09': 'https://t.me/friends2021complete/1366', 's06e10': 'https://t.me/friends2021complete/1369', 's06e11': 'https://t.me/friends2021complete/1370', 's06e12': 'https://t.me/friends2021complete/1371',
         's06e13': 'https://t.me/friends2021complete/1372', 's01e14': 'https://t.me/friends2021complete/1373', 's06e15': 'https://t.me/friends2021complete/1374', 's06e16': 'https://t.me/friends2021complete/1375', 's06e17': 'https://t.me/friends2021complete/1376', 's06e18': 'https://t.me/friends2021complete/1378', 's06e19': 'https://t.me/friends2021complete/1380', 's06e20': 'https://t.me/friends2021complete/1383', 's06e21': 'https://t.me/friends2021complete/1385', 's06e22': 'https://t.me/friends2021complete/1390', 's06e23': 'https://t.me/friends2021complete/1391', 's06e24': 'https://t.me/friends2021complete/1392', 's06s25': 'https://t.me/friends2021complete/1393'}

dict7 = {'s07e01': '', 's07e02': '', 's07e03': '', 's07e04': '', 's07e05': '', 's07e06': '', 's07e07': '', 's07e08': '', 's07e09': '', 's07e10': '', 's07e11': '', 's07e12': '',
         's07e13': '', 's01e14': '', 's07e15': '', 's07e16': '', 's07e17': '', 's07e18': '', 's07e19': '', 's07e20': '', 's07e21': '', 's07e22': '', 's07e23': '', 's07e24': ''}

dict8 = {'s08e01': '', 's08e02': '', 's08e03': '', 's08e04': '', 's08e05': '', 's08e06': '', 's08e07': '', 's08e08': '', 's08e09': '', 's08e10': '', 's08e11': '', 's08e12': '',
         's08e13': '', 's01e14': '', 's08e15': '', 's08e16': '', 's08e17': '', 's08e18': '', 's08e19': '', 's08e20': '', 's08e21': '', 's08e22': '', 's08e23': '', 's08e24': ''}

dict9 = {'s09e01': '', 's09e02': '', 's09e03': '', 's09e04': '', 's09e05': '', 's09e06': '', 's09e07': '', 's09e08': '', 's09e09': '', 's09e10': '', 's09e11': '', 's09e12': '',
         's09e13': '', 's01e14': '', 's09e15': '', 's09e16': '', 's09e17': '', 's09e18': '', 's09e19': '', 's09e20': '', 's09e21': '', 's09e22': '', 's09e23': '', 's09e24': ''}

dict10 = {'s010e01': '', 's010e02': '', 's010e03': '', 's010e04': '', 's010e05': '', 's010e06': '', 's010e07': '', 's010e08': '', 's010e09': '', 's010e10': '', 's010e11': '', 's010e12': '',
          's010e13': '', 's01e14': '', 's010e15': '', 's010e16': '', 's010e17': '', 's010e18': '', 's010e19': '', 's010e20': '', 's010e21': '', 's010e22': '', 's010e23': '', 's010e24': ''}

'''dict11 = {'s01e01': '', 's01e02': '', 's01e03': '', 's01e04': '', 's01e05': '', 's01e06': '', 's01e07': '', 's01e08': '', 's01e09': '', 's01e10': '', 's01e11': '', 's01e12': '',
          's01e13': '', 's01e14': '', 's01e15': '', 's01e16': '', 's01e17': '', 's01e18': '', 's01e19': '', 's01e20': '', 's01e21': '', 's01e22': '', 's01e23': '', 's01e24': ''}

dict22 = {'s02e01': '', 's02e02': '', 's02e03': '', 's02e04': '', 's02e05': '', 's02e06': '', 's02e07': '', 's02e08': '', 's02e09': '', 's02e10': '', 's02e11': '', 's02e12': '',
          's02e13': '', 's01e14': '', 's02e15': '', 's02e16': '', 's02e17': '', 's02e18': '', 's02e19': '', 's02e20': '', 's02e21': '', 's02e22': '', 's02e23': '', 's02e24': ''}

dict33 = {'s03e01': '', 's03e02': '', 's03e03': '', 's03e04': '', 's03e05': '', 's03e06': '', 's03e07': '', 's03e08': '', 's03e09': '', 's03e10': '', 's03e11': '', 's03e12': '',
          's03e13': '', 's01e14': '', 's03e15': '', 's03e16': '', 's03e17': '', 's03e18': '', 's03e19': '', 's03e20': '', 's03e21': '', 's03e22': '', 's03e23': '', 's03e24': ''}

dict44 = {'s04e01': '', 's04e02': '', 's04e03': '', 's04e04': '', 's04e05': '', 's04e06': '', 's04e07': '', 's04e08': '', 's04e09': '', 's04e10': '', 's04e11': '', 's04e12': '',
          's04e13': '', 's01e14': '', 's04e15': '', 's04e16': '', 's04e17': '', 's04e18': '', 's04e19': '', 's04e20': '', 's04e21': '', 's04e22': '', 's04e23': '', 's04e24': ''}

dict55 = {'s05e01': '', 's05e02': '', 's05e03': '', 's05e04': '', 's05e05': '', 's05e06': '', 's05e07': '', 's05e08': '', 's05e09': '', 's05e10': '', 's05e11': '', 's05e12': '',
          's05e13': '', 's01e14': '', 's05e15': '', 's05e16': '', 's05e17': '', 's05e18': '', 's05e19': '', 's05e20': '', 's05e21': '', 's05e22': '', 's05e23': '', 's05e24': ''}

dict66 = {'s06e01': '', 's06e02': '', 's06e03': '', 's06e04': '', 's06e05': '', 's06e06': '', 's06e07': '', 's06e08': '', 's06e09': '', 's06e10': '', 's06e11': '', 's06e12': '',
          's06e13': '', 's01e14': '', 's06e15': '', 's06e16': '', 's06e17': '', 's06e18': '', 's06e19': '', 's06e20': '', 's06e21': '', 's06e22': '', 's06e23': '', 's06e24': ''}

dict77 = {'s07e01': '', 's07e02': '', 's07e03': '', 's07e04': '', 's07e05': '', 's07e06': '', 's07e07': '', 's07e08': '', 's07e09': '', 's07e10': '', 's07e11': '', 's07e12': '',
          's07e13': '', 's01e14': '', 's07e15': '', 's07e16': '', 's07e17': '', 's07e18': '', 's07e19': '', 's07e20': '', 's07e21': '', 's07e22': '', 's07e23': '', 's07e24': ''}

dict88 = {'s08e01': '', 's08e02': '', 's08e03': '', 's08e04': '', 's08e05': '', 's08e06': '', 's08e07': '', 's08e08': '', 's08e09': '', 's08e10': '', 's08e11': '', 's08e12': '',
          's08e13': '', 's01e14': '', 's08e15': '', 's08e16': '', 's08e17': '', 's08e18': '', 's08e19': '', 's08e20': '', 's08e21': '', 's08e22': '', 's08e23': '', 's08e24': ''}

dict99 = {'s09e01': '', 's09e02': '', 's09e03': '', 's09e04': '', 's09e05': '', 's09e06': '', 's09e07': '', 's09e08': '', 's09e09': '', 's09e10': '', 's09e11': '', 's09e12': '',
          's09e13': '', 's01e14': '', 's09e15': '', 's09e16': '', 's09e17': '', 's09e18': '', 's09e19': '', 's09e20': '', 's09e21': '', 's09e22': '', 's09e23': '', 's09e24': ''}

dict1010 = {'s010e01': '', 's010e02': '', 's010e03': '', 's010e04': '', 's010e05': '', 's010e06': '', 's010e07': '', 's010e08': '', 's010e09': '', 's010e10': '', 's010e11': '', 's010e12': '',
            's010e13': '', 's01e14': '', 's010e15': '', 's010e16': '', 's010e17': '', 's010e18': '', 's010e19': '', 's010e20': '', 's010e21': '', 's010e22': '', 's010e23': '', 's010e24': ''}'''


def send_message(url, chat_id, message):
    if message == 'hi':
        reply = "How u doin'😉"
        send = requests.post(url+'sendMessage?chat_id=' +
                             str(chat_id)+'&text='+reply)
        print(send)
        # return send

# start
    elif message == '/start':
        reply = '''
        Hola! 
        I'm the F.R.I.E.N.D.S bot, here 
        to help you with downloing the 
        series.

        Use `s01e01` to download episode 
        1 of season 1.

        Use `s05` to download season 5 
        all episodes.

        If you want to know more about 
        the series and some interesting 
        facts about our main charecters, 
        use their first name as the 
        command.

        For any help regarding the 
        commands, use the command 
        `help` or `/help`. 

        To get to know about the 
        developers use the command 
        `info`.

        PS: The episode and season 
        commands give you two ways to 
        access the series. One, direcly 
        download the episode another to 
        stream it online using "playit" 
        app in your mobiles.
        '''
        send = requests.post(url+'sendMessage?chat_id=' +
                             str(chat_id)+'&text='+reply)

# info
    elif message == 'info':
        reply = '''
       Hey there! 
       We are the biggest fans of the sitcom F.R.I.E.N.D.S, so we wanted to make this available for all people so they can access it easily.
        For any suggestions or complaints to report contact
        @dbalajivaraprasad
        @CHAKRADHAR_GBG
        @abhiramavala
        '''
        send = requests.post(url+'sendMessage?chat_id=' +
                             str(chat_id)+'&text='+reply)

    elif message in dict1.keys():
        reply = dict1[message]
        send = requests.post(url+'sendMessage?chat_id=' +
                             str(chat_id)+'&text='+reply)

    elif message in dict2.keys():
        reply = dict2[message]
        send = requests.post(url+'sendMessage?chat_id=' +
                             str(chat_id)+'&text='+reply)

    elif message in dict3.keys():
        reply = dict3[message]
        send = requests.post(url+'sendMessage?chat_id=' +
                             str(chat_id)+'&text='+reply)


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
