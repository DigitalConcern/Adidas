import uiautomator2 as u2
import data as dd
import cash_wipe as cc
import gps_red as gps
import proxy_red as pp
import adidass_reg as aa
import adidass_reg_no_kb as ab
import adidas_ext as ee
import keyboard as kk

shoe = 'YEEZY BOOST 700'

plist = []
posts = []
addresses = []
fullnames = []
telephones = []
cards = []
d = u2.connect()
ACCOUNTS = 50
phone = {
    'id': 'null',
    'number': 'null',
    'code': ''
}

file = open('UsListLog.txt', 'w+')
for turn in range(ACCOUNTS):
    ee.adidas_ext(d)
    print("Adidas exit")
    user = dd.data(posts, addresses, fullnames, telephones, cards)
    file.write(str(user) + '\n')
    print(turn, " ", user)
    prox_usr = dd.proxy(plist)
    cc.cash_wipe(d)
    print("Cache wiped")
    pp.proxy_red(d, prox_usr, turn)
    print("Proxy redded")
    gps.gps_red(d, turn)
    print("gps redded")
    ab.adidas_reg(d, user, phone, turn, shoe)

file.close()
