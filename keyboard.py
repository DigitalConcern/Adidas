import uiautomator2 as u2
import random as rand

# СДЕЛАТЬ ПРОВЕРКУ НА КОРРЕКТНОСТЬ ВВОДА

d = u2.connect()
eng = {
    'q': [rand.randint(14, 64), rand.randint(878, 935)],
    'w': [rand.randint(87, 136), rand.randint(878, 935)],
    'e': [rand.randint(157, 206), rand.randint(878, 935)],
    'r': [rand.randint(228, 277), rand.randint(878, 935)],
    't': [rand.randint(300, 348), rand.randint(878, 935)],
    'y': [rand.randint(371, 420), rand.randint(878, 935)],
    'u': [rand.randint(443, 490), rand.randint(878, 935)],
    'i': [rand.randint(515, 560), rand.randint(878, 935)],
    'o': [rand.randint(585, 631), rand.randint(878, 935)],
    'p': [rand.randint(655, 704), rand.randint(878, 935)],

    'a': [rand.randint(52, 94), rand.randint(980, 1036)],
    's': [rand.randint(123, 170), rand.randint(980, 1036)],
    'd': [rand.randint(194, 238), rand.randint(980, 1036)],
    'f': [rand.randint(265, 310), rand.randint(980, 1036)],
    'g': [rand.randint(336, 382), rand.randint(980, 1036)],
    'h': [rand.randint(407, 454), rand.randint(980, 1036)],
    'j': [rand.randint(478, 526), rand.randint(980, 1036)],
    'k': [rand.randint(549, 598), rand.randint(980, 1036)],
    'l': [rand.randint(620, 668), rand.randint(980, 1036)],

    'z': [rand.randint(124, 171), rand.randint(1083, 1137)],
    'x': [rand.randint(195, 242), rand.randint(1083, 1137)],
    'c': [rand.randint(266, 313), rand.randint(1083, 1137)],
    'v': [rand.randint(337, 384), rand.randint(1083, 1137)],
    'b': [rand.randint(408, 455), rand.randint(1083, 1137)],
    'n': [rand.randint(479, 526), rand.randint(1083, 1137)],
    'm': [rand.randint(550, 597), rand.randint(1083, 1137)],

    'back': [rand.randint(620, 700), rand.randint(1083, 1138)],
    'shift': [rand.randint(15, 100), rand.randint(1083, 1138)],
    ' ': [rand.randint(196, 524), rand.randint(1183, 1241)]
}

rus = {
    'й': [rand.randint(18, 62), rand.randint(879, 935)],
    'ц': [rand.randint(81, 126), rand.randint(879, 935)],
    'у': [rand.randint(145, 190), rand.randint(879, 935)],
    'к': [rand.randint(208, 254), rand.randint(879, 935)],
    'е': [rand.randint(272, 318), rand.randint(879, 935)],
    'ё': [rand.randint(272, 318), rand.randint(879, 935)],
    'н': [rand.randint(336, 382), rand.randint(879, 935)],
    'г': [rand.randint(400, 446), rand.randint(879, 935)],
    'ш': [rand.randint(464, 510), rand.randint(879, 935)],
    'щ': [rand.randint(528, 575), rand.randint(879, 935)],
    'з': [rand.randint(600, 638), rand.randint(879, 935)],
    'х': [rand.randint(660, 701), rand.randint(879, 935)],

    'ф': [rand.randint(18, 62), rand.randint(981, 1035)],
    'ы': [rand.randint(81, 126), rand.randint(981, 1035)],
    'в': [rand.randint(145, 190), rand.randint(981, 1035)],
    'а': [rand.randint(208, 254), rand.randint(981, 1035)],
    'п': [rand.randint(272, 318), rand.randint(981, 1035)],
    'р': [rand.randint(336, 382), rand.randint(981, 1035)],
    'о': [rand.randint(400, 446), rand.randint(981, 1035)],
    'л': [rand.randint(464, 510), rand.randint(981, 1035)],
    'д': [rand.randint(528, 575), rand.randint(981, 1035)],
    'ж': [rand.randint(600, 638), rand.randint(981, 1035)],
    'э': [rand.randint(660, 701), rand.randint(981, 1035)],

    'я': [rand.randint(83, 125), rand.randint(1083, 1137)],
    'ч': [rand.randint(147, 189), rand.randint(1083, 1137)],
    'с': [rand.randint(210, 253), rand.randint(1083, 1137)],
    'м': [rand.randint(276, 317), rand.randint(1083, 1137)],
    'и': [rand.randint(340, 381), rand.randint(1083, 1137)],
    'т': [rand.randint(403, 445), rand.randint(1083, 1137)],
    'ь': [rand.randint(467, 509), rand.randint(1083, 1137)],
    'б': [rand.randint(531, 570), rand.randint(1083, 1137)],
    'ю': [rand.randint(595, 638), rand.randint(1083, 1137)],

    'back': [rand.randint(659, 700), rand.randint(1083, 1137)],
    'shift': [rand.randint(18, 60), rand.randint(1083, 1137)],
    ' ': [rand.randint(196, 521), rand.randint(1187, 1239)]
}

