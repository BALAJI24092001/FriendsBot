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
         's06e13': 'https://t.me/friends2021complete/1372', 's01e14': 'https://t.me/friends2021complete/1373', 's06e15': 'https://t.me/friends2021complete/1374', 's06e16': 'https://t.me/friends2021complete/1375', 's06e17': 'https://t.me/friends2021complete/1376', 's06e18': 'https://t.me/friends2021complete/1378', 's06e19': 'https://t.me/friends2021complete/1380', 's06e20': 'https://t.me/friends2021complete/1383', 's06e21': 'https://t.me/friends2021complete/1385', 's06e22': 'https://t.me/friends2021complete/1390', 's06e23': 'https://t.me/friends2021complete/1391', 's06e24': 'https://t.me/friends2021complete/1392','s06s25':'https://t.me/friends2021complete/1393'}

dict7 = {'s07e01': 'https://t.me/friendscompletesubtitle/654', 's07e02': 'https://t.me/friendscompletesubtitle/655', 's07e03': 'https://t.me/friendscompletesubtitle/656', 's07e04': 'https://t.me/friendscompletesubtitle/657', 's07e05': 'https://t.me/friendscompletesubtitle/659', 's07e06': 'https://t.me/friendscompletesubtitle/660', 's07e07': 'https://t.me/friendscompletesubtitle/661', 's07e08': 'https://t.me/friendscompletesubtitle/663', 's07e09': 'https://t.me/friendscompletesubtitle/664', 's07e10': 'https://t.me/friendscompletesubtitle/665', 's07e11': 'https://t.me/friendscompletesubtitle/666', 's07e12': 'https://t.me/friendscompletesubtitle/667',
          's07e13': 'https://t.me/friendscompletesubtitle/668', 's01e14': 'https://t.me/friendscompletesubtitle/669', 's07e15': 'https://t.me/friendscompletesubtitle/670', 's07e16': 'https://t.me/friendscompletesubtitle/671', 's07e17': 'https://t.me/friendscompletesubtitle/672', 's07e18': 'https://t.me/friendscompletesubtitle/673', 's07e19': 'https://t.me/friendscompletesubtitle/674', 's07e20': 'https://t.me/friendscompletesubtitle/675', 's07e21': 'https://t.me/friendscompletesubtitle/676', 's07e22': 'https://t.me/friendscompletesubtitle/677', 's07e23': 'https://t.me/friendscompletesubtitle/678', 's07e24': 'https://t.me/friendscompletesubtitle/680'}

dict8 = {'s08e01': 'https://t.me/friendscompletesubtitle/682', 's08e02': 'https://t.me/friendscompletesubtitle/683', 's08e03': 'https://t.me/friendscompletesubtitle/684', 's08e04': 'https://t.me/friendscompletesubtitle/685', 's08e05': 'https://t.me/friendscompletesubtitle/686', 's08e06': 'https://t.me/friendscompletesubtitle/687', 's08e07': 'https://t.me/friendscompletesubtitle/688', 's08e08': 'https://t.me/friendscompletesubtitle/689', 's08e09': 'https://t.me/friendscompletesubtitle/690', 's08e10': 'https://t.me/friendscompletesubtitle/691', 's08e11': 'https://t.me/friendscompletesubtitle/692', 's08e12': 'https://t.me/friendscompletesubtitle/693',
          's08e13': 'https://t.me/friendscompletesubtitle/694', 's01e14': 'https://t.me/friendscompletesubtitle/696', 's08e15': 'https://t.me/friendscompletesubtitle/697', 's08e16': 'https://t.me/friendscompletesubtitle/698', 's08e17': 'https://t.me/friendscompletesubtitle/699', 's08e18': 'https://t.me/friendscompletesubtitle/700', 's08e19': 'https://t.me/friendscompletesubtitle/701', 's08e20': 'https://t.me/friendscompletesubtitle/702', 's08e21': 'https://t.me/friendscompletesubtitle/703', 's08e22': 'https://t.me/friendscompletesubtitle/704', 's08e23': 'https://t.me/friendscompletesubtitle/705', 's08e24': 'https://t.me/friendscompletesubtitle/706'}

