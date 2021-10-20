import random as rand
import keyboard as kk
import sms


def adidas_reg(device, user, phons, turn):
    device.press("home")
    device.click(93, 150)  # ADIDAS APP
    device.sleep(15)
    device.click(rand.randint(190, 500), rand.randint(1150, 1215))
    print('Геоданные')
    device.sleep(2)
    device.click(rand.randint(113, 550), rand.randint(672, 750))
    print('Мужская одежда')
    device.sleep(5)

    device.click(rand.randint(185, 240), rand.randint(1195, 1250))
    print('Поиск')
    device.sleep(1)

    device.click(rand.randint(42, 100), rand.randint(1195, 1250))
    print('дропы')
    device.sleep(5)

    device.click(rand.randint(185, 240), rand.randint(1195, 1250))
    print('Поиск')
    device.sleep(1)

    device.click(rand.randint(42, 100), rand.randint(1195, 1250))
    print('дропы')
    device.sleep(5)

    device.click(rand.randint(113, 550), rand.randint(672, 750))
    print('Нажать на тапок')
    device.sleep(5)
    device.click(rand.randint(50, 670), rand.randint(1130, 1220))
    print(' принять участие')
    device.sleep(3)
    device.click(rand.randint(40, 680), rand.randint(1110, 1210))
    print('Войди в аккаунт')
    device.sleep(3)
    device.click(rand.randint(70, 650), rand.randint(490, 540))
    print(' Емаил')
    device.sleep(5)
    kk.keyboard_eng(user['post'], device)
    print('Ввод емаила')
    device.sleep(2)
    device.click(rand.randint(600, 649), rand.randint(330, 375))
    print(' Емаил ентер')
    device.sleep(8)
    device.click(rand.randint(460, 550), rand.randint(380, 420))
    print('старше 14')
    device.sleep(8)
    device.click(rand.randint(66, 550), rand.randint(353, 386))
    print(' пароль клик')
    device.sleep(2)
    kk.keyboard_eng("12345678Ab", device)
    print('Ввод пароля')
    device.sleep(5)
    device.click(rand.randint(35, 680), rand.randint(691, 755))
    print(' пароль ентер')
    device.sleep(10)
    device.click(rand.randint(35, 680), rand.randint(1025, 1120))
    print('подтвердить аккаунт')
    device.sleep(2)


    sms.telephone_receiver(phons)
    device.sleep(2)
    kk.keyboard_num(phons['number'], device)
    print(' Ввод телефона для пруфа')
    device.sleep(2)
    device.click(rand.randint(600, 643), rand.randint(420, 450))
    print(' ентер телефона')
    device.sleep(5)
    sms.code_receiver(phons)
    if (phons['code'] == "STATUS_WAIT_CODE"):
        device.press("home")
        exit(1)    
    device.sleep(2)


    kk.keyboard_num(phons['code'], device)
    print(' Ввод ПРОВЕРОЧНОГО КОДА')
    device.sleep(2)
    device.click(rand.randint(599, 650), rand.randint(280, 320))
    print(' ентер проверочного кода')
    device.sleep(8)
    size = rand.randint(1, 15)
    if size == 1:
        for p in range(6):
            device.click(rand.randint(163, 255), rand.randint(636, 674))
            device.sleep(3)
    if size == 2:
        for p in range(5):
            device.click(rand.randint(163, 255), rand.randint(636, 674))
            device.sleep(3)
    if size == 3:
        for p in range(4):
            device.click(rand.randint(163, 255), rand.randint(636, 674))
            device.sleep(3)
    if size == 4:
        for p in range(3):
            device.click(rand.randint(163, 255), rand.randint(636, 674))
            device.sleep(3)
    if size == 5:
        for p in range(2):
            device.click(rand.randint(163, 255), rand.randint(636, 674))
            device.sleep(3)
    if size == 6:
        for p in range(1):
            device.click(rand.randint(163, 255), rand.randint(636, 674))
            device.sleep(3)
    if size == 8:
        for p in range(1):
            device.click(rand.randint(465, 530), rand.randint(636, 674))
            device.sleep(3)
    if size == 9:
        for p in range(2):
            device.click(rand.randint(465, 530), rand.randint(636, 674))
            device.sleep(3)
    if size == 10:
        for p in range(3):
            device.click(rand.randint(465, 530), rand.randint(636, 674))
            device.sleep(3)
    if size == 11:
        for p in range(4):
            device.click(rand.randint(465, 530), rand.randint(636, 674))
            device.sleep(3)
    if size == 12:
        for p in range(5):
            device.click(rand.randint(465, 530), rand.randint(636, 674))
            device.sleep(3)
    if size == 13:
        for p in range(6):
            device.click(rand.randint(465, 530), rand.randint(636, 674))
            device.sleep(3)
    if size == 14:
        for p in range(7):
            device.click(rand.randint(465, 530), rand.randint(636, 674))
            device.sleep(3)
    if size == 15:
        for p in range(8):
            device.click(rand.randint(465, 530), rand.randint(636, 674))
            device.sleep(3)
    device.sleep(5)
    device.click(rand.randint(50, 670), rand.randint(980, 1054))  # продолжить с разм
    device.sleep(10)
    # НАЧИНАЕТСЯ ЧЕРНЫЙ ЭКРАН
    device.click(rand.randint(120, 680), rand.randint(595, 690))  # адрес
    device.sleep(3)
    device.click(rand.randint(35, 680), rand.randint(1160, 1240))  # Добавить адрес
    device.sleep(3)
    device.click(rand.randint(66, 300), rand.randint(300, 325))  # имя
    device.sleep(3)
    kk.keyboard_rus(user['name'], device,1,1)  # Ввод ИМЕНИ
    device.sleep(3)
    device.click(rand.randint(370, 500), rand.randint(300, 325))  # Фамилия
    device.sleep(3)
    kk.keyboard_rus(user['surname'], device,0,1)  # Ввод Фамилии
    device.sleep(3)
    device.click(rand.randint(599, 650), rand.randint(265, 320))  # продолжить
    device.sleep(10)
    kk.keyboard_rus(user['street'], device,0,1)  # Ввод Адреса
    device.sleep(3)
    device.click(rand.randint(599, 650), rand.randint(350, 400))  # продолжить
    device.sleep(6)
    # Редачим итоговую анкету с адресом\именем
    device.click(rand.randint(66, 650), rand.randint(855, 880))  # кнопка дома
    device.sleep(3)
    kk.keyboard_rus(user['building'], device,0,1)  # Ввод дома
    device.sleep(3)
    device.press("back")
    device.sleep(3)
    device.click(rand.randint(66, 650), rand.randint(950, 975))  # кнопка квартиры
    device.sleep(3)
    kk.keyboard_rus(user['flat'], device,0,1)  # Ввод квартиры
    device.sleep(1)
    device.press("back")
    device.sleep(3)
    device.click(rand.randint(66, 650), rand.randint(950, 975))  # кнопка города
    device.sleep(3)
    kk.keyboard_rus(user['city'], device,0,1)  # Ввод города
    device.sleep(3)
    device.press("back")
    device.sleep(3)
    device.click(rand.randint(66, 650), rand.randint(950, 975))  # кнопка индекса
    device.sleep(3)
    kk.keyboard_num(user['code'], device)  # Ввод индекса
    device.sleep(1)
    device.press("back")
    device.sleep(3)
    device.click(rand.randint(66, 650), rand.randint(950, 975))  # кнопка Мобильный телефон
    device.sleep(3)
    kk.keyboard_num("+79776543035", device)  # Ввод телефона НОРМ ТЕЛЕФОН С ПЕРЕАДР
    device.sleep(3)
    device.press("back")
    device.sleep(3)
    device.click(rand.randint(40, 680), rand.randint(1160, 1240))  # кнопка Сохранить
    device.sleep(25)
    device.click(rand.randint(70, 520), rand.randint(850, 1050))  # выбрать адрес
    device.sleep(6)
    # Добавление оплаты
    device.click(rand.randint(480, 680), rand.randint(710, 740))  # кнопка выбрать метод оплаты ПРОВЕРИТЬ
    device.sleep(3)
    device.click(rand.randint(70, 650), rand.randint(1175, 1230))  # кнопка выбрать ВИЗА МАСТЕРКАРД МИР
    device.sleep(3)
    device.click(rand.randint(70, 650), rand.randint(305, 330))  # кнопка номер карты
    device.sleep(3)
    kk.keyboard_num("5536913992523155", device)  # Ввод номера карты ДОДЕЛАТЬ
    device.sleep(3)
    device.click(rand.randint(70, 650), rand.randint(530, 550))  # кнопка срок
    device.sleep(3)
    kk.keyboard_num("0629", device)  # Ввод срока
    device.sleep(3)
    device.press("back")
    device.sleep(3)
    device.click(rand.randint(70, 650), rand.randint(305, 330))  # кнопка имя на карте
    device.sleep(3)
    kk.keyboard_eng("Denis Babkin", device)  # Ввод имени
    device.sleep(3)
    device.click(rand.randint(70, 650), rand.randint(770, 895))  # кнопка CVV
    device.sleep(3)
    kk.keyboard_num("892", device)  # Ввод CVV
    device.sleep(3)
    device.press("back")
    device.sleep(3)
    device.click(rand.randint(40, 650), rand.randint(1160, 1240))  # кнопка Сохранить карту
    device.sleep(3)
    device.click(rand.randint(40, 650), rand.randint(1160, 1240))  # кнопка подтвердить с таймером
    device.sleep(3)
    device.click(rand.randint(370, 650), rand.randint(766, 850))  # кнопка подтвердить
    device.sleep(3)
    device.sleep(2)
