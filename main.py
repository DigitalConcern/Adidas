import uiautomator2 as u2
import data as dd
import cash_wipe as cc
import gps_red as gps
import proxy_red as pp
import adidass_reg as aa
import adidas_ext as ee

plist = []
posts = []
addresses = []
fullnames = []
telephones = []
cards = []
d = u2.connect()
ACCOUNTS = 10
phone = {
    'id': 'null',
    'number': 'null',
    'code': ''
}

file = open('UsListLog.txt', 'w+')
for turn in range(ACCOUNTS):
    ee.adidas_ext(d)
    cc.cash_wipe(d)

    prox_usr = dd.proxy(plist)
    pp.proxy_red(d, prox_usr, turn)

    gps.gps_red(d, turn)

    user = dd.data(posts, addresses, fullnames, phone, cards)
    file.write(str(user) + '\n')
    print(turn, " ", user)
    aa.adidas_reg(d, user, phone, turn)

file.close()