dict9 = {'s09e01': 'https://t.me/friendscompletesubtitle/708', 's09e02': 'https://t.me/friendscompletesubtitle/709', 's09e03': 'https://t.me/friendscompletesubtitle/710', 's09e04': 'https://t.me/friendscompletesubtitle/711', 's09e05': 'https://t.me/friendscompletesubtitle/712', 's09e06': 'https://t.me/friendscompletesubtitle/713', 's09e07': 'https://t.me/friendscompletesubtitle/714', 's09e08': 'https://t.me/friendscompletesubtitle/715', 's09e09': 'https://t.me/friendscompletesubtitle/716', 's09e10': 'https://t.me/friendscompletesubtitle/717', 's09e11': 'https://t.me/friendscompletesubtitle/718', 's09e12': 'https://t.me/friendscompletesubtitle/719',
          's09e13': 'https://t.me/friendscompletesubtitle/720', 's01e14': 'https://t.me/friendscompletesubtitle/721', 's09e15': 'https://t.me/friendscompletesubtitle/722', 's09e16': 'https://t.me/friendscompletesubtitle/723', 's09e17': 'https://t.me/friendscompletesubtitle/724', 's09e18': 'https://t.me/friendscompletesubtitle/725', 's09e19': 'https://t.me/friendscompletesubtitle/726', 's09e20': 'https://t.me/friendscompletesubtitle/727', 's09e21': 'https://t.me/friendscompletesubtitle/728', 's09e22': 'https://t.me/friendscompletesubtitle/729', 's09e23': 'https://t.me/friendscompletesubtitle/730', 's09e24': 'https://t.me/friendscompletesubtitle/730'}

dict10 = {'s10e01': 'https://t.me/friendscompletesubtitle/732', 's10e02': 'https://t.me/friendscompletesubtitle/733', 's10e03': 'https://t.me/friendscompletesubtitle/734', 's10e04': 'https://t.me/friendscompletesubtitle/735', 's10e05': 'https://t.me/friendscompletesubtitle/737', 's10e06': 'https://t.me/friendscompletesubtitle/738', 's10e07': 'https://t.me/friendscompletesubtitle/739', 's10e08': 'https://t.me/friendscompletesubtitle/740', 's10e09': 'https://t.me/friendscompletesubtitle/741', 's10e10': 'https://t.me/friendscompletesubtitle/742', 's10e11': 'https://t.me/friendscompletesubtitle/743', 's10e12': 'https://t.me/friendscompletesubtitle/744',
            's10e13': 'https://t.me/friendscompletesubtitle/745', 's10e14': 'https://t.me/friendscompletesubtitle/746', 's10e15': 'https://t.me/friendscompletesubtitle/747', 's10e16': 'https://t.me/friendscompletesubtitle/748', 's10e17': 'https://t.me/friendscompletesubtitle/749', 's10e18': 'https://t.me/friendscompletesubtitle/749'}

dict11 = {'s01e01': 'https://kuklink.com/1/bnYyZnZ0MDAxdWh5', 's01e02': 'https://kuklink.com/1/bnYyZnZ4MDAwMmI1', 's01e03': 'https://kuklink.com/1/bnYyZnZ4MDAwNXN6', 's01e04': 'https://kuklink.com/1/bnYyZnZ4MDAwMGY4', 's01e05': 'http://www.pdisk.net/share-video?videoid=nv2fvx000ea1', 's01e06': 'https://kuklink.com/1/bnYyZnZ4MDAwb2Rx', 's01e07': 'https://kuklink.com/1/bnYyZnZ4MDAwdHB3', 's01e08': 'https://kuklink.com/1/bnYyZnZ4MDAwbWxk', 's01e09': 'https://kuklink.com/1/bnYyZnZ4MDAwYmFj', 's01e10': 'https://kuklink.com/1/bnYyZnZ4MDAwc2o1', 's01e11': 'https://kuklink.com/1/bnYyZnZ4MDAwams1', 's01e12': 'https://kuklink.com/1/bnYyZnZ4MDAwZDN1',
          's01e13': 'https://kuklink.com/1/bnYyZnZ4MDAwYmM2', 's01e14': 'https://kuklink.com/1/bnYyZnZ4MDAwNHM3', 's01e15': 'https://kuklink.com/1/bnYyZnZ4MDAwbG0y', 's01e16': 'https://kuklink.com/1/bnYyZnZ4MDAwaDBz', 's01e17': 'https://kuklink.com/1/bnYyZnZ4MDAwaWpp', 's01e18': 'https://kuklink.com/1/bnYyZnZ4MDAwOTZ2', 's01e19': 'https://kuklink.com/1/bnYyZnZ4MDAweXpj', 's01e20': 'https://kuklink.com/1/bnYyZnZ4MDAwOGw5', 's01e21': 'https://kuklink.com/1/bnYyZnZ4MDAwa3Rw', 's01e22': 'https://kuklink.com/1/bnYyZnZ4MDAwbjhk', 's01e23': 'https://kuklink.com/1/bnYyZnZ4MDAwbDBm', 's01e24': 'https://kuklink.com/1/bnYyZnZ4MDAwbnhr'}

