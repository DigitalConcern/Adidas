def cash_wipe(device):
    device.sleep(1)
    device.press("home")
    device.sleep(0.5)
    device(text="Настройки").click()
    device.sleep(2)
    try:
        device(text="Опции").click()
        device.sleep(0.5)
        device(text="Диспетчер приложений").click()
    except:
        device(text="Диспетчер приложений").click()
    device.sleep(0.5)
    while not device(text="adidas").exists:
        device.swipe(350, 1200, 350, 1000, 0.05)
    device(text="adidas").click()
    device.sleep(5)
    device(text="Очистить данные").click()
    device.sleep(0.5)
    device(text="Да").click()
    device.sleep(0.5)
    device.press("home")
    device.sleep(1)
