import random as rand
import keyboard as kk
import sms



def adidas_reg(device, user,phons, turn):
    device.press("home")
    device.click(93, 150)  # ADIDAS APP
    device.sleep(10)
    device.click(rand.randint(190, 500), rand.randint(1150, 1215))  # Геоданные
    device.sleep(1)
    device.click(rand.randint(113, 550), rand.randint(672, 750))  # Мужская одежда
    device.sleep(6)
    device.click(rand.randint(59, 620), rand.randint(350, 815))  # убрать уведомление
    device.sleep(1)
    device.click(rand.randint(113, 550), rand.randint(672, 750))  # Нажать на тапок
    device.sleep(1)
    device.click(rand.randint(50, 670), rand.randint(670, 1220))  # принять участие
    device.sleep(1)
    device.click(rand.randint(40, 680), rand.randint(1110, 1210))  # Войди в аккаунт
    device.sleep(1)
    device.click(rand.randint(64, 650), rand.randint(482, 546))  # Емаил
    device.sleep(1)
    kk.keyboard_eng(user('post'), device)  # Ввод емаила
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
    device.click(rand.randint(35, 680), rand.randint(1025, 1120))  # подтвердить аккаунт
    device.sleep(1)

    kk.keyboard_num(sms.telephone_receiver(phons)['number'], device)  # Ввод телефона для пруфа
    device.sleep(1)
    device.click(rand.randint(570, 643), rand.randint(385, 480))  # ентер телефона
    device.sleep(7)
    kk.keyboard_num(sms.code_receiver(phons)['code'], device)  # Ввод ПРОВЕРОЧНОГО КОДА
    device.sleep(1)
    device.click(rand.randint(599, 650), rand.randint(280, 320))  # ентер проверочного кода
    device.sleep(1)
    size = rand.randint(1, 15)
    if size == 1:
        for p in range(6):
            device.click(rand.randint(163, 255), rand.randint(636, 674))
            device.sleep(1)
    if size == 2:
        for p in range(5):
            device.click(rand.randint(163, 255), rand.randint(636, 674))
            device.sleep(1)
    if size == 3:
        for p in range(4):
            device.click(rand.randint(163, 255), rand.randint(636, 674))
            device.sleep(1)
    if size == 4:
        for p in range(3):
            device.click(rand.randint(163, 255), rand.randint(636, 674))
            device.sleep(1)
    if size == 5:
        for p in range(2):
            device.click(rand.randint(163, 255), rand.randint(636, 674))
            device.sleep(1)
    if size == 6:
        for p in range(1):
            device.click(rand.randint(163, 255), rand.randint(636, 674))
            device.sleep(1)
    if size == 8:
        for p in range(1):
            device.click(rand.randint(465, 530), rand.randint(636, 674))
            device.sleep(1)
    if size == 9:
        for p in range(2):
            device.click(rand.randint(465, 530), rand.randint(636, 674))
            device.sleep(1)
    if size == 10:
        for p in range(3):
            device.click(rand.randint(465, 530), rand.randint(636, 674))
            device.sleep(1)
    if size == 11:
        for p in range(4):
            device.click(rand.randint(465, 530), rand.randint(636, 674))
            device.sleep(1)
    if size == 12:
        for p in range(5):
            device.click(rand.randint(465, 530), rand.randint(636, 674))
            device.sleep(1)
    if size == 13:
        for p in range(6):
            device.click(rand.randint(465, 530), rand.randint(636, 674))
            device.sleep(1)
    if size == 14:
        for p in range(7):
            device.click(rand.randint(465, 530), rand.randint(636, 674))
            device.sleep(1)
    if size == 15:
        for p in range(8):
            device.click(rand.randint(465, 530), rand.randint(636, 674))
            device.sleep(1)
    device.sleep(1)
    device.click(rand.randint(50, 670), rand.randint(980, 1054))  # продолжить с 41 разм
    device.sleep(5)
    # НАЧИНАЕТСЯ ЧЕРНЫЙ ЭКРАН
    device.click(rand.randint(120, 680), rand.randint(595, 690))  # адрес
    device.sleep(1)
    device.click(rand.randint(35, 680), rand.randint(1160, 1240))  # Добавить адрес
    device.sleep(1)
    device.click(rand.randint(66, 350), rand.randint(353, 325))  # имя
    device.sleep(1)
    kk.keyboard_rus(user['name'], device)  # Ввод ИМЕНИ
    device.sleep(1)
    device.click(rand.randint(370, 650), rand.randint(300, 325))  # Фамилия
    device.sleep(1)
    kk.keyboard_rus(user['surname'], device)  # Ввод Фамилии
    device.sleep(1)
    device.click(rand.randint(599, 650), rand.randint(265, 320))  # продолжить
    device.sleep(1)
    kk.keyboard_rus(user['street'], device)  # Ввод Адреса
    device.sleep(1)
    device.click(rand.randint(599, 650), rand.randint(350, 400))  # продолжить
    device.sleep(1)
    # Редачим итоговую анкету с адресом\именем
    device.click(rand.randint(66, 650), rand.randint(855, 880))  # кнопка дома
    device.sleep(1)
    kk.keyboard_rus(user['building'], device)  # Ввод дома
    device.sleep(1)
    device.press("back")
    device.click(rand.randint(66, 650), rand.randint(950, 975))  # кнопка квартиры
    device.sleep(1)
    kk.keyboard_rus(user['flat'], device)  # Ввод квартиры
    device.sleep(1)
    device.press("back")
    device.click(rand.randint(66, 650), rand.randint(950, 975))  # кнопка города
    device.sleep(1)
    kk.keyboard_rus(user['city'], device)  # Ввод города
    device.sleep(1)
    device.press("back")
    device.click(rand.randint(66, 650), rand.randint(950, 975))  # кнопка индекса
    device.sleep(1)
    kk.keyboard_num(user['code'], device)  # Ввод индекса
    device.sleep(1)
    device.press("back")
    device.click(rand.randint(66, 650), rand.randint(950, 975))  # кнопка Мобильный телефон
    device.sleep(1)
    kk.keyboard_num("+79777777777777777", device)  # Ввод телефона НОРМ ТЕЛЕФОН С ПЕРЕАДР
    device.sleep(1)
    device.press("back")
    device.sleep(1)
    device.click(rand.randint(40, 680), rand.randint(1160, 1240))  # кнопка Сохранить
    device.sleep(6)
    device.click(rand.randint(70, 520), rand.randint(850, 1050))  # кнопка Сохранить
    device.sleep(6)
    # Добавление оплаты
    device.click(rand.randint(480, 680), rand.randint(710, 740))  # кнопка выбрать метод оплаты ПРОВЕРИТЬ
    device.sleep(2)
    device.click(rand.randint(70, 650), rand.randint(1175, 1230))  # кнопка выбрать ВИЗА МАСТЕРКАРД МИР
    device.sleep(2)
    device.click(rand.randint(70, 650), rand.randint(305, 330))  # кнопка номер карты
    device.sleep(2)
    kk.keyboard_num("1111222233334444", device)  # Ввод номера карты ДОДЕЛАТЬ
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
