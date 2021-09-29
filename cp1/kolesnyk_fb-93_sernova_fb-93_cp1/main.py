import re
import math

def entrop_let(str_txt, filename, letters):
    lettersq=len(letters)
    entr=0
    let_q = [None] * lettersq
    let_freq_mass = [None] * lettersq
    len_txt = len(str_txt)
    for i in range(0, lettersq):
        let_freq_mass[i] = (str_txt.count(letters[i])) / len_txt
    # entrop:
    for i in range(0, lettersq):
        if(let_freq_mass[i]!=0):
            entr = entr + let_freq_mass[i] * math.log2(let_freq_mass[i])
    entr=-entr

    freq_dict = dict(zip(letters, let_freq_mass))
    sorted_values = sorted(freq_dict.values(), reverse=True)  # Sort the values
    sorted_dict = {}
    for i in sorted_values:
        for k in freq_dict.keys():
            if freq_dict[k] == i:
                sorted_dict[k] = freq_dict[k]
                break

    filename.write("\n" + "Sorted dict(letter+freq):\n")
    filename.write(str(sorted_dict))
    filename.write("\nEntrop: " + str(entr))


def entrop_bigr1(lett, text, filename, cross):
    alph_l = len(lett)

    mass_bigr = [[lett[k] + lett[i] for i in range(alph_l)] for k in range(alph_l)]
    values=[[0 for i in range(alph_l)] for k in range(alph_l)]


    if cross==True:
        for i in range(0, len(text) - 1):
            s1 = lett.find(text[i])
            s2 = lett.find(text[i + 1])
            values[s1][s2] += 1
        for i in range(0, alph_l):
            for j in range(alph_l):
                values[i][j]=values[i][j] / (len(text) - 1)
    else:
        for i in range(0, len(text) - 1, 2):
            s1 = lett.find(text[i])
            s2 = lett.find(text[i + 1])
            values[s1][s2] += 1
        for i in range(alph_l):
            for j in range(alph_l):
                values[i][j] = values[i][j] / (len(text)/2)
    entr = 0
    for i in range(alph_l):
        for j in range(alph_l):
            if (values[i][j] != 0):
                entr += (values[i][j] * (math.log2(values[i][j])))
    entr=-entr/2
    for i in range(alph_l):
        for j in range(alph_l):
            filename.write(" " + mass_bigr[i][j]+" -> "+str(values[i][j])+" " )
        filename.write("\n")
    filename.write("Entropy is: " + str(entr))


alpha = "абвгдежзийклмнопрстуфхцчшщыьэюя"
alpha2 = "абвгдежзийклмнопрстуфхцчшщыьэюя "
filesp = open('spaces.txt', 'r', encoding='utf-8') #filesp - file with spaces
filensp = open('nospaces.txt', 'r', encoding='utf-8') #without spaces
file2 = open('after.txt', 'w', encoding='utf-8') #result

text_str_nsp = filensp.read()
file2.write("Letters, no spaces: ")
file2.write("entrop for letters, no spaces")
entrop_let(text_str_nsp, file2, alpha)


file2.write("\nBigram cross, no spaces \n")
croos_val=True
entrop_bigr1(alpha, text_str_nsp, file2, croos_val)
file2.write("\nBigram for no cross, no spaces \n")
croos_val=False
entrop_bigr1(alpha, text_str_nsp, file2,croos_val)

#Робимо теж саме, але з пробілами

text_sp = filesp.read()

file2.write("\nEntrop for letters, with spaces\n")
entrop_let(text_sp, file2, alpha2)

file2.write("\nBigram cross, with spaces \n")
croos_val=True
entrop_bigr1(alpha2, text_sp,file2,croos_val)
file2.write("\nBigram for no cross, with spaces \n")
croos_val=False
entrop_bigr1(alpha2, text_sp, file2,croos_val,)

file2.close()
filesp.close()
filensp.close()