dict22 = {'s02e01': 'https://kuklink.com/1/bnYyZncxMDAweW1v', 's02e02': 'https://kuklink.com/1/bnYyZncxMDA0eTdh', 's02e03': 'https://kuklink.com/1/bnYyZncxMDAwNHc4', 's02e04': 'https://kuklink.com/1/bnYyZncxMDA1ZzFh', 's02e05': 'https://kuklink.com/1/bnYyZncxMDAwYjli', 's02e06': 'https://kuklink.com/1/bnYyZncxMDAxbTVz', 's02e07': 'https://kuklink.com/1/bnYyZncxMDAyOTUz', 's02e08': 'https://kuklink.com/1/bnYyZncxMDA0anVz', 's02e09': 'https://kuklink.com/1/bnYyZncxMDAwZGdk', 's02e10': 'https://kuklink.com/1/bnYyZncxMDAxbW1o', 's02e11': 'https://kuklink.com/1/bnYyZncxMDA1cmZn', 's02e12': 'https://kuklink.com/1/bnYyZncxMDAxbjJ0',
          's02e13': 'https://kuklink.com/1/bnYyZncxMDAzaW9w', 's01e14': 'https://kuklink.com/1/bnYyZncxMDAwdHZw', 's02e15': 'https://kuklink.com/1/bnYyZncxMDAxYWZ6', 's02e16': 'https://kuklink.com/1/bnYyZncxMDA0MDVk', 's02e17': 'https://kuklink.com/1/bnYyZncxMDAyd3hn', 's02e18': 'https://kuklink.com/1/bnYyZncxMDA1cTJi', 's02e19': 'https://kuklink.com/1/bnYyZncxMDA0cGJr', 's02e20': 'https://kuklink.com/1/bnYyZncxMDA1ZHJy', 's02e21': 'https://kuklink.com/1/bnYyZncxMDA0d3Bv', 's02e22': 'https://kuklink.com/1/bnYyZncxMDAyb2R3', 's02e23': 'https://kuklink.com/1/bnYyZncxMDAyNG5u', 's02e24': 'https://kuklink.com/1/bnYyZncxMDAxeW1m'}

dict33 = {'s03e01': 'https://kuklink.com/1/bnYyZnc1MDAwM3Ro', 's03e02': 'https://kuklink.com/1/bnYyZnc1MDAwMW41', 's03e03': 'https://kuklink.com/1/bnYyZnc1MDAwMTB2', 's03e04': 'https://kuklink.com/1/bnYyZnc1MDAwNHpn', 's03e05': 'https://kuklink.com/1/bnYyZnc1MDAwNWxo', 's03e06': 'https://kuklink.com/1/bnYyZnc1MDAwOGkz', 's03e07': 'https://kuklink.com/1/bnYyZnc1MDAwZmRk', 's03e08': 'https://kuklink.com/1/bnYyZnc1MDAwbWl5', 's03e09': 'https://kuklink.com/1/bnYyZnc1MDAwdHR5', 's03e10': 'https://kuklink.com/1/bnYyZnc1MDAwa3Ay', 's03e11': 'https://kuklink.com/1/bnYyZnc1MDAwZHN5', 's03e12': 'https://kuklink.com/1/bnYyZnc1MDAwY3du',
          's03e13': 'https://kuklink.com/1/bnYyZnc1MDAweXd3', 's01e14': 'https://kuklink.com/1/bnYyZnc1MDAwbnBn', 's03e15': 'https://kuklink.com/1/bnYyZnc1MDAwc2w1', 's03e16': 'https://kuklink.com/1/bnYyZnc1MDAwbG80', 's03e17': 'https://kuklink.com/1/bnYyZnc1MDAwdXMy', 's03e18': 'https://kuklink.com/1/bnYyZnc1MDAwdmty', 's03e19': 'https://kuklink.com/1/bnYyZnc1MDAwN3hq', 's03e20': 'https://kuklink.com/1/bnYyZnc1MDAwejNl', 's03e21': 'https://kuklink.com/1/bnYyZnc1MDAwdWF4', 's03e22': 'https://kuklink.com/1/bnYyZnc1MDAwbm1p', 's03e23': 'https://kuklink.com/1/bnYyZnc1MDAwcm5q', 's03e24': 'https://kuklink.com/1/bnYyZnc1MDAwZ25i', 's03e25': 'https://kuklink.com/1/bnYyZnc1MDAwMzhh'}

