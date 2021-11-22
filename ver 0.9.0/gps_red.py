import random as rand


def gps_red(device, turn):
    device.click(287, 150)  ##GPS APP
    device.sleep(1)
    intx = rand.randint(81, 610)
    inty = rand.randint(705, 800)
    device.double_click(intx, inty, 0.01)
    device.sleep(0.5)
    device(index=2, className="android.widget.ImageView").click()
    device.sleep(2)
    device.press("home")
    device.sleep(0.5)
