import random as rand


def adidas_ext(device):
    device.sleep(2)
    for i in range(12):
        device.press("back")
        device.sleep(1)
    device.sleep(3)
    device.click(93, 150)  # ADIDAS APP
    device.sleep(5)
    device.click(rand.randint(610, 700), rand.randint(60, 150))  # профиль
    device.sleep(6)
    device.click(rand.randint(510, 690), rand.randint(370, 405))  # настройки
    device.sleep(1)
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
    device.sleep(1)
    device.press("back")  #
    device.sleep(1)
    device.press("home")
    device.sleep(2)
