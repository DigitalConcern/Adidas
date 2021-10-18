import uiautomator2 as u2
import random as rand
import data as dd
from uiautomator2 import UiObject
import keyboard as kk
import cash_wipe as cc

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
    device.click(rand.randint(599, 650), rand.randint(280, 320))  # ентер проверочного кода
    device.sleep(1)
    device.click(rand.randint(50, 670), rand.randint(980, 1054))  # продолжить с 41 разм
    device.sleep(5)
    #НАЧИНАЕТСЯ ЧЕРНЫЙ ЭКРАН
    device.click(rand.randint(120, 680), rand.randint(595, 690))  #адрес
    device.sleep(1)
    device.click(rand.randint(35, 680), rand.randint(1160, 1240))  #Добавить адрес
    device.sleep(1)
    device.click(rand.randint(66, 350), rand.randint(353, 325))  #имя
    device.sleep(1)
    kk.keyboard_rus("Имя",device)  #Ввод ИМЕНИ
    device.sleep(1)
    device.click(rand.randint(370, 650), rand.randint(300, 325))  #Фамилия
    device.sleep(1)
    kk.keyboard_rus("Фамилия", device)  # Ввод Фамилии
    device.sleep(1)
    device.click(rand.randint(599, 650), rand.randint(265, 320))  # продолжить
    device.sleep(1)
    kk.keyboard_rus("Адрес", device)  # Ввод Адреса
    device.sleep(1)
    device.click(rand.randint(599, 650), rand.randint(350, 400))  # продолжить
    device.sleep(1)
    #Редачим итоговую анкету с адресом\именем
    device.click(rand.randint(66, 650), rand.randint(855, 880))  # кнопка дома
    device.sleep(1)
    kk.keyboard_rus("123", device)  # Ввод дома
    device.sleep(1)
    device.press("back")
    device.click(rand.randint(66, 650), rand.randint(950, 975))  # кнопка квартиры
    device.sleep(1)
    kk.keyboard_rus("123", device)  # Ввод квартиры
    device.sleep(1)
    device.press("back")
    device.click(rand.randint(66, 650), rand.randint(950, 975))  # кнопка города
    device.sleep(1)
    kk.keyboard_rus("Москва", device)  # Ввод города
    device.sleep(1)
    device.press("back")
    device.click(rand.randint(66, 650), rand.randint(950, 975))  # кнопка индекса
    device.sleep(1)
    kk.keyboard_num("1234543", device)  # Ввод индекса
    device.sleep(1)
    device.press("back")
    device.click(rand.randint(66, 650), rand.randint(950, 975))  # кнопка Мобильный телефон
    device.sleep(1)
    kk.keyboard_num("+79771991000", device)  # Ввод телефона
    device.sleep(1)
    device.press("back")
    device.sleep(1)
    device.click(rand.randint(40, 680), rand.randint(1160, 1240))  # кнопка Сохранить
    device.sleep(6)
    device.click(rand.randint(70, 520), rand.randint(850, 1050))  # кнопка Сохранить
    device.sleep(6)
    #Добавление оплаты
    device.click(rand.randint(480, 680), rand.randint(710, 740))  # кнопка выбрать метод оплаты ПРОВЕРИТЬ
    device.sleep(2)
    device.click(rand.randint(70, 650), rand.randint(1175, 1230))  # кнопка выбрать ВИЗА МАСТЕРКАРД МИР
    device.sleep(2)
    device.click(rand.randint(70, 650), rand.randint(305, 330))  # кнопка номер карты
    device.sleep(2)
    kk.keyboard_num("1111222233334444", device)  # Ввод номера карты
    device.sleep(1)
    device.click(rand.randint(70, 650), rand.randint(530, 550))  # кнопка срок
    device.sleep(2)
    kk.keyboard_num("1111222233334444", device)  # Ввод срока
    device.sleep(1)
    device.press("back")
    device.sleep(1)
    device.click(rand.randint(70, 650), rand.randint(305, 330))  # кнопка имя на карте
    device.sleep(2)
    kk.keyboard_rus("ВАЛЕРА", device)  # Ввод имени
    device.sleep(1)
    device.click(rand.randint(70, 650), rand.randint(770, 895))  # кнопка CVV
    device.sleep(2)
    kk.keyboard_num("123", device)  # Ввод CVV
    device.sleep(1)
    device.press("back")
    device.sleep(1)
    device.click(rand.randint(40, 650), rand.randint(1160, 1240))  # кнопка Сохранить карту
    device.sleep(1)
    device.click(rand.randint(40, 650), rand.randint(1160, 1240))  # кнопка подтвердить с таймером
    device.sleep(1)
    device.click(rand.randint(370, 650), rand.randint(766, 850))  # кнопка подтвердить
    device.sleep(1)


    ##device.swipe(rand.randint(30, 680), rand.randint(1148, 1250),rand.randint(30, 680),rand.randint(10, 350))
    cc.cash_wipe(device)

d = u2.connect()
# gps_red(d, 0)
# proxy_red(d, 0)
adidas(d, 0)

