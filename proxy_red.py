import data as dd


def proxy_red(device, proxy, turn):
    device.press("home")
    device.sleep(1)
    dron=1
    if not device(text="Droni").exists:
        dron=0
    device.click(439, 140)  # Proxy APP
    device.sleep(2)
    if (dron==1):
        device.click(287, 1215)
        device.sleep(1)
        device.swipe(567, 680, 36, 617,0.3)
        device.sleep(1)
        device.click(248, 1057)  # wifi
        device.sleep(1)
        device.click(323, 257)  # имя wifi
        device.sleep(1)

        device.click(328, 652)  # сервер
        device.sleep(1)
        device(className="android.widget.EditText").set_text(proxy['ip'])
        device.sleep(1)
        device.click(575, 558)
        device.sleep(1)

    # device.click(351, 789)  # порт
    # device.sleep(1)
    # device(className="android.widget.EditText").set_text(proxy['port'])
    # device.sleep(1)
    # device.click(575, 558)
    # device.sleep(1)
    #
    # device.click(233, 908)  # имя
    # device.sleep(1)
    # device(className="android.widget.EditText").set_text(proxy["name"])
    # device.sleep(1)
    # device(index=1, className="android.widget.Button").click()
    # device.sleep(1)
    #
    # device.click(298, 1062)  # пароль
    # device.sleep(1)
    # device(className="android.widget.EditText").set_text(proxy["password"])
    # device.sleep(1)
    # device(index=1, className="android.widget.Button").click()
    # device.sleep(1)

        device.sleep(1)
        device.press("back")
        device.sleep(1)
        device.press("back")
        device.sleep(1)
        device.swipe(36, 617, 567, 680,0.3)
        device.sleep(1)
        device.click(287, 1215)
        device.sleep(5)
    else:
        device.sleep(0.5)
        device(resourceId='android:id/switchWidget').click()
        device.sleep(0.5)
        device(text='Адрес').click()
        device.sleep(0.5)
        device(resourceId='android:id/edit').set_text(proxy['ip'])
        device.sleep(0.5)
        device(resourceId='android:id/button1').click()
        device.sleep(0.5)
        device(resourceId='android:id/switchWidget').click()
        device.sleep(3)
    device.press("home")
    device.sleep(2)
