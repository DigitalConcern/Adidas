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
    device.sleep(6)

    device.click(rand.randint(185, 240), rand.randint(1195, 1250))
    print('Поиск')
    device.sleep(1)

    device.click(rand.randint(42, 100), rand.randint(1195, 1250))
    print('дропы')
    device.sleep(1)

    while not device(text='YEEZY BOOST 350 V2').exists:
        device.sleep(1)

    device.click(rand.randint(185, 240), rand.randint(1195, 1250))
    print('Поиск')
    device.sleep(1)

    device.click(rand.randint(42, 100), rand.randint(1195, 1250))
    print('дропы')
    device.sleep(1)

    while not device(text='YEEZY BOOST 350 V2').exists:
        device.sleep(3)
    device.sleep(2)
    device.click(rand.randint(113, 550), rand.randint(672, 750))
    print('Нажать на тапок')

    device.sleep(2)

    while not device(className='android.widget.Button').exists:
        device.sleep(1)
        # device.click(rand.randint(113, 550), rand.randint(672, 750))
        # print('Нажать на тапок')
    device.sleep(2)
    device.click(rand.randint(50, 670), rand.randint(1130, 1220))
    print(' принять участие')

    device.sleep(2)

    while not device(className='android.widget.Button').exists:
        device.sleep(1)
        # device.click(rand.randint(50, 670), rand.randint(1130, 1220))
        # print(' принять участие')
    device.sleep(2)
    device.click(rand.randint(40, 680), rand.randint(1110, 1210))
    print('Войди в аккаунт')
    device.sleep(2)

    while not device(text='Email').exists:
        device.sleep(1)
    device.sleep(2)
    device.click(rand.randint(76, 519), rand.randint(510, 520))

    print(' Емаил')
    device.sleep(3)
    kk.keyboard_eng(user['post'], device)
    print('Ввод емаила')
    device.sleep(2)
    device.click(rand.randint(600, 649), rand.randint(330, 375))
    device.sleep(4)
    try:
        device.press(text="ОК")
        device.sleep(30)
    except:
        pass
    print(' Емаил ентер')
    device.sleep(20)
    device.click(rand.randint(460, 550), rand.randint(380, 420))
    print('старше 14')
    device.sleep(5)
    device.click(rand.randint(70, 250), rand.randint(360, 380))
    print(' пароль клик')
    device.sleep(2)
    kk.keyboard_eng("12345678Ab", device)
    print('Ввод пароля')
    device.sleep(5)
    device.click(rand.randint(35, 680), rand.randint(691, 755))
    try:
        device.press(text="ОК")
        device.sleep(30)
    except:
        pass
    print(' пароль ентер')
    device.sleep(10)
    device.click(rand.randint(35, 680), rand.randint(1025, 1120))
    print('подтвердить аккаунт')
    device.sleep(2)

    sms.telephone_receiver(phons)
    device.sleep(8)
    kk.keyboard_num(phons['number'], device)
    print(' Ввод телефона для пруфа')
    device.sleep(2)
    device.click(rand.randint(600, 643), rand.randint(420, 450))
    print(' ентер телефона')
    device.sleep(8)
    sms.code_receiver(phons)
    if phons['code'] == "STATUS_WAIT_CODE":
        while phons['code'] == "STATUS_WAIT_CODE":
            device.press("back")
            device.press("back")
            device(className='android.widget.EditText').set_text('')
            sms.telephone_receiver(phons)
            device.sleep(8)
            kk.keyboard_num(phons['number'], device)
            print(' Ввод телефона для пруфа')
            device.sleep(2)
            device.click(rand.randint(600, 643), rand.randint(420, 450))
            print(' ентер телефона')
            device.sleep(8)
            sms.code_receiver(phons)
        kk.keyboard_num(phons['code'], device)
        print(' Ввод ПРОВЕРОЧНОГО КОДА')
    else:
        kk.keyboard_num(phons['code'], device)
        print(' Ввод ПРОВЕРОЧНОГО КОДА')
    device.sleep(2)
    device.click(rand.randint(599, 650), rand.randint(280, 320))
    print(' ентер проверочного кода')

    device.sleep(9)
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
    device.sleep(10)
    device.click(rand.randint(50, 670), rand.randint(980, 1054))
    print('продолжить с разм')
    device.sleep(3)

    while not device(className='android.widget.Button', enabled='false').exists:
        device.sleep(1)

    # НАЧИНАЕТСЯ ЧЕРНЫЙ ЭКРАН
    device.click(rand.randint(120, 680), rand.randint(595, 690))
    print('адрес')
    device.sleep(3)

    while not device(className='android.widget.Button', enabled='true').exists:
        device.sleep(1)
    device.sleep(2)

    device.click(rand.randint(35, 680), rand.randint(1160, 1240))
    print('Добавить адрес')
    device.sleep(3)
    device.click(rand.randint(66, 300), rand.randint(300, 325))
    print('имя')
    device.sleep(3)
    kk.keyboard_rus(user['name'], device)
    print('Ввод ИМЕНИ')
    device.sleep(3)
    device.click(rand.randint(370, 500), rand.randint(300, 325))
    print('Фамилия')
    device.sleep(3)
    kk.keyboard_rus(user['surname'], device)
    print('Ввод Фамилии')
    device.sleep(3)
    device.click(rand.randint(599, 650), rand.randint(265, 320))
    print('продолжить')
    device.sleep(10)
    kk.keyboard_rus(user['street'], device)
    print('Ввод Адреса')
    device.sleep(3)
    device.click(rand.randint(599, 650), rand.randint(350, 400))
    print('продолжить')
    device.sleep(6)
    # Редачим итоговую анкету с адресом\именем
    device.click(rand.randint(66, 650), rand.randint(855, 880))
    print('кнопка дома')
    device.sleep(3)
    kk.keyboard_eng(user['building'], device)
    print('Ввод дома')
    device.sleep(3)
    device.press("back")
    device.sleep(3)
    device.click(rand.randint(66, 650), rand.randint(950, 975))
    print('кнопка квартиры')
    device.sleep(3)
    kk.keyboard_rus(user['flat'], device)
    print('Ввод квартиры')
    device.sleep(1)
    device.press("back")
    device.sleep(3)
    device.click(rand.randint(66, 650), rand.randint(950, 975))
    print('кнопка города')
    device.sleep(3)
    kk.keyboard_rus(user['city'], device)
    print('Ввод города')
    device.sleep(3)
    device.press("back")
    device.sleep(3)
    device.click(rand.randint(66, 650), rand.randint(950, 975))
    print('кнопка индекса')
    device.sleep(3)
    kk.keyboard_num(user['code'], device)
    print('Ввод индекса')
    device.sleep(1)
    device.press("back")
    device.sleep(3)
    device.click(rand.randint(66, 650), rand.randint(950, 975))
    print('кнопка Мобильный телефон')
    device.sleep(3)
    kk.keyboard_num("+79776543035", device)
    print('Ввод телефона НОРМ ТЕЛЕФОН С ПЕРЕАДР')
    device.sleep(3)
    device.press("back")
    device.sleep(3)
    device.click(rand.randint(40, 680), rand.randint(1160, 1240))
    print(' кнопка Сохранить')
    device.sleep(12)
    device.click(rand.randint(75, 400), rand.randint(900, 1000))
    print(' выбрать адрес')
    device.sleep(2)

    while not device(className='android.widget.Button', enabled='false').exists:
        device.sleep(1)
    device.sleep(2)

    # Добавление оплаты
    device.click(rand.randint(480, 680), rand.randint(860, 890))
    print(' кнопка выбрать метод оплаты')
    device.sleep(3)
    device.click(rand.randint(70, 500), rand.randint(1175, 1230))
    print(' кнопка выбрать ВИЗА МАСТЕРКАРД МИР')
    device.sleep(3)
    device.click(rand.randint(70, 650), rand.randint(305, 330))
    print(' кнопка номер карты')
    device.sleep(3)
    kk.keyboard_num("5536913992523155", device)
    print('Ввод номера карты ДОДЕЛАТЬ')
    device.sleep(3)
    device.click(rand.randint(70, 650), rand.randint(530, 550))
    print(' кнопка срок')
    device.sleep(3)
    kk.keyboard_num("06", device)
    device.sleep(3)
    kk.keyboard_num("29", device)
    print(' Ввод срока')
    device.sleep(3)
    device.press("back")
    device.sleep(3)
    device.click(rand.randint(70, 650), 625)
    print('кнопка имя на карте')
    device.sleep(3)
    kk.keyboard_eng("Denis Babkin", device)
    print('Ввод имени')
    device.sleep(3)
    device.press("back")
    device.sleep(3)
    device.click(rand.randint(70, 650), rand.randint(770, 895))
    print('кнопка CVV')
    device.sleep(3)
    kk.keyboard_num("892", device)
    print(' Ввод CVV')
    device.sleep(3)
    device.press("back")
    device.sleep(5)
    device.click(rand.randint(40, 650), rand.randint(1160, 1240))
    print('кнопка Сохранить карту')
    device.sleep(5)

    while not device(className='android.widget.Button', enabled='true'):
        device.sleep(1)
    device.sleep(5)

    device.click(rand.randint(40, 650), rand.randint(1160, 1240))
    print('кнопка подтвердить с таймером')
    device.sleep(5)

    device.click(rand.randint(370, 650), rand.randint(766, 850))
    print('кнопка подтвердить')
    device.sleep(7)

