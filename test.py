import requests
url = 'https://api.telegram.org/bot1974553065:AAGm9ZRmLymL9bWx-inSxEIKLTigQHGgtT4/'
#Abhiram_Avala_Start
#Abhiram_Avala

list1 = ['s01e01','s01e02','s01e03','s01e04','s01e05','s01e06','s01e07','s01e08','s01e09','s01e10','s01e11','s01e12','s01e13','s01e14','s01e15','s01e16','s01e17','s01e18','s01e19','s01e20','s01e21','s01e22','s01e23','s01e24']
dict1 = {'s01e01':'https://t.me/friends25yrs/6','s01e02':'https://t.me/friends25yrs/7','s01e03':'https://t.me/friends25yrs/8','s01e04':'https://t.me/friends25yrs/11','s01e05':'https://t.me/friends25yrs/13','s01e06':'https://t.me/friends25yrs/14','s01e07':'https://t.me/friends25yrs/15','s01e08':'https://t.me/friends25yrs/16','s01e09':'https://t.me/friends25yrs/17','s01e10':'https://t.me/friends25yrs/20','s01e11':'https://t.me/friends25yrs/21','s01e12':'https://t.me/friends25yrs/22','s01e13':'https://t.me/friends25yrs/23','s01e14':'https://t.me/friends25yrs/24','s01e15':'https://t.me/friends25yrs/25','s01e16':'https://t.me/friends25yrs/27','s01e17':'https://t.me/friends25yrs/28','s01e18':'https://t.me/friends25yrs/29','s01e19':'https://t.me/friends25yrs/30','s01e20':'https://t.me/friends25yrs/31','s01e21':'https://t.me/friends25yrs/32','s01e22':'https://t.me/friends25yrs/33','s01e23':'https://t.me/friends25yrs/35','s01e24':'https://t.me/friends25yrs/37'}
list2 = ['s02e01','s02e02','s02e03','s02e04','s02e05','s02e06','s02e07','s02e08','s02e09','s02e10','s02e11','s02e12','s02e13','s02e14','s02e15','s02e16','s02e17','s02e18','s02e19','s02e20','s02e21','s02e22','s02e23','s02e24']
dict2 = {'s02e01':'https://t.me/friends25yrs/53','s02e02':'https://t.me/friends25yrs/54','s02e03':'https://t.me/friends25yrs/55','s02e04':'https://t.me/friends25yrs/56','s02e05':'https://t.me/friends25yrs/57','s02e06':'https://t.me/friends25yrs/58','s02e07':'https://t.me/friends25yrs/59','s02e08':'https://t.me/friends25yrs/60','s02e09':'https://t.me/friends25yrs/61','s02e10':'https://t.me/friends25yrs/62','s02e11':'https://t.me/friends25yrs/63','s02e12':'https://t.me/friends25yrs/64','s02e13':'https://t.me/friends25yrs/65','s02e14':'https://t.me/friends25yrs/66','s02e15':'https://t.me/friends25yrs/67','s02e16':'https://t.me/friends25yrs/68','s02e17':'https://t.me/friends25yrs/69','s02e18':'https://t.me/friends25yrs/70','s02e19':'https://t.me/friends25yrs/71','s02e20':'https://t.me/friends25yrs/72','s02e21':'https://t.me/friends25yrs/73','s02e22':'https://t.me/friends25yrs/75','s02e23':'https://t.me/friends25yrs/76','s02e24':'https://t.me/friends25yrs/77'}
list3 = ['s03e01','s03e02','s03e03','s03e04','s03e05','s03e06','s03e07','s03e08','s03e09','s03e10','s03e11','s03e12','s03e13','s03e14','s03e15','s03e16','s03e17','s03e18','s03e19','s03e20','s03e21','s03e22','s03e23','s03e24']
dict3 = {'s03e01':'https://t.me/friends25yrs/79','s03e02':'https://t.me/friends25yrs/82','s03e03':'https://t.me/friends25yrs/83','s03e04':'https://t.me/friends25yrs/84','s03e05':'https://t.me/friends25yrs/85','s03e06':'https://t.me/friends25yrs/86','s03e07':'https://t.me/friends25yrs/87','s03e08':'https://t.me/friends25yrs/88','s03e09':'https://t.me/friends25yrs/89','s03e10':'https://t.me/friends25yrs/90','s03e11':'https://t.me/friends25yrs/91','s03e12':'https://t.me/friends25yrs/92','s03e13':'https://t.me/friends25yrs/93','s03e14':'https://t.me/friends25yrs/94','s03e15':'https://t.me/friends25yrs/95','s03e16':'https://t.me/friends25yrs/96','s03e17':'https://t.me/friends25yrs/97','s03e18':'https://t.me/friends25yrs/98','s03e19':'https://t.me/friends25yrs/99','s03e20':'https://t.me/friends25yrs/100','s03e21':'https://t.me/friends25yrs/101','s03e22':'https://t.me/friends25yrs/102','s03e23':'https://t.me/friends25yrs/103','s03e24':'https://t.me/friends25yrs/104','s03e25':'https://t.me/friends25yrs/105'}

#Abhiram_Avala
#Abhiram_Avala_End

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
        # print(send)
        # return send
    elif message == 's05e20':
        requests.post(url + 'sendMessage?chat_id='+str(chat_id) +
                      '&text='+'https://t.me/friends25yrs/151')
    elif message == 'friends':
        requests.post(url + 'sendMessage?chat_id='+str(chat_id) +
                      '&text= https://mega.nz/file/4VswUaIB#wGvdagunBcgb6cVyU4VkSakP23kq4kFBP_5CCnu21Gs')
        requests.post(url + 'sendMessage?chat_id='+str(chat_id)+'&text=' +
                      'Decryption key = wGvdagunBcgb6cVyU4VkSakP23kq4kFBP_5CCnu21Gs')
    
    #Abhiram_Avala_Start
    #Abhiram_Avala

    elif message in list1:
        for i in list1:
            if message == i:
                reply = dict1[i]
                send = requests.post(url+'sendMessage?chat_id=' +
                                    str(chat_id)+'&text='+reply)
    
    elif message in list2:
        for i in list2:
            if message == i:
                reply = dict2[i]
                send = requests.post(url+'sendMessage?chat_id=' +
                                    str(chat_id)+'&text='+reply)

    elif message in list3:
        for i in list3:
            if message == i:
                reply = dict3[i]
                send = requests.post(url+'sendMessage?chat_id=' +
                                    str(chat_id)+'&text='+reply)

    #Abhiram_Avala
    #Abhiram_Avala_End

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
