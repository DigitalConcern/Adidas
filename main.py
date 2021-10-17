import uiautomator2 as u2
import random as rand
import data as dd
from uiautomator2 import UiObject
import keyboard as kk

plist = []
posts = []
addresses = []
fullnames = []
telephones = []
cards = []


def gps_red(device, turn):
    device.press("home")
    device.sleep(1)
    device.click(287, 150)  ##GPS APP
    device.sleep(3)

    intx = rand.randint(81, 610)
    inty = rand.randint(705, 800)
    device.double_click(intx, inty, 0.01)
    device.sleep(1)
    device(index=2, className="android.widget.ImageView").click()
    device.sleep(5)
    device.press("home")


def proxy_red(device, turn):
    device.press("home")
    device.sleep(1)
    device.click(439, 140)  ##Proxy APP
    device.sleep(3)
    device.click(287, 1215)
    device.sleep(1)
    device.swipe(567, 680, 36, 617)
    device.sleep(1)
    device.click(248, 1057)  # wifi
    device.sleep(1)
    device.click(323, 257)  # имя wifi
    device.sleep(1)

    proxy=dd.proxy(plist)

    device.click(328, 652)  # сервер
    device.sleep(1)
    device(className="android.widget.EditText").set_text(proxy['ip'])
    device.sleep(1)
    device.click(575, 558)
    device.sleep(1)

    device.click(351, 789)  # порт
    device.sleep(1)
    device(className="android.widget.EditText").set_text(proxy['port'])
    device.sleep(1)
    device.click(575, 558)
    device.sleep(1)

    device.click(233, 908)  # имя
    device.sleep(1)
    device(className="android.widget.EditText").set_text(proxy["name"])
    device.sleep(1)
    device(index=1, className="android.widget.Button").click()
    device.sleep(1)

    device.click(298, 1062)  # пароль
    device.sleep(1)
    device(className="android.widget.EditText").set_text(proxy["password"])
    device.sleep(1)
    device(index=1, className="android.widget.Button").click()
    device.sleep(1)

    device.sleep(1)
    device.press("back")
    device.sleep(1)
    device.press("back")
    device.swipe(36, 617, 567, 680)
    device.sleep(1)
    device.click(287, 1215)
    device.sleep(5)
    device.press("home")


def cash_wipe(device):
    device.press("home")
    device(text="Настройки").click()
    device.sleep(1)
    device.swipe(350, 1200, 350, 1, 0.1)
    device.swipe(350, 1200, 350, 1, 0.1) # Ищем диспетчер приложений
    device.swipe(350, 1200, 350, 1, 0.1)
    device.sleep(1)
    device.click(89, 591)
    device.sleep(1)
    device.swipe(350, 1200, 350, 1, 0.5) # Ищем Adidas
    device.swipe(350, 1200, 350, 1, 0.5)
    device.sleep(1)
    device.click(89, 591) # Нажимаем Adidas
    device.sleep(1)
    device.swipe(350, 1200, 350, 600, 0.5) # Свайп к кэшу
    device.sleep(1)
    device(text="Очистить данные").click()
    device.sleep(1)
    device(text="Да").click()
    device.sleep(1)
    device.click(596, 689) # Отчистить кэш
    device.sleep(1)
    device.press("home")


def adidas(device, turn):
    user = dd.data(posts, addresses, fullnames, telephones, cards)
    device.press("home")
    device.click(93, 150)  ##ADIDAS APP
    device.sleep(10)
    device.click(rand.randint(190, 500), rand.randint(1150, 1215)) #Геоданные
    device.sleep(1)
    device.click(rand.randint(113, 550), rand.randint(672, 750)) #Мужская одежда
    device.sleep(6)
    device.click(rand.randint(59, 620), rand.randint(350, 815)) #убрать уведомление
    device.sleep(1)
    device.click(rand.randint(113, 550), rand.randint(672, 750)) #Нажать на тапок
    device.sleep(1)
    device.click(rand.randint(50, 670), rand.randint(670, 1220))  #принять участие
    device.sleep(1)
    device.click(rand.randint(40, 680), rand.randint(1110, 1210))  #Войди в аккаунт
    device.sleep(1)
    device.click(rand.randint(64, 650), rand.randint(482, 546))  #Емаил
    device.sleep(1)
    kk.keyboard_eng("EMAIL@KEK.RU",device) #Ввод емаила
    device.sleep(1)
    device.click(rand.randint(577, 649), rand.randint(300, 388))  # Емаил ентер
    device.sleep(1)
    device.click(rand.randint(460, 550), rand.randint(380, 420))  # старше 14
    device.sleep(1)
    device.click(rand.randint(66, 550), rand.randint(353, 386))  # пароль клик
    device.sleep(1)
    kk.keyboard_eng("12345678Ab", device)  # Ввод пароля
    device.sleep(1)
    device.click(rand.randint(35, 680), rand.randint(691, 755))  # пароль ентер
    device.sleep(7)
    device.click(rand.randint(35, 680), rand.randint(1025, 1120))  #подтвердить аккаунт
    device.sleep(1)
    kk.keyboard_num("12345678",device) # Ввод телефона для пруфа
    device.sleep(1)
    device.click(rand.randint(570, 643), rand.randint(385, 480)) #ентер телефона
    device.sleep(7)
    kk.keyboard_num("12345678", device)  # Ввод ПРОВЕРОЧНОГО КОДА
    device.sleep(1)
    device.click(rand.randint(590, 650), rand.randint(280, 320))  # ентер проверочного кода
    device.sleep(1)
    device.click(rand.randint(50, 670), rand.randint(980, 1054))  # продолжить с 41 разм
    device.sleep(5)
    #НАЧИНАЕТСЯ ЧЕРНЫЙ ЭКРАН
    device.click(rand.randint(120, 680), rand.randint(595, 690))  #адрес
    device.sleep(1)
    device.click(rand.randint(35, 680), rand.randint(1160, 1240))  #Добавить адрес
    device.sleep(1)

device.press("home")
    cash_wipe(device)

d = u2.connect()
# gps_red(d, 0)
# proxy_red(d, 0)
adidas(d, 0)