dict44 = {'s04e01': 'https://kuklink.com/1/bnYyZnc1MDAwZWwy', 's04e02': 'https://kuklink.com/1/bnYyZnc1MDAwcWQ3', 's04e03': 'https://kuklink.com/1/bnYyZnc1MDAwN2ti', 's04e04': 'https://kuklink.com/1/bnYyZnc1MDAwMzg2', 's04e05': 'https://kuklink.com/1/bnYyZnc1MDAwNXRn', 's04e06': 'https://kuklink.com/1/bnYyZnc1MDAwZm16', 's04e07': 'https://kuklink.com/1/bnYyZnc1MDAwMjZ2', 's04e08': 'https://kuklink.com/1/bnYyZnc1MDAwMDRo', 's04e09': 'https://kuklink.com/1/bnYyZnc1MDAweGw4', 's04e10': 'https://kuklink.com/1/bnYyZnc1MDAwazlz', 's04e11': 'https://kuklink.com/1/bnYyZnc1MDAwMXE0', 's04e12': 'https://kuklink.com/1/bnYyZnc1MDAwajFm',
          's04e13': 'https://kuklink.com/1/bnYyZnc1MDAwMThk', 's01e14': 'https://kuklink.com/1/bnYyZnc1MDAxbThy', 's04e15': 'https://kuklink.com/1/bnYyZnc1MDA0ZGh1', 's04e16': 'https://kuklink.com/1/bnYyZnc1MDA1NXJi', 's04e17': 'https://kuklink.com/1/bnYyZnc1MDA0d3Rj', 's04e18': 'https://kuklink.com/1/bnYyZnc1MDA0M3Nw', 's04e19': 'https://kuklink.com/1/bnYyZnc1MDAwNXMw', 's04e20': 'https://kuklink.com/1/bnYyZnc1MDA0ODZ0', 's04e21': 'https://kuklink.com/1/bnYyZnc1MDAzb3M4', 's04e22': 'https://kuklink.com/1/bnYyZnc1MDAyY2Nw', 's04e23': 'https://kuklink.com/1/bnYyZnc1MDAzNjlh', 's04e24': 'https://kuklink.com/1/bnYyZnc1MDAxaWF4'}

dict55 = {'s05e01': 'https://kuklink.com/1/bnYyZnc1MDAxaTZp', 's05e02': 'https://kuklink.com/1/bnYyZnc1MDAxOXFi', 's05e03': 'https://kuklink.com/1/bnYyZnc1MDAyOWxu', 's05e04': 'https://kuklink.com/1/bnYyZnc1MDA0c2g2', 's05e05': 'https://kuklink.com/1/bnYyZnc1MDAxNDdq', 's05e06': 'https://kuklink.com/1/bnYyZnc1MDAyOWUx', 's05e07': 'https://kuklink.com/1/bnYyZnc1MDAwc204', 's05e08': 'https://kuklink.com/1/bnYyZnc1MDAyaWJh', 's05e09': 'https://kuklink.com/1/bnYyZnc1MDA1bWU4', 's05e10': 'https://kuklink.com/1/bnYyZnc1MDAzY3hp', 's05e11': 'https://kuklink.com/1/bnYyZnc1MDAyMWVu', 's05e12': 'https://kuklink.com/1/bnYyZnc1MDA1OGJp',
          's05e13': 'https://kuklink.com/1/bnYyZnc1MDAybGJ0', 's01e14': 'https://kuklink.com/1/bnYyZnc1MDAxdnFs', 's05e15': 'https://kuklink.com/1/bnYyZnc1MDA0NDl0', 's05e16': 'https://kuklink.com/1/bnYyZnc1MDAwemY3', 's05e17': 'https://kuklink.com/1/bnYyZnc1MDAzZXNi', 's05e18': 'https://kuklink.com/1/bnYyZnc1MDAyaHd3', 's05e19': 'https://kuklink.com/1/bnYyZnc1MDA0bng0', 's05e20': 'https://kuklink.com/1/bnYyZnc1MDAwMGYz', 's05e21': 'https://kuklink.com/1/bnYyZnc1MDA0bWl4', 's05e22': 'https://kuklink.com/1/bnYyZnc1MDAydWdj', 's05e23': 'https://kuklink.com/1/bnYyZnc1MDA1anAy', 's05e24': 'https://kuklink.com/1/bnYyZnc1MDAwdjgw'}

