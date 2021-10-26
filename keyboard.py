import uiautomator2 as u2
import random as rand

# СДЕЛАТЬ ПРОВЕРКУ НА КОРРЕКТНОСТЬ ВВОДА

# d = u2.connect()
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

    'z': [rand.randint(124, 171), rand.randint(1096, 1152)],
    'x': [rand.randint(195, 236), rand.randint(1096, 1152)],
    'c': [rand.randint(268, 306), rand.randint(1096, 1152)],
    'v': [rand.randint(337, 374), rand.randint(1096, 1152)],
    'b': [rand.randint(410, 448), rand.randint(1096, 1152)],
    'n': [rand.randint(479, 523), rand.randint(1096, 1152)],
    'm': [rand.randint(550, 594), rand.randint(1096, 1152)],

    'back': [rand.randint(625, 700), rand.randint(1092, 1152)],
    'shift': [rand.randint(19, 88), rand.randint(1092, 1152)],
    ' ': [rand.randint(295, 500), rand.randint(1193, 1245)],
    '.': [rand.randint(555, 588), rand.randint(1187, 1239)]
}

rus = {
    'й': [rand.randint(20,   51), rand.randint(905, 950)],
    'ц': [rand.randint(85,  111),  rand.randint(905, 950)],
    'у': [rand.randint(145, 178), rand.randint(905, 950)],
    'к': [rand.randint(212, 245), rand.randint(905, 950)],
    'е': [rand.randint(277, 308), rand.randint(905, 950)],
    'ё': [rand.randint(277, 308), rand.randint(905, 950)],
    'н': [rand.randint(340, 375), rand.randint(905, 950)],
    'г': [rand.randint(407, 437), rand.randint(905, 950)],
    'ш': [rand.randint(471, 502), rand.randint(905, 950)],
    'щ': [rand.randint(534, 567), rand.randint(905, 950)],
    'з': [rand.randint(600, 633), rand.randint(905, 950)],
    'х': [rand.randint(670, 697), rand.randint(905, 950)],

    'ф': [rand.randint(20,   51), rand.randint(1000, 1055)],
    'ы': [rand.randint(85,  111), rand.randint(1000, 1055)],
    'в': [rand.randint(145, 178), rand.randint(1000, 1055)],
    'а': [rand.randint(212, 245), rand.randint(1000, 1055)],
    'п': [rand.randint(277, 308), rand.randint(1000, 1055)],
    'р': [rand.randint(340, 375), rand.randint(1000, 1055)],
    'о': [rand.randint(407, 437), rand.randint(1000, 1055)],
    'л': [rand.randint(471, 502), rand.randint(1000, 1055)],
    'д': [rand.randint(534, 567), rand.randint(1000, 1055)],
    'ж': [rand.randint(600, 633), rand.randint(1000, 1055)],
    'э': [rand.randint(670, 697), rand.randint(1000, 1055)],

    'я': [rand.randint(100, 128), rand.randint(1100, 1147)],
    'ч': [rand.randint(162, 190), rand.randint(1100, 1147)],
    'с': [rand.randint(219, 248), rand.randint(1100, 1147)],
    'м': [rand.randint(283, 311), rand.randint(1100, 1147)],
    'и': [rand.randint(346, 369), rand.randint(1100, 1147)],
    'т': [rand.randint(407, 429), rand.randint(1100, 1147)],
    'ь': [rand.randint(469, 491), rand.randint(1100, 1147)],
    'б': [rand.randint(528, 555), rand.randint(1100, 1147)],
    'ю': [rand.randint(595, 618), rand.randint(1100, 1147)],

    'back': [rand.randint(659, 700), rand.randint(1100, 1147)],
    'shift': [rand.randint(21, 60), rand.randint(1100, 1147)],
    ' ': [rand.randint(196, 521), rand.randint(1187, 1239)],
    '.': [rand.randint(555, 588), rand.randint(1187, 1239)]
}

sym = {
    '1': [rand.randint(20, 55),   rand.randint(789, 829)],
    '2': [rand.randint(90, 125),  rand.randint(789, 829)],
    '3': [rand.randint(160, 200), rand.randint(789, 829)],
    '4': [rand.randint(232, 268), rand.randint(789, 829)],
    '5': [rand.randint(308, 337), rand.randint(789, 829)],
    '6': [rand.randint(375, 412), rand.randint(789, 829)],
    '7': [rand.randint(446, 479), rand.randint(789, 829)],
    '8': [rand.randint(519, 560), rand.randint(789, 829)],
    '9': [rand.randint(585, 626), rand.randint(789, 829)],
    '0': [rand.randint(655, 700), rand.randint(789, 829)],

    '@': [rand.randint(21, 57), rand.randint(943, 1001)],
#     '#': [rand.randint(161, 204), rand.randint(982, 1034)],
#     '$': [rand.randint(232, 274), rand.randint(982, 1034)],
#     '_': [rand.randint(376, 417), rand.randint(880, 927)],
#     '&': [rand.randint(446, 491), rand.randint(982, 1034)],
    '-': [rand.randint(377, 408), rand.randint(1001, 1050)],
    '+': [rand.randint(445, 480), rand.randint(1001, 1050)],
#     '(': [rand.randint(590, 627), rand.randint(982, 1034)],
#     ')': [rand.randint(657, 697), rand.randint(982, 1034)],
#     '/': [rand.randint(302, 340), rand.randint(982, 1034)],
#     '.': [rand.randint(552, 590), rand.randint(1187, 1237)]
#     ',': [rand.randint(482, 525), rand.randint(1083, 1133)],
}

