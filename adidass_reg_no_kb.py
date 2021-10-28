import random as rand
import keyboard as kk
import sms


def adidas_reg(device, user, phons, turn, model):
    device.sleep(1)
    device.press("home")
    device.sleep(1)
    device.click(93, 150)  # ADIDAS APP

    while not device(resourceId='com.adidas.app:id/requestLocationPermissionImage').exists:
        device.sleep(0.5)
    device.sleep(1)
    device.click(rand.randint(190, 500), rand.randint(1150, 1215))
    print('Геоданные')
    device.sleep(1)
    device.click(rand.randint(113, 550), rand.randint(672, 750))
    print('Мужская одежда')
    device.sleep(0.5)

    device.click(rand.randint(113, 550), rand.randint(672, 750))
    device.sleep(5)

    device.click(rand.randint(185, 240), rand.randint(1195, 1250))
    print('Поиск')
    device.sleep(1)

    device.click(rand.randint(42, 100), rand.randint(1195, 1250))
    print('дропы')
    device.sleep(1)

    while not device(text=model).exists:
        device.sleep(0.1)
    device.sleep(1)
    device.click(rand.randint(185, 240), rand.randint(1195, 1250))
    print('Поиск')
    device.sleep(0.5)

    device.click(rand.randint(42, 100), rand.randint(1195, 1250))
    print('дропы')
    device.sleep(0.5)

    while not device(text=model).exists:
        device.sleep(0.1)
    device.sleep(0.5)
    device.click(rand.randint(113, 550), rand.randint(672, 750))
    print('Нажать на тапок')

    device.sleep(0.5)

    while not device(resourceId='com.adidas.app:id/adidasStatefulInternalButton', clickable='true').exists:
        device.sleep(0.1)
        # device.click(rand.randint(113, 550), rand.randint(672, 750))
        # print('Нажать на тапок')
    device.sleep(1)
    device.click(rand.randint(50, 670), rand.randint(1130, 1220))
    print('принять участие')

    while not device(resourceId='com.adidas.app:id/btnRequirementsEnable').exists:
        device.sleep(0.1)
        # device.click(rand.randint(50, 670), rand.randint(1130, 1220))
        # print(' принять участие')
    device.sleep(0.5)
    device.click(rand.randint(40, 680), rand.randint(1130, 1210))
    print('Войди в аккаунт')
    device.sleep(0.5)

    while not device(text='Email').exists:
        device.sleep(0.1)
    device.sleep(0.5)
    device.click(rand.randint(76, 519), rand.randint(510, 520))

    print(' Емаил')
    device.sleep(0.5)

    # kk.keyboard_eng(user['post'], device)
    # device(text='Email', className='android.widget.EditText').press
    device(text='Email', className='android.widget.EditText').set_text(user['post'])

    print('Ввод емаила')
    device.sleep(0.5)
    device.click(rand.randint(600, 649), rand.randint(330, 375))
    while not device(resourceId='com.adidas.app:id/selectableItemText').exists:
        device.sleep(0.1)
        try:
            device(text="OK").click()
            device.sleep(30)
            device.click(rand.randint(600, 649), rand.randint(330, 375))
        except:
            pass
    print('Емаил ентер')
    # while not device(resourceId='com.adidas.app:id/formFieldTitleView').exists:
    #     device.sleep(0.1)
    device.sleep(0.5)
    device.click(rand.randint(366, 480), rand.randint(360, 380))
    print('Cтарше 14')
    while not device(className='android.widget.EditText').exists:
        device.sleep(0.1)
    device.sleep(0.5)

    # device.click(rand.randint(70, 250), rand.randint(360, 380))
    # print('Пароль клик')
    # device.sleep(1)

    # kk.keyboard_eng("12345678Ab", device)
    device(className='android.widget.EditText').set_text("12345678Ab")

    print('Ввод пароля')
    device.sleep(1)
    device.click(rand.randint(35, 680), rand.randint(691, 755))
    # while device(resourceId='com.adidas.app:id/formFieldGuidance').exists:
    # device.sleep(1)
    while not device(resourceId='com.adidas.app:id/tvRequirementsStepContent').exists:
        device.sleep(0.1)
        try:
            device(text="OK").click()
            device.sleep(30)
            device.click(rand.randint(35, 680), rand.randint(691, 755))
        except:
            pass
    device.sleep(0.5)
    print(' пароль ентер')
    while not device(resourceId='com.adidas.app:id/btnRequirementsEnable').exists:
        device.sleep(0.1)
    device.sleep(0.5)
    device.click(rand.randint(40, 600), rand.randint(1030, 1110))
    print('подтвердить аккаунт')

    while not device(resourceId='com.adidas.app:id/formSubtitle').exists:  # Подзаголовок экрана с телефоном
        device.sleep(0.1)
    device.sleep(0.5)
    sms.telephone_receiver(phons)
    device.sleep(0.5)

    # kk.keyboard_num(phons['number'], device)
    device(className='android.widget.EditText').set_text(phons['number'])

    print(' Ввод телефона для пруфа')
    device.sleep(0.5)
    device.click(rand.randint(600, 643), rand.randint(430, 450))
    print(' ентер телефона')
    timer = 0
    while device(resourceId='com.adidas.app:id/formSubtitle').exists:
        device.sleep(0.1)
        if device(resourceId='com.adidas.app:id/alertDialogMessage').exists:
            timer = timer + 1
            if (timer % 10) == 0:
                print("Prepare for restart")
            if timer == 20:
                device(text="OK").click()
                return 0

    device.sleep(1)
    sms.code_receiver(phons)
    if phons['code'] == "STATUS_WAIT_CODE":
        while phons['code'] == "STATUS_WAIT_CODE":
            device.press("back")
            device.press("back")
            while not device(resourceId='com.adidas.app:id/formSubtitle').exists:  # Подзаголовок экрана с телефоном
                device.sleep(0.1)
            device(className='android.widget.EditText').set_text('')
            sms.telephone_receiver(phons)
            device.sleep(3)
            device.click(rand.randint(75, 600), rand.randint(430, 450))
            device.sleep(1)

            # kk.keyboard_num(phons['number'], device)
            device(className='android.widget.EditText').set_text(phons['number'])

            print(' Ввод телефона для пруфа')
            device.sleep(2)
            device.click(rand.randint(600, 643), rand.randint(430, 450))
            print(' ентер телефона')
            while device(resourceId='com.adidas.app:id/formSubtitle').exists:
                device.sleep(0.1)
            device.sleep(1)
            sms.code_receiver(phons)

        # kk.keyboard_num(phons['code'], device)
        device(className='android.widget.EditText').set_text(phons['code'])

        print(' Ввод ПРОВЕРОЧНОГО КОДА')
    else:
        # kk.keyboard_num(phons['code'], device)
        device(className='android.widget.EditText').set_text(phons['code'])

        print(' Ввод ПРОВЕРОЧНОГО КОДА')
    device.sleep(2)
    device.click(rand.randint(599, 650), rand.randint(280, 320))
    print(' ентер проверочного кода')
    ass = 0
    while not device(resourceId='com.adidas.app:id/fittingLayout').exists:
        device.sleep(1)
        if (ass % 10) == 0:
            print("Prepare for full restart")
        ass = ass + 1
        if ass == 20 and device(className='android.widget.Button', enabled='true').exists and device(
                resourceId='com.adidas.app:id/alertDialogMessage').exists:
            device(text="OK").click()
            return 0

    # device.sleep(1)
    # size = rand.randint(1, 15)
    # if size == 1:
    #    for p in range(6):
    #        device.click(rand.randint(163, 255), rand.randint(636, 674))
    #        device.sleep(1)
    # if size == 2:
    #    for p in range(5):
    #        device.click(rand.randint(163, 255), rand.randint(636, 674))
    #        device.sleep(1)
    # if size == 3:
    #    for p in range(4):
    #        device.click(rand.randint(163, 255), rand.randint(636, 674))
    #        device.sleep(1)
    # if size == 4:
    #    for p in range(3):
    #       device.click(rand.randint(163, 255), rand.randint(636, 674))
    #       device.sleep(1)
    # if size == 5:
    #    for p in range(2):
    #        device.click(rand.randint(163, 255), rand.randint(636, 674))
    #        device.sleep(1)
    # if size == 6:
    #    for p in range(1):
    #        device.click(rand.randint(163, 255), rand.randint(636, 674))
    #        device.sleep(1)
    # if size == 8:
    #    for p in range(1):
    #        device.click(rand.randint(465, 530), rand.randint(636, 674))
    #        device.sleep(1)
    # if size == 9:
    #    for p in range(2):
    #        device.click(rand.randint(465, 530), rand.randint(636, 674))
    #        device.sleep(1)
    # if size == 10:
    #    for p in range(3):
    #        device.click(rand.randint(465, 530), rand.randint(636, 674))
    #        device.sleep(1)
    # if size == 11:
    #    for p in range(4):
    #        device.click(rand.randint(465, 530), rand.randint(636, 674))
    #        device.sleep(1)
    # if size == 12:
    #    for p in range(5):
    #        device.click(rand.randint(465, 530), rand.randint(636, 674))
    #        device.sleep(1)
    # if size == 13:
    #    for p in range(6):
    #        device.click(rand.randint(465, 530), rand.randint(636, 674))
    #        device.sleep(1)
    # if size == 14:
    #    for p in range(7):
    #        device.click(rand.randint(465, 530), rand.randint(636, 674))
    #        device.sleep(1)
    # if size == 15:
    #    for p in range(8):
    #        device.click(rand.randint(465, 530), rand.randint(636, 674))
    #        device.sleep(1)
    device.sleep(0.5)
    device.click(rand.randint(50, 670), rand.randint(980, 1054))
    print('продолжить с разм')

    while not device(resourceId='com.adidas.app:id/termsText').exists:
        device.sleep(0.1)
    device.sleep(0.5)

    # НАЧИНАЕТСЯ ЧЕРНЫЙ ЭКРАН
    device.click(rand.randint(120, 680), rand.randint(595, 690))
    print('адрес')

    while not device(resourceId='com.adidas.app:id/addAddress').exists:
        device.sleep(0.1)
    device.sleep(1)

    device.click(rand.randint(35, 680), rand.randint(1160, 1240))
    print('Добавить адрес')
    while not device(resourceId='com.adidas.app:id/leftField').exists:
        device.sleep(0.1)
    device.sleep(0.5)
    # device.click(rand.randint(66, 300), rand.randint(300, 325))
    print('имя')
    # device.sleep(2)
    device(resourceId='com.adidas.app:id/leftField').set_text(user['name'])
    # kk.keyboard_rus(user['name'], device)
    print('Ввод ИМЕНИ')
    # device.sleep(2)
    # device.click(rand.randint(370, 500), rand.randint(300, 325))
    print('Фамилия')
    # device.sleep(2)
    device(resourceId='com.adidas.app:id/rightField').set_text(user['surname'])
    print('Ввод Фамилии')
    device.sleep(0.5)
    device.click(rand.randint(599, 650), rand.randint(265, 320))
    print('продолжить')
    while not device(resourceId='com.adidas.app:id/autoCompleteSearchField').exists:
        device.sleep(0.1)
    device.sleep(0.5)
    device(resourceId='com.adidas.app:id/adidasInputFieldContentView').set_text(user['street'])

    # kk.keyboard_rus(user['street'], device)
    print('Ввод Адреса')
    while not device(resourceId='com.adidas.app:id/formFieldActionContainer').exists:
        device.sleep(0.1)
    device.sleep(0.5)
    device.click(rand.randint(599, 650), rand.randint(350, 400))
    print('продолжить')
    while not device(index=6, className='android.widget.LinearLayout').exists:
        device.sleep(0.1)
    device.sleep(0.5)
    # Редачим итоговую анкету с адресом\именем
    device.click(rand.randint(70, 600), rand.randint(855, 880))
    print('кнопка дома')
    device.sleep(0.5)
    device.press("back")
    device.sleep(0.5)
    device(index=3, className='android.widget.LinearLayout').child(className='android.widget.EditText').set_text(user['building'])
    # kk.keyboard_rus(user['building'], device)
    print('Ввод дома')
    device.sleep(0.5)
    device(index=4, className='android.widget.LinearLayout').click()
    # device.click(rand.randint(70, 600), rand.randint(960, 985))
    print('кнопка квартиры')
    device.sleep(0.5)
    device.press("back")
    device.sleep(0.5)
    device(index=4,className='android.widget.LinearLayout').child(className='android.widget.EditText').set_text(user['flat'])
    # kk.keyboard_rus(user['flat'], device)
    print('Ввод квартиры')
    device.sleep(0.5)
    device(index=5, className='android.widget.LinearLayout').click()
    # device.click(rand.randint(70, 600), rand.randint(960, 985))
    print('кнопка города')
    device.sleep(0.5)
    device.press("back")
    device.sleep(0.5)
    device(index=5, className='android.widget.LinearLayout').child(className='android.widget.EditText').set_text(user['city'])
    # kk.keyboard_rus(user['city'], device)
    print('Ввод города')
    device.sleep(0.5)
    device.swipe(345,1083,333,170,0.1)
    device.sleep(0.5)
    device(index=6, className='android.widget.LinearLayout').click()
    # device.click(rand.randint(70, 600), rand.randint(920, 940))
    print('кнопка индекса')
    device.sleep(0.5)
    device.press("back")
    device.sleep(0.5)
    device(index=6, className='android.widget.LinearLayout').child(className='android.widget.EditText').set_text(user['code'])
    # kk.keyboard_num(user['code'], device)
    print('Ввод индекса')
    device.sleep(0.5)
    device(index=7, className='android.widget.LinearLayout').click()
    # device.click(rand.randint(70, 600), rand.randint(1020, 1045))
    print('Кнопка Мобильный телефон')
    device.sleep(0.5)
    device.press("back")
    device.sleep(0.5)
    device(index=7, className='android.widget.LinearLayout').child(className='android.widget.EditText').set_text(user['tele'])
    # kk.keyboard_num("+79776543035", device)
    print('Ввод телефона НОРМ ТЕЛЕФОН С ПЕРЕАДР')
    device.sleep(0.5)
    while not device(resourceId='com.adidas.app:id/adidasStatefulInternalButton', enabled='true').exists:
        device.sleep(1)
    device.sleep(0.5)
    device.click(rand.randint(40, 680), rand.randint(1239, 1240))
    print('Кнопка Сохранить')
    while not device(resourceId='com.adidas.app:id/addressText').exists:
        device.sleep(1)
    device.sleep(0.5)
    device.click(rand.randint(75, 400), rand.randint(900, 1000))
    print('Выбрать адрес')

    while not device(resourceId='com.adidas.app:id/checkout_screen_payment_method').exists:
        device.sleep(0.1)
    device.sleep(0.5)

    # Добавление оплаты
    device.click(rand.randint(480, 680), rand.randint(860, 890))  # Добавить проверку
    print(' кнопка выбрать метод оплаты')
    while not device(resourceId='com.adidas.app:id/addCardRoot').exists:
        device.sleep(0.1)
    device.sleep(0.5)
    device.click(rand.randint(70, 500), rand.randint(1175, 1230))
    print(' кнопка выбрать ВИЗА МАСТЕРКАРД МИР')
    while not device(index=3, className='android.widget.LinearLayout').exists:
        device.sleep(0.1)
    device.sleep(0.5)
    device.click(rand.randint(70, 650), rand.randint(305, 330))
    print(' кнопка номер карты')
    device.sleep(0.5)
    device(index=0, className='android.widget.LinearLayout').child(className='android.widget.EditText').set_text(user['card'])
    #kk.keyboard_num(user['card'], device)
    print('Ввод номера карты ДОДЕЛАТЬ')
    device.sleep(0.5)
    device.click(rand.randint(70, 600), rand.randint(555, 580))
    print(' кнопка срок')
    device.sleep(0.5)
    kk.keyboard_num(user['date'], device)
    device.sleep(0.5)
    kk.keyboard_num(user['year'], device)
    print(' Ввод срока')
    device.sleep(0.5)
    device.click(rand.randint(70, 600), rand.randint(655, 680))
    print('кнопка имя на карте')
    device.sleep(0.5)
    device(index=2, className='android.widget.LinearLayout').child(className='android.widget.EditText').set_text(kk.translit(user['name']) + ' ' + kk.translit(user['surname']))
    #kk.keyboard_eng(kk.translit(user['name']) + ' ' + kk.translit(user['surname']), device)
    print('Ввод имени')
    device.sleep(0.5)
    device.press("back")
    device.sleep(0.5)
    device(index=3, className='android.widget.LinearLayout').click()
    device.click(rand.randint(70, 600), rand.randint(830, 855))
    print('кнопка CVV')
    device.sleep(0.5)
    #device(index=3, className='android.widget.LinearLayout').child(className='android.widget.EditText').set_text(user['card'])
    kk.keyboard_num(user['CVV'], device)
    print(' Ввод CVV')
    device.sleep(0.5)
    device.press("back")
    device.sleep(0.5)
    device.swipe(rand.randint(70, 600), rand.randint(960, 1100), rand.randint(70, 600), rand.randint(32, 300),0.1)
    device.sleep(1)
    device.click(rand.randint(70, 600), rand.randint(1235, 1240))
    print('кнопка Сохранить карту')
    device.sleep(0.5)
    while not device(resourceId='com.adidas.app:id/conditionsText').exists and not device(
            resourceId='com.adidas.app:id/adidasStatefulInternalButton',
            enabled='true').exists:  # сделать проверку на иконку оплаты
        device.sleep(0.1)
    device.sleep(2)

    device.click(rand.randint(40, 650), rand.randint(1160, 1240))
    print('кнопка подтвердить с таймером')

    while not device(resourceId='com.adidas.app:id/alertDialogMessage').exists:
        device.sleep(0.1)
    device.sleep(0.5)

    device.click(rand.randint(370, 650), rand.randint(766, 850))
    print('кнопка подтвердить')
    device.sleep(0.5)
    while not device(className='android.widget.Button', enabled='true').exists:
        device.sleep(0.1)