dict66 = {'s06e01': 'https://kuklink.com/1/bnYyZndwMDAyOXE4', 's06e02': 'https://kuklink.com/1/bnYyZndwMDA0eHBj', 's06e03': 'https://kuklink.com/1/bnYyZndwMDAyeGNj', 's06e04': 'https://kuklink.com/1/bnYyZnd0MDAwNW9n', 's06e05': 'https://kuklink.com/1/bnYyZnd0MDAwMWti', 's06e06': 'https://kuklink.com/1/bnYyZnd0MDAwNHkx', 's06e07': 'https://kuklink.com/1/bnYyZnd0MDAwNDFw', 's06e08': 'https://kuklink.com/1/bnYyZnd0MDAwNXp1', 's06e09': 'https://kuklink.com/1/bnYyZnd0MDAwZ2Jy', 's06e10': 'https://kuklink.com/1/bnYyZnd0MDAwNmZ3', 's06e11': 'https://kuklink.com/1/bnYyZnd0MDAwa2Zx', 's06e12': 'https://kuklink.com/1/bnYyZnd0MDAwMTQw',
          's06e13': 'https://kuklink.com/1/bnYyZnd0MDAwMGVl', 's01e14': 'https://kuklink.com/1/bnYyZnd0MDAwajNx', 's06e15': 'https://kuklink.com/1/bnYyZnd0MDAwdWUx', 's06e16': 'https://kuklink.com/1/bnYyZnd0MDAwaGFq', 's06e17': 'https://kuklink.com/1/bnYyZnd0MDAweGRo', 's06e18': 'https://kuklink.com/1/bnYyZnd0MDAwcWlp', 's06e19': 'https://kuklink.com/1/bnYyZnd0MDAwYXdn', 's06e20': 'https://kuklink.com/1/bnYyZnd0MDAwaDd0', 's06e21': 'https://kuklink.com/1/bnYyZnd0MDAwazBw', 's06e22': 'https://kuklink.com/1/bnYyZnd0MDAwZTNr', 's06e23': 'https://kuklink.com/1/bnYyZnd0MDAweXgy', 's06e24': 'https://kuklink.com/1/bnYyZnd0MDAwbGJu', 's06e25': 'https://kuklink.com/1/bnYyZnd0MDAwaGQy'}

dict77 = {'s07e01': 'https://kuklink.com/1/bnYyZnh0MDAwcDR6', 's07e02': 'https://kuklink.com/1/bnYyZnh0MDA0bWZ1', 's07e03': 'https://kuklink.com/1/bnYyZnh0MDAxMGYw', 's07e04': 'https://kuklink.com/1/bnYyZnh0MDAzeGI1', 's07e05': 'https://kuklink.com/1/bnYyZnh0MDAzam5m', 's07e06': 'https://kuklink.com/1/bnYyZnh0MDAyOG4z', 's07e07': 'https://kuklink.com/1/bnYyZnh0MDA0MXN5', 's07e08': 'https://kuklink.com/1/bnYyZnh0MDA1bGI4', 's07e09': 'https://kuklink.com/1/bnYyZnh0MDAybDdw', 's07e10': 'https://kuklink.com/1/bnYyZnh0MDAxMTYy', 's07e11': 'https://kuklink.com/1/bnYyZnh0MDA1NXd5', 's07e12': 'https://kuklink.com/1/bnYyZnh0MDAzaG1s',
         's07e13': 'https://kuklink.com/1/bnYyZnh0MDAwMTlr', 's01e14': 'https://kuklink.com/1/bnYyZnh0MDAwemU2', 's07e15': 'https://kuklink.com/1/bnYyZnh0MDAzN3ox', 's07e16': 'https://kuklink.com/1/bnYyZnh0MDAwYWlr', 's07e17': 'https://kuklink.com/1/bnYyZnh0MDA1YnFx', 's07e18': 'https://kuklink.com/1/bnYyZnh0MDAxNHRo', 's07e19': 'https://kuklink.com/1/bnYyZnh0MDAxMnZy', 's07e20': 'https://kuklink.com/1/bnYyZnh0MDA1N2Yw', 's07e21': 'https://kuklink.com/1/bnYyZnh0MDAyMTdo', 's07e22': 'https://kuklink.com/1/bnYyZnh0MDA0MDR2', 's07e23': 'https://kuklink.com/1/bnYyZnh0MDA0Y3ho', 's07e24': 'https://kuklink.com/1/bnYyZnh0MDAwNHFj'}

