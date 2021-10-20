def cash_wipe(device):
    device.press("home")
    device(text="Настройки").click()
    device.sleep(3)
    device.swipe(350, 1200, 350, 1, 0.1)
    device.swipe(350, 1200, 350, 1, 0.1) # Ищем диспетчер приложений
    device.swipe(350, 1200, 350, 1, 0.1)
    device.sleep(3)
    device.click(89, 591)
    device.sleep(3)
    device.swipe(350, 1200, 350, 1, 0.5) # Ищем Adidas
    device.swipe(350, 1200, 350, 1, 0.5)
    device.sleep(2)
    device.click(89, 591) # Нажимаем Adidas
    device.sleep(2)
    device.swipe(350, 1200, 350, 600, 0.5) # Свайп к кэшу
    device.sleep(1)
    device(text="Очистить данные").click()
    device.sleep(1)
    device(text="Да").click()
    device.sleep(1)
    device.click(596, 689) # Отчистить кэш
    device.sleep(1)
    device.press("home")
    device.sleep(2)