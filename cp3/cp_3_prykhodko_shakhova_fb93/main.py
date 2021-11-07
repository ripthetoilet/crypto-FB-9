with open ('encrypted.txt','r',encoding='utf-8') as file:
    encrypted = file.read()

with open ('decrypted.txt','r',encoding='utf-8') as file1:
    decrypted = file1.read()

alphabet = ['а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ы','ь','э','ю','я']
ciphertext = ''.join(i for i in encrypted if i in alphabet)

def gcd_extended(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcd_extended(b % a, a)
    x = y1 - (b//a)*x1
    y = x1
    return gcd, x, y


def find_reverse_element(a, mod):
    gcd, x, y = gcd_extended(a, mod)
    if gcd == 1:
        return (x % mod + mod) % mod
    else:
        return -1


def solve_linear_equation(a, b, mod):
    answer = []
    gsd, x, y = gcd_extended(a, mod)
    if gsd == 1:
        x = ((find_reverse_element(a, mod))*b) % mod
        return x
    elif b % gsd != 0:
        return -1
    else :
        a1 = a / gsd
        b1 = b / gsd
        n1 = mod / gsd
        x0 = solve_linear_equation(a1, b1, n1)
        for i in range(gsd-1):
            answer.append(int(x0+i*n1))
        return answer


def number_for_bigram(bigram, mod):
    return alphabet.index(bigram[0]) * mod + alphabet.index(bigram[1])


def bigram_from_number(number, mod):
    return alphabet[number//mod]+alphabet[number%mod]


def encrypt_bigram(a, b, mod, bigram):
    X = number_for_bigram(bigram, mod)
    Y = (a*X + b) % (mod*mod)
    return bigram_from_number(Y, mod)


def decrypt_bigram(a, b, mod, bigram):
    Y = number_for_bigram(bigram, mod)
    X = (find_reverse_element(a, mod*mod)*(Y-b)) % (mod*mod)
    return bigram_from_number(X, mod)


def encrypt(a, b, mod, text):
    encrypt=[]
    text = [text[i:i + 2] for i in range(0, len(text), 2)]
    for i in range(len(text)):
        encrypted = (encrypt_bigram(a, b, mod, text[i]))
        encrypt.append(encrypted)
    return ''.join(encrypt)


def decrypt(a,b,mod,text):
    decrypt = []
    text = [text[i:i + 2] for i in range(0, len(text), 2)]
    for i in range(len(text)):
        decrypted = (decrypt_bigram(a,b,mod,text[i]))
        decrypt.append(decrypted)
    decrypt =  ''.join(decrypt)
    return decrypt


def make_key(x1, x2, y1, y2, mod):
    Y = number_for_bigram(y1, mod)-number_for_bigram(y2, mod)
    X = number_for_bigram(x1,mod) - number_for_bigram(x2,mod)
    a = solve_linear_equation(X,Y,mod*mod)
    b = (number_for_bigram(y1,mod)-a*number_for_bigram(x1,mod))%(mod*mod)
    return [a,b]

print(decrypt(654,777,31,encrypted))