dict88 = {'s08e01': 'https://kuklink.com/1/bnYyZnh4MDAxMHU1', 's08e02': 'https://kuklink.com/1/bnYyZnh4MDAzbG5y', 's08e03': 'https://kuklink.com/1/bnYyZnh4MDAxemVk', 's08e04': 'https://kuklink.com/1/bnYyZnh4MDA0dXIx', 's08e05': 'https://kuklink.com/1/bnYyZnh4MDAxNWFn', 's08e06': 'https://kuklink.com/1/bnYyZnh4MDA0dDM1', 's08e07': 'https://kuklink.com/1/bnYyZnh4MDAwNmEy', 's08e08': 'https://kuklink.com/1/bnYyZnh4MDAzdGx5', 's08e09': 'https://kuklink.com/1/bnYyZnh4MDA0ZjB4', 's08e10': 'https://kuklink.com/1/bnYyZnh4MDA0bW5l', 's08e11': 'https://kuklink.com/1/bnYyZnh4MDAzcDN1', 's08e12': 'https://kuklink.com/1/bnYyZnh4MDA1d2N4',
         's08e13': 'https://kuklink.com/1/bnYyZnh4MDAwd2F2', 's01e14': 'https://kuklink.com/1/bnYyZnh4MDA0b2xl', 's08e15': 'https://kuklink.com/1/bnYyZnh4MDAwdWhv', 's08e16': 'https://kuklink.com/1/bnYyZnh4MDAxNDdw', 's08e17': 'https://kuklink.com/1/bnYyZnh4MDAzdjRm', 's08e18': 'https://kuklink.com/1/bnYyZnh4MDAzb2lh', 's08e19': 'https://kuklink.com/1/bnYyZnh4MDA0OXYw', 's08e20': 'https://kuklink.com/1/bnYyZnh4MDAybHB6', 's08e21': 'https://kuklink.com/1/bnYyZnh4MDAwcGRv', 's08e22': 'https://kuklink.com/1/bnYyZnh4MDA1ejVm', 's08e23': 'https://kuklink.com/1/bnYyZnh4MDAyaGI1', 's08e24': 'https://kuklink.com/1/bnYyZnh4MDAwanpl'}

dict99 = {'s09e01': 'https://kuklink.com/1/bnYyZnh4MDA1dG9l', 's09e02': 'https://kuklink.com/1/bnYyZnh4MDAxZTZx', 's09e03': 'https://kuklink.com/1/bnYyZnh4MDAxejZm', 's09e04': 'https://kuklink.com/1/bnYyZnh4MDAxMzAy', 's09e05': 'https://kuklink.com/1/bnYyZnh4MDAwMmlm', 's09e06': 'https://kuklink.com/1/bnYyZnh4MDAyOGF2', 's09e07': 'https://kuklink.com/1/bnYyZnh4MDAxejN3', 's09e08': 'https://kuklink.com/1/bnYyZnh4MDAzNm9l', 's09e09': 'https://kuklink.com/1/bnYyZnh4MDAwbnd2', 's09e10': 'https://kuklink.com/1/bnYyZnh4MDAwZmR0', 's09e11': 'https://kuklink.com/1/bnYyZnh4MDAxdnh0', 's09e12': 'https://kuklink.com/1/bnYyZnh4MDAzb3oz',
         's09e13': 'https://kuklink.com/1/bnYyZnk1MDA0OHhr', 's01e14': 'https://kuklink.com/1/bnYyZnk1MDA1Z3lz', 's09e15': 'https://kuklink.com/1/bnYyZnk1MDA1NzB3', 's09e16': 'https://kuklink.com/1/bnYyZnk1MDAwczRw', 's09e17': 'https://kuklink.com/1/bnYyZnk1MDAxcWw2', 's09e18': 'https://kuklink.com/1/bnYyZnk1MDAwNGM3', 's09e19': 'https://kuklink.com/1/bnYyZnk1MDA1YWdq', 's09e20': 'https://kuklink.com/1/bnYyZnk1MDA0ODho', 's09e21': 'https://kuklink.com/1/bnYyZnk1MDAyeXBk', 's09e22': 'https://kuklink.com/1/bnYyZnk1MDAxYjE5', 's09e23': 'https://kuklink.com/1/bnYyZnk1MDA1cXdz', 's09e24': 'https://kuklink.com/1/bnYyZnk1MDA1cXdz'}