num = {
    '1': [rand.randint(25, 165), rand.randint(900, 956)],
    '2': [rand.randint(202, 350), rand.randint(900, 956)],
    '3': [rand.randint(380, 519), rand.randint(900, 956)],

    '4': [rand.randint(25, 165), rand.randint(993, 1050)],
    '5': [rand.randint(202, 350), rand.randint(993, 1050)],
    '6': [rand.randint(380, 519), rand.randint(993, 1050)],

    '7': [rand.randint(25, 165), rand.randint(1100, 1150)],
    '8': [rand.randint(202, 350), rand.randint(1100, 1150)],
    '9': [rand.randint(380, 519), rand.randint(1100, 1150)],

    '0': [rand.randint(202, 350), rand.randint(1196, 1250)],
    '+': [rand.randint(202, 350), rand.randint(1196, 1250 )]
}


trans = {
    'й': 'j',
    'ц': 'cz',
    'у': 'u',
    'к': 'k',
    'е': 'e',
    'ё': 'yo',
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
    'ю': 'yu',
    'ь': '',
    ' ': ' ',
    '.': '.'
}


def translit(word):
    rusword = ''
    for let in list(word):
        if let.isupper():
            let = let.lower()
        rusword += trans[let]
    return rusword


def keyboard_sym_pause(letter, device):
    if letter in list("1234567890"):
        device.sleep(0.1)
        device.click(sym[letter][0], sym[letter][1])
        device.sleep(0.1)
    else:
        device.click(rand.randint(25, 91), rand.randint(1155, 1235))
        device.sleep(0.5)
        device.click(sym[letter][0], sym[letter][1])
        device.sleep(0.5)
        device.click(rand.randint(25, 91), rand.randint(1155, 1235))


def keyboard_sym(string, device):
    device.click(rand.randint(25, 91), rand.randint(1155, 1235))
    device.sleep(0.1)
    lets = list(string)
    for let in lets:
        device.click(sym[let][0], sym[let][1])
        device.sleep(rand.uniform(0.01, 0.1))
    device.sleep(0.1)
    device.click(rand.randint(17, 97), rand.randint(1155, 1235))


def keyboard_rus(string, device):
    device.click(rand.randint(195, 235), rand.randint(1195, 1245))
    device.sleep(1)
    lets = list(string)
    i = 0
    for let in lets:
        if let in list('1234567890@#$_&+-=()/*,'):
            keyboard_sym_pause(let, device)
        else:
            if i > 0:
                rand_chars = ['а', 'п', 'р', 'о', 'т', 'и', 'м', 'ь', 'г', 'ш', 'к', 'в']
                if rand.randint(1, 8) == 3:
                    rand_char = rand.choice(rand_chars)
                    device.click(rus[rand_char][0], rus[rand_char][1])
                    device.sleep(0.2)
                    device.click(rus['back'][0], rus['back'][1])
                    device.sleep(0.2)
                if let.isupper():
                    let = let.lower()
                    device.sleep(0.2)
                    device.click(rus['shift'][0], rus['shift'][1])
                    device.sleep(0.2)
                    device.click(rus[let][0], rus[let][1])
                else:
                    device.click(rus[let][0], rus[let][1])
            else:
                if let.isupper():
                    let = let.lower()
                    device.click(rus[let][0], rus[let][1])
                else:
                    device.click(rus[let][0], rus[let][1])
        device.sleep(rand.uniform(0.01, 0.1))
        i += 1

    device.sleep(rand.uniform(0.01, 0.1))
    device.sleep(1)
    device.click(rand.randint(195, 235), rand.randint(1195, 1245))


def keyboard_eng(string, device):
    lets = list(string)
    i = 0
    for let in lets:
        if let in list('1234567890@#$_&+-=()/*,'):
            keyboard_sym_pause(let, device)
        else:
            if i > 0:
                rand_chars = ['j', 'g', 'f', 'h', 'l', 'b', 'v', 'c', 'n', 'm', 'x', 'r']
                if rand.randint(1, 8) == 3:
                    rand_char = rand.choice(rand_chars)
                    device.click(eng[rand_char][0], eng[rand_char][1])
                    device.sleep(0.2)
                    device.click(eng['back'][0], eng['back'][1])
                    device.sleep(0.2)
                if let.isupper():
                    let = let.lower()
                    device.sleep(0.2)
                    device.click(eng['shift'][0], eng['shift'][1])
                    device.sleep(0.2)
                    device.click(eng[let][0], eng[let][1])
                else:
                    device.click(eng[let][0], eng[let][1])
            else:
                if let.isupper():
                    let = let.lower()
                    device.click(eng[let][0], eng[let][1])
                else:
                    device.click(eng[let][0], eng[let][1])
        device.sleep(rand.uniform(0.01, 0.1))
        i += 1


def keyboard_num(string, device):
    lets = list(string)
    for let in lets:
        device.click(num[let][0], num[let][1])
        device.sleep(rand.uniform(0.01, 0.1))


# keyboard_eng(translit('На дворе октябрь. '
#              'Уже убрали с полей картофель. '
#              'На огородах срезают капусту. '
#              'Тяжёлые светлые кочаны лежат в корзинках. '
#              'Сладкая репка и красная морковка насыпаны между грядками. '
#              'На краю леса краснеет рябина. '
#              'Кудрявое дерево ее усыпано ягодами словно яркими бусами. '
#              'По опушкам алеют зрелые ягоды калины. '
#              'Сильнее дует осенний ветер. '
#              'В комнатах потеют окошки. '), d)

# keyboard_num('+79162548685', d)


