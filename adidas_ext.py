import random as rand

model = 'YEEZY 500'

def adidas_ext(device):

    device.sleep(0.5)
    device.press("home")
    device.sleep(0.5)
    device.click(93, 150)  # ADIDAS APP
    device.sleep(0.5)
    # try:
    #     device(text="OK").click()
    #     device.sleep(0.1)
    # except:
    #     pass
    while not device(resourceId='com.sec.android.app.launcher:id/home_allAppsIcon').exists:
        device.press("back")
        device.sleep(0.1)
    device.sleep(0.5)
    device.click(93, 150)  # ADIDAS APP
    while not device(text=model).exists:
        device.sleep(0.1)
    device.sleep(0.5)
    device.click(rand.randint(610, 700), rand.randint(60, 150))  # профиль
    device.sleep(1)
    device.swipe(400, 500, 100, 500, 0.1)
    device.sleep(0.5)
    device.swipe(400, 500, 100, 500, 0.1)# настройки
    device.sleep(0.5)
    device.swipe(rand.randint(180, 550), rand.randint(1190, 1270), rand.randint(180, 550), rand.randint(48, 250),
                 0.1)  #
    device.sleep(1)
    device.swipe(rand.randint(180, 550), rand.randint(1190, 1270), rand.randint(180, 550), rand.randint(48, 250),
                 0.1)  # свайпы вниз
    device.sleep(1)
    device.swipe(rand.randint(180, 550), rand.randint(1190, 1270), rand.randint(180, 550), rand.randint(48, 250),
                 0.1)  #
    device.sleep(1)
    device.click(rand.randint(40, 650), rand.randint(1140, 1220))  # выход
    device.sleep(2)
    device.press("back")  #
    device.sleep(0.5)
    device.press("home")
    device.sleep(0.5)