sym = {
    '1': [rand.randint(17, 60), rand.randint(789, 829)],
    '2': [rand.randint(88, 131), rand.randint(789, 829)],
    '3': [rand.randint(159, 202), rand.randint(789, 829)],
    '4': [rand.randint(230, 273), rand.randint(789, 829)],
    '5': [rand.randint(301, 344), rand.randint(789, 829)],
    '6': [rand.randint(372, 415), rand.randint(789, 829)],
    '7': [rand.randint(443, 486), rand.randint(789, 829)],
    '8': [rand.randint(514, 557), rand.randint(789, 829)],
    '9': [rand.randint(585, 628), rand.randint(789, 829)],
    '0': [rand.randint(656, 699), rand.randint(789, 829)],

    '@': [rand.randint(87, 136), rand.randint(982, 1034)],
    '#': [rand.randint(161, 204), rand.randint(982, 1034)],
    '$': [rand.randint(232, 274), rand.randint(982, 1034)],
    '_': [rand.randint(376, 417), rand.randint(880, 927)],
    '&': [rand.randint(446, 491), rand.randint(982, 1034)],
    '-': [rand.randint(129, 169), rand.randint(1083, 1133)],
    '+': [rand.randint(22, 62), rand.randint(880, 927)],
    '(': [rand.randint(590, 627), rand.randint(982, 1034)],
    ')': [rand.randint(657, 697), rand.randint(982, 1034)],
    '/': [rand.randint(302, 340), rand.randint(982, 1034)],
    '.': [rand.randint(552, 590), rand.randint(1187, 1237)],
    ',': [rand.randint(482, 525), rand.randint(1083, 1133)],
}

num = {
    '1': [rand.randint(20, 160), rand.randint(790, 880)],
    '2': [rand.randint(200, 330), rand.randint(790, 880)],
    '3': [rand.randint(380, 510), rand.randint(790, 880)],

    '4': [rand.randint(20, 160), rand.randint(912, 1000)],
    '5': [rand.randint(200, 330), rand.randint(912, 1000)],
    '6': [rand.randint(380, 510), rand.randint(912, 1000)],

    '7': [rand.randint(20, 160), rand.randint(1030, 1120)],
    '8': [rand.randint(200, 330), rand.randint(1030, 1120)],
    '9': [rand.randint(380, 510), rand.randint(1030, 1120)],

    '0': [rand.randint(200, 330), rand.randint(1155, 1235)],
    '+': [rand.randint(200, 330), rand.randint(1155, 1235)]
}


def keyboard_sym_pause(letter, device):
    device.click(rand.randint(19, 97), rand.randint(1184, 1236))
    device.sleep(0.01)
    device.click(sym[letter][0], sym[letter][1])
    device.sleep(0.01)
    device.click(rand.randint(19, 97), rand.randint(1184, 1236))


def keyboard_sym(string, device):
    device.click(rand.randint(19, 97), rand.randint(1184, 1236))
    device.sleep(0.1)
    lets = list(string)
    for let in lets:
        device.click(sym[let][0], sym[let][1])
    device.sleep(0.1)
    device.click(rand.randint(19, 97), rand.randint(1184, 1236))


def keyboard_rus(string, device, ifrus, ifshift):
    if ifrus != 1:
        device.swipe(rand.randint(211, 253), rand.randint(1192, 1232), rand.randint(470, 510), rand.randint(1192, 1232))
    device.sleep(rand.uniform(0.1, 0.3))
    if ifshift != 0:
        device.sleep(1)
        device.click(rus['shift'][0], rus['shift'][1])
        device.sleep(1)
        device.click(rus['shift'][0], rus['shift'][1])
    lets = list(string)
    first_letter = 1
    for let in lets:
        if let in list('1234567890@#$_&+-=()/*,.'):
            keyboard_sym_pause(let, device)
        else:
            rand_chars = ['а', 'п', 'р', 'о', 'т', 'и', 'м', 'ь', 'г', 'ш', 'к', 'в']
            if rand.randint(1, 8) == 3 and first_letter != 1:
                device.click(rus[rand.choice(rand_chars)][0], rus[rand.choice(rand_chars)][1])
                device.sleep(0.2)
                device.click(rus['back'][0], rus['back'][1])
                device.sleep(0.2)
            first_letter = 0
            if let.isupper():
                let = let.lower()
                device.click(rus['shift'][0], rus['shift'][1])
                device.click(rus[let][0], rus[let][1])
            else:
                device.click(rus[let][0], rus[let][1])
        device.sleep(rand.uniform(0.1, 0.3))

    device.sleep(rand.uniform(0.1, 0.3))
    device.swipe(rand.randint(211, 253), rand.randint(1192, 1232), rand.randint(470, 510), rand.randint(1192, 1232))


def keyboard_eng(string, device):
    lets = list(string)
    for let in lets:
        if let in list('1234567890@#$_&+-=()/*,.'):
            keyboard_sym_pause(let, device)
        else:
            rand_chars = ['j', 'g', 'f', 'h', 'l', 'b', 'v', 'c', 'n', 'm', 'x', 'r']
            if rand.randint(1, 8) == 3:
                device.click(eng[rand.choice(rand_chars)][0], eng[rand.choice(rand_chars)][1])
                device.sleep(0.2)
                device.click(eng['back'][0], eng['back'][1])
                device.sleep(0.2)

            if let.isupper():
                let = let.lower()
                device.click(eng['shift'][0], eng['shift'][1])
                device.click(eng[let][0], eng[let][1])
            else:
                device.click(eng[let][0], eng[let][1])
        device.sleep(rand.uniform(0.1, 0.3))


def keyboard_num(string, device):
    lets = list(string)
    for let in lets:
        if let != '+':
            device.click(num[let][0], num[let][1])
        else:
            device.long_click(num[let][0], num[let][1])
    device.sleep(rand.uniform(0.1, 0.3))
