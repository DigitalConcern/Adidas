import random
import string


def file_len(fname):
    with open(fname, encoding='utf-8') as f:
        for i, l in enumerate(f):
            pass
    return i + 1


def proxy(plist):
    check = False
    if file_len('proxxs.txt') <= len(plist):
        plist.clear()
    while not check:
        proxxy: str = random.choice(open('proxxs.txt', encoding='utf-8').readlines()).strip()
        if proxxy not in plist:
            true_proxy = proxxy
            check = True
    points = true_proxy.split(':')
    proxy_data = {
        'ip': points[0],
        'port': points[1],
        'name': points[2],
        'password': points[3]
    }
    plist.append(true_proxy)
    return proxy_data


def data(posts, addresses, fullnames, telephones, cards):
    check = False
    while not check:
        post: str = ''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(6, 9)))+'@abn-mail.xyz'
        if post not in posts:
            true_post = post
            check = True

    check = False
    if file_len('addresses.txt') <= len(addresses):
        addresses.clear()
    while not check:
        address: str = random.choice(open('addresses.txt', encoding='utf-8').readlines()).strip() \
                       + ', ' + f'{random.randint(1, 50)}'
        if address not in addresses:
            true_address = address
            check = True

    check = False
    if file_len('names.txt') <= len(fullnames):
        fullnames.clear()
    while not check:
        fullname: str = random.choice(open('names.txt', encoding='utf-8').readlines()).strip() \
                        + ' ' + random.choice(open('surnames.txt', encoding='utf-8').readlines()).strip() \
                        + ' ' + random.choice(open('midnames.txt', encoding='utf-8').readlines()).strip()
        if fullname not in fullnames:
            true_fullname = fullname
            check = True

    points = true_address.split(', ')
    points_name = true_fullname.split(' ')
    user = {
        'name': points_name[0],
        'surname': points_name[1],
        'midname': points_name[2],
        'country': points[0],
        'city': points[1],
        'street': points[2],
        'building': points[3],
        'flat': points[5],
        'code': points[4],
        'tele': 'NULL',
        'post': true_post,
        'password': 'TheBestGuysEver1',
        'card': 'NULL'
    }
    posts.append(true_post)
    addresses.append(true_address)
    fullnames.append(true_fullname)

    return user
