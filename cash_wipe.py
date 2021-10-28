def cash_wipe(device):
    device.sleep(1)
    device.press("home")
    device.sleep(0.5)
    device(text="Настройки").click()
    device.sleep(0.5)
    try:
        device(text="Диспетчер приложений").click()
    except:
        device(text="Опции").click()
        device.sleep(0.5)
        device(text="Диспетчер приложений").click()
    device.sleep(0.5)
    while not device(text="adidas").exists:
        device.swipe(350, 1200, 350, 800, 0.1)
        device.sleep(0.5)
    device.sleep(0.5)
    device(text="adidas").click()
    while device(text="Вычисление...").exists or device(text="Очистить данные", enabled=0).exists:
        device.sleep(0.1)
    device.sleep(0.5)
    while not device(text="Очистить данные", clickable='true').exists:
        device.sleep(0.1)
    device(text="Очистить данные").click()
    device.sleep(0.5)
    device(text="Да").click()
    device.sleep(0.5)
    device.press("home")
    device.sleep(0.5)
