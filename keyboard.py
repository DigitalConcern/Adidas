import uiautomator2 as u2
import random as rand


d = u2.connect()
eng = {
    'q': [rand.randint(20, 55),   rand.randint(900, 955)],
    'w': [rand.randint(90, 125),  rand.randint(900, 955)],
    'e': [rand.randint(160, 200), rand.randint(900, 955)],
    'r': [rand.randint(232, 268), rand.randint(900, 955)],
    't': [rand.randint(308, 337), rand.randint(900, 955)],
    'y': [rand.randint(375, 412), rand.randint(900, 955)],
    'u': [rand.randint(446, 479), rand.randint(900, 955)],
    'i': [rand.randint(519, 560), rand.randint(900, 955)],
    'o': [rand.randint(585, 626), rand.randint(900, 955)],
    'p': [rand.randint(655, 700), rand.randint(900, 955)],

    'a': [rand.randint(52, 94), rand.randint(1000, 1055)],
    's': [rand.randint(123, 165), rand.randint(1000, 1055)],
    'd': [rand.randint(194, 235), rand.randint(1000, 1055)],
    'f': [rand.randint(265, 305), rand.randint(1000, 1055)],
    'g': [rand.randint(336, 378), rand.randint(1000, 1055)],
    'h': [rand.randint(407, 448), rand.randint(1000, 1055)],
    'j': [rand.randint(478, 515), rand.randint(1000, 1055)],
    'k': [rand.randint(549, 588), rand.randint(1000, 1055)],
    'l': [rand.randint(622, 663), rand.randint(1000, 1055)],

    'z': [rand.randint(124, 171), rand.randint(1092, 1153)],
    'x': [rand.randint(195, 236), rand.randint(1092, 1153)],
    'c': [rand.randint(268, 306), rand.randint(1092, 1153)],
    'v': [rand.randint(337, 374), rand.randint(1092, 1153)],
    'b': [rand.randint(410, 448), rand.randint(1092, 1153)],
    'n': [rand.randint(479, 523), rand.randint(1092, 1153)],
    'm': [rand.randint(550, 594), rand.randint(1092, 1153)],

    'back': [rand.randint(625, 700), rand.randint(1092, 1153)],
    'shift': [rand.randint(19, 88), rand.randint(1092, 1153)],
    ' ': [rand.randint(264, 512), rand.randint(1193, 1245)]
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
    '1': [rand.randint(20, 55),   rand.randint(810, 863)],
    '2': [rand.randint(90, 125),  rand.randint(810, 863)],
    '3': [rand.randint(160, 200), rand.randint(810, 863)],
    '4': [rand.randint(232, 268), rand.randint(810, 863)],
    '5': [rand.randint(308, 337), rand.randint(810, 863)],
    '6': [rand.randint(375, 412), rand.randint(810, 863)],
    '7': [rand.randint(446, 479), rand.randint(810, 863)],
    '8': [rand.randint(519, 560), rand.randint(810, 863)],
    '9': [rand.randint(585, 626), rand.randint(810, 863)],
    '0': [rand.randint(655, 700), rand.randint(810, 863)],

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

trans = {
    'й': 'j',
    'ц': 'cz',
    'у': 'u',
    'к': 'k',
    'е': 'e',
    'н': 'n',
    'г': 'g',
    'ш': 'sh',
    'щ': 'shh',
    'з': 'z',
    'х': 'kh',
    'ф': 'f',
    'ы': 'y',
    'в': 'v',
    'а': 'a',
    'п': 'p',
    'р': 'r',
    'о': 'o',
    'л': 'l',
    'д': 'd',
    'ж': 'zh',
    'э': 'e',
    'я': 'ya',
    'ч': 'ch',
    'с': 's',
    'м': 'm',
    'и': 'i',
    'т': 't',
    'б': 'b',
    'ю': 'yu'
}


def translit(word):
    rusword = ''
    for let in list(word):
        if let.isupper():
            let = let.lower()
        rusword += trans[let]
    return rusword


def keyboard_sym_pause(letter, device):
    device.click(rand.randint(17, 97), rand.randint(1105, 1144))
    device.sleep(0.01)
    device.click(sym[letter][0], sym[letter][1])
    device.sleep(0.01)
    device.click(rand.randint(17, 97), rand.randint(1105, 1144))


def keyboard_sym(string, device):
    device.click(rand.randint(17, 97), rand.randint(1105, 1144))
    device.sleep(0.1)
    lets = list(string)
    for let in lets:
        device.click(sym[let][0], sym[let][1])
    device.sleep(0.1)
    device.click(rand.randint(17, 97), rand.randint(1105, 1144))


def keyboard_rus(string, device):
    device.click(rand.randint(189, 235), rand.randint(1105, 1144))
    device.sleep(1)

    lets = list(string)
    for let in lets:
        if let in list('1234567890@#$_&+-=()/*,.'):
            keyboard_sym_pause(let, device)
        else:
            rand_chars = ['а', 'п', 'р', 'о', 'т', 'и', 'м', 'ь', 'г', 'ш', 'к', 'в']
            if rand.randint(1, 8) == 3:
                device.click(rus[rand.choice(rand_chars)][0], rus[rand.choice(rand_chars)][1])
                device.sleep(0.2)
                device.click(rus['back'][0], rus['back'][1])
                device.sleep(0.2)

            if let.isupper():
                let = let.lower()
                device.click(rus['shift'][0], rus['shift'][1])
                device.click(rus[let][0], rus[let][1])
            else:
                device.click(rus[let][0], rus[let][1])
        device.sleep(0.3)

    device.sleep(1)
    device.click(rand.randint(189, 235), rand.randint(1105, 1144))


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
        device.sleep(0.3)


keyboard_eng(translit('кринжанул'), d)