dict1010 = {'s010e01': 'https://kuklink.com/1/bnYyZnk1MDAyam5h', 's010e02': 'https://kuklink.com/1/bnYyZnk1MDA0cTFo', 's010e03': 'https://kuklink.com/1/bnYyZnk1MDA1cHNi', 's010e04': 'https://kuklink.com/1/bnYyZnk1MDA0M2Np', 's010e05': 'https://kuklink.com/1/bnYyZnk1MDAzang2', 's010e06': 'https://kuklink.com/1/bnYyZnk1MDAzaGZk', 's010e07': 'https://kuklink.com/1/bnYyZnk1MDAwbWs1', 's010e08': 'https://kuklink.com/1/bnYyZnk1MDA0dDEx', 's010e09': 'https://kuklink.com/1/bnYyZnk1MDAyZ3Y0', 's010e10': 'https://kuklink.com/1/bnYyZnk1MDAzcnpq', 's010e11': 'https://kuklink.com/1/bnYyZnk1MDAzZTVs', 's010e12': 'https://kuklink.com/1/bnYyZnk1MDAyMHVw',
          's010e13': 'https://kuklink.com/1/bnYyZnk1MDAzYWdh', 's01e14': 'https://kuklink.com/1/bnYyZnk1MDAxcTM3', 's010e15': 'https://kuklink.com/1/bnYyZnk1MDA0bG9t', 's010e16': 'https://kuklink.com/1/bnYyZnk1MDAxYzR1', 's010e17': 'https://kuklink.com/1/bnYyZnk1MDA1cnZh', 's010e18': 'https://kuklink.com/1/bnYyZnk1MDA1cnZh'}



def send_message(url, chat_id, message):
    if message == 'hi':
        reply = "How u doin'😉"
        send = requests.post(url+'sendMessage?chat_id=' +
                             str(chat_id)+'&text='+reply)
        print(send)
        # return send
        
#start 
    elif message =='/start':
        reply ='''Hola! Iam a Bot here is the list of things u can do here
                1.Download the most amazing sitcom ever , Yeah the F.R.I.E.N.D.S.(Enter the command 'download' to get the any episode)
                2.if u already know the names of the characters enter any name and i will tell u briefly about them.
                3.You wnna hear some special lines of the F.R.I.E.N.D.S name the character i will give you thier most iconic line. 
                4.And lastly to know about the developers who made me type info)'''
        send = requests.post(url+'sendMessage?chat_id=' + str(chat_id)+'&text='+reply)

#info
    elif message == 'info':
        reply = '''
       Hey there! we are one of the biggest fans of the sitcom F.R.I.E.N.D.S so we wanted to make this available for all people so they can watch like us and enjoy
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
    elif message in dict4.keys():
        reply = dict4[message] 
        send = requests.post(url+'sendMessage?chat_id=' +
                             str(chat_id)+'&text='+reply)

    elif message in dict5.keys():
        reply = dict5[message]
        send = requests.post(url+'sendMessage?chat_id=' +
                             str(chat_id)+'&text='+reply)

    elif message in dict6.keys():
        reply = dict6[message]
        send = requests.post(url+'sendMessage?chat_id=' +
                             str(chat_id)+'&text='+reply)
    elif message in dict7.keys():
        reply = dict7[message] 
        send = requests.post(url+'sendMessage?chat_id=' +
                             str(chat_id)+'&text='+reply)

    elif message in dict8.keys():
        reply = dict9[message]
        send = requests.post(url+'sendMessage?chat_id=' +
                             str(chat_id)+'&text='+reply)

    elif message in dict9.keys():
        reply = dict9[message]
        send = requests.post(url+'sendMessage?chat_id=' +
                             str(chat_id)+'&text='+reply)
    elif message in dict10.keys():
        reply = dict10[message] 
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
