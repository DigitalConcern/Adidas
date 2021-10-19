import uiautomator2 as u2
import data as dd
import cash_wipe as cc
import gps_red as gps
import proxy_red as pp
import adidass_reg as aa

plist = []
posts = []
addresses = []
fullnames = []
telephones = []
cards = []
d = u2.connect()
ACCOUNTS = 150
phone = {
    'id': 'null',
    'number': 'null',
    'code': ''
}
file = open('UsListLog.txt','w+')

for turn in range(ACCOUNTS):
    user = dd.data(posts, addresses, fullnames, telephones, cards)
    file.write(str(user)+'\n')
    print(turn, " ", user)
    prox_usr = dd.proxy(plist)
#   cc.cash_wipe(d)
#   pp.proxy_red(d, prox_usr)
#   gps.gps_red(d, turn)
#   aa.adidas_reg(d, user, phone,turn)
file.close()