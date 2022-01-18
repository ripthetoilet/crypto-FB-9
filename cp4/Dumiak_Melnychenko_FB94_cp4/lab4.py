from random import randrange
from math import gcd

out = open('output.txt', 'w', encoding='UTF-8')
# розширений алгоритм Евкліда
def gcd_extended(a, b):
    if a == 0:
        return b, 0, 1
    g, x1, y1 = gcd_extended(b % a, a)
    x = y1 - (b//a)*x1
    y = x1
    return g, x, y


# обернений елемент
def findrevel(a, mod):
    gcd, x, y = gcd_extended(a, mod)
    if gcd == 1:
        return (x % mod + mod) % mod
    else:
        return -1


# тест Мілера-Рабіна простоти числа
def miller_rabin(n):

    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
        return False

    d = n - 1
    r = 0

    while d % 2 == 0:
        d //= 2
        r += 1
    a = randrange(2, n - 1)
    x = pow(a, d, n)
    if x == 1 or x == n-1:
        return True
    while r > 1:
        x = pow(x, x, n)
        if x == 1:
            return False
        if x == -1:
            return True
        r -= 1
    return False


# генерація простого великого числа
def gen_prime(bits):
    while True:
        a = (randrange(1 << bits - 1, 1 << bits) << 1) + 1
        if miller_rabin(a):
            return a
        else:
            with open("not_passed_test.txt",'a') as file:
                file.writelines("Тест не пройдено " + str(a) + '\n')


# генерування публічного та приватного ключа
def generate_key_pair(p, q):
    n = p * q
    euler = (p - 1) * (q - 1)

    e = randrange(2, euler)
    while gcd(e, euler) != 1:
        e = randrange(2, euler)

    d = findrevel(e, euler)

    return [e, n], [d, p, q]

# цифровий підпис
def sign(msg, private_key):
    return pow(msg, private_key[0], private_key[1]*private_key[2])

# шифрування
def encrypt(msg, public_key):
    return pow(msg, public_key[0], public_key[1])

# розшифрування
def decrypt(encrypted_msg, private_key):
    return pow(encrypted_msg, private_key[0], private_key[1]*private_key[2])

# генерація чотирьох простих чисел
def gen_numbers_pair():
    pair = []
    for i in range(4):
        pair.append(gen_prime(256))
    while pair[0]*pair[1] >= pair[2]*pair[3]:
        pair = []
        for i in range(4):
            pair.append(gen_prime(256))
    return pair

# перевірка цифрового підпису
def verify(msg, sign, public_key):
    return pow(sign, public_key[0], public_key[1]) == msg

# процедура протоколу - отримання та верифікація повідомлення
def recieve_key(k1, s1, private, public):
    k = decrypt(k1, private)
    s = decrypt(s1, private)
    if verify(k, s, public):
        out.write(f'\nПовідомлення: {k} '
                  f'Повідомлення верифіковане!')
    else:
        out.write(f'\nПовідомлення не верифіковане ')
    return k, s


# процедура протоколу - надсилання
def send_key(k, public, private):
    k1 = encrypt(k, public)
    s = sign(k, private)
    s1 = encrypt(s, public)
    return k1, s1


# тестували "локально"
def my_test():
    # згенерували 4 простих числа

    p = 187156463707002327242518278048595454514917679063365971927821472291072504766441
    q = 127959056034053068909358638400152563064201296452461878347117921496951779449943
    p1 = 171609582938160317934866051290435176704795499855788447312475043502134297275223
    q1 = 195675775422407457345536838409950592640387574122223900423190191155768047508071
    out.write(f'p = {p}\n'
              f'q = {q}\n'
              f'p1 = {p1}\n'
              f'q1 = {q1}\n'
              )

    # згенерували публічні та приватні ключі Максиму та Олександру
    alpub, alpr = generate_key_pair(p, q)
    mpub, mpr = generate_key_pair(p1, q1)

    # наше повідомлення
    msg = 111333555777999
    # частина для Олександра
    encrypted_alex = encrypt(msg,alpub)
    decrypted_alex = decrypt(encrypted_alex,alpr)


    # Олександр підписав повідомлення та перевірили його
    alex_sign = sign(msg,alpr)


    # частина Максима
    encrypted_max = encrypt(msg, mpub)
    decrypted_max = decrypt(encrypted_max, mpr)

    # Максим підписав повідомлення - ми його перевірили
    max_sign = sign(msg, mpr)

    # протокол обміну
    k1,s1 = send_key(msg,mpub,alpr)
    recieve_key(k1,s1,mpr,alpub)
    out.write(f'\nПублічний ключ Олександра: (e,n) {alpub}\n'
              f'Приватний ключ Олександра: (d,p,q) {alpr}\n'
              f'Публічний ключ Максима: (e1,n1) {mpub}\n'
              f'Приватний ключ Максима: (d1,p1,q1){mpr}\n'
              f'\nЗашифроване повідомлення Олександра: {encrypted_alex}\n'
              f'Розшифроване повідомлення Олександра: {decrypted_alex}\n'
              f'Підпис Олександра: {alex_sign}\n'
              f'Перевірка підпису: {verify(msg,alex_sign,alpub)}\n'
              f'Зашифроване повідомлення Максима: {encrypted_max}\n'
              f'Розшифроване повідомлення Максима: {decrypted_max}\n'
              f'Підпис Максима: {max_sign}\n'
              f'Перевірка підпису: {verify(msg, max_sign, mpub)}\n'
              )

def int_to_hex(number):
    return hex(number)[2:].upper()


def hex_to_int(hex_value):
    return int(hex_value, 16)


def encode_to_hex(string):
    string = (string.encode('utf-8'))
    return string.hex().upper()


def decode_from_hex(hex_value):
    return bytes.fromhex(hex_value).decode('utf-8')


def sever_test():
    # ключ з сервера
    modulus = 'C606EB2ED40AC9D3591308000A1E05CA79CABBD890BC8D704CB7172E67D4A22B'
    exp = '10001'

    server_open = [hex_to_int(exp),hex_to_int(modulus)]

    msg = 'I want to die'

    # складові нашого ключа (згенеровані у 1 частині для Олександра)



    p = 187156463707002327242518278048595454514917679063365971927821472291072504766441
    q = 127959056034053068909358638400152563064201296452461878347117921496951779449943
    n = p * q
    euler = (p - 1) * (q - 1)
    e = randrange(2, euler)
    while gcd(e, euler) != 1:
        e = randrange(2, euler)
    d = findrevel(e, euler)


    my_open = [e,n]
    my_private = [d,p,q]


    # site encryption

    enc = encrypt(hex_to_int(encode_to_hex(msg)),my_open)



    # site decryption
    encrypted = encrypt(hex_to_int(encode_to_hex(msg)),server_open)



    # site sign
    site_sg = '9BCCB357BE5D4DBDA559E76510C82EFEE304C260773E87288093790AF8D5AFB4'


    # my sign
    my_sg = sign(hex_to_int(encode_to_hex(msg)),my_private)
    out.write(f'\nmod = {int_to_hex(n)}\n'
              f'e = {int_to_hex(e)}\n'
              f'enc= {int_to_hex(enc)}\n'
              f'Зашифроване = {int_to_hex(encrypted)}\n'
              f'\n{verify(hex_to_int(encode_to_hex(msg)),hex_to_int(site_sg),server_open)}\n'
              f'Мій підпис = {int_to_hex(my_sg)}\n'
              )

if __name__ == '__main__':
    my_test()
    sever_test()