from array import *
from math import*
 
 
file_source = "..\\file1.txt"
file_noSpace = "..\\file2_noSpace.txt"
file_Space = "..\\file3_Space.txt"
file_probability_noSpace = "..\\file4_probability_noSpace.txt"
file_probability_Space = "..\\file5_probability_Space.txt"
file_bigramms_Space_1 = "..\\file6_bigramms_Space_1.txt"
file_bigramms_Space_2 = "..\\file7_bigramms_Space_2.txt"
file_bigramms_noSpace_1 = "..\\file8_bigramms_noSpace_1.txt"
file_bigramms_noSpace_2 = "..\\file9_bigramms_noSpace_2.txt"
 
 
Alphabet1=['а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ы','ь','ъ','э','ю','я']
Alphabet2=['а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ы','ь','ъ','э','ю','я', ' ']
 
 
file1 = open(file_source, "r")
cont_source = file1.read()
 
###################################################################################
###############################   Открываем файл 2     ############################
 
file2 = open(file_noSpace, "w")
 
# в этой функции мы меняем пpописные буквы на строчные и убраем пробелы
def swap_case(s):
    swapped = []
    for char in s:
        if char.isalpha() == False:  # убраем все лишние символы
            char = ''
 
        if char.isupper():  # меняем прописные буквы на строчные
            swapped.append(char.lower())
        else:
            swapped.append(char)
    return ''.join(swapped)
 
file2.write(swap_case(cont_source))
file2.close()
 
 
###########  тут стираются буквы, которых нет в алфавите ##################
file2 = open(file_noSpace, "r")
cont_noSpace = file2.read()
file2.close()
 
file2 = open(file_noSpace, "w")
def alph(s):
    arr = []
    for char in cont_noSpace:
        if char == 'ё':
            char = 'е'
        if char == 'ъ':
            char = 'ь'
 
        if char not in Alphabet1:
            char = ''
        else:
            arr.append(char)
    return ''.join(arr)
file2.write(alph(cont_noSpace))
file2.close()
 
 
#####################    Частота букв в файле 4     ###############################
 
file2 = open(file_noSpace, "r")
cont_noSpace = file2.read()
 
arr = []
thisset = set()
for char in cont_noSpace:
    thisset.add(char) 
for c in thisset:
    arr.append(c)
 
arr.sort()
for i in range(0,len(arr)):
    k = (cont_noSpace.count(arr[i]))/len(cont_noSpace)
    strochka1 = arr[i] + "\t " +str(cont_noSpace.count(arr[i])) + "\t " +  str(k)
    file4 = open(file_probability_noSpace, "a")
    file4.write(strochka1 + '\n')
    file4.close()
file2.close()
 
 
 
####################################################################################
############################   Открываем файл 3     ################################
 
file3 = open(file_Space, "w")
 
# в этой функции мы меняем пpописные буквы на строчные
def swap_case(s):
    swapped = []
    for char in s:
        if char.isupper():  # меняем прописные буквы на строчные
            swapped.append(char.lower())
        else:
            swapped.append(char)
    return ''.join(swapped)
 
 
file3.write(swap_case(cont_source))
file3.close()
 
###########  тут стираются буквы, которых нет в алфавите ##################
file3 = open(file_Space, "r")
cont_Space = file3.read()
file3.close()
 
file3 = open(file_Space, "w")
 
def alph(s):
    arr = []
    for char in cont_Space:
 
        if char == '\n':
            char = ' '
        if char == 'ё':
            char = 'е'
        if char == 'ъ':
            char = 'ь'
 
        if char not in Alphabet2:
            char = ''
        else:
            arr.append(char)
    return ''.join(arr)
 
###########  тут стираются ненужные пробелы ##################
def space(s):
    s = s.split()
    return ' '.join(s)
 
string = alph(cont_Space)
file3.write(space(string))
file3.close()
 
 
#####################   Частота букв в файле 3     ###############################
 
file3 = open(file_Space, "r")
cont_Space = file3.read()
 
arr = []
thisset = set()
for char in cont_Space:
    thisset.add(char) 
for c in thisset:
    arr.append(c)
 
 
arr.sort()
for i in range(0,len(arr)):
    k = (cont_Space.count(arr[i]))/len(cont_Space)
    strochka2 = arr[i] + "\t " +str(cont_Space.count(arr[i])) + "\t " +  str(k)
    file5 = open(file_probability_Space, "a")
    file5.write(strochka2 + '\n')
    file5.close()
file3.close()
 
#######################################################################################
###############################     Биграммы    #######################################
 
 
#############################  Файл 2 (без пробелов) с шагом 1      ###################
 
file2 = open(file_noSpace, "r")
cont_noSpace = file2.read()
 
arr1 = []
j = 0
for i in range(0,len(cont_noSpace)-1):
    char = cont_noSpace[i] + cont_noSpace[i+1]
    arr1.append(char)
    j+=1
arr = []
thisset = set()
for char in arr1:
    thisset.add(char) 
for c in thisset:
    arr.append(c)
arr.sort()
for i in range(0, len(arr)):
    
    k = (cont_noSpace.count(arr[i]))/j
    strochka3 = arr[i] + "\t " +str(cont_noSpace.count(arr[i])) + "\t " +  str(k)
    file6 = open(file_bigramms_noSpace_1, "a")
    file6.write(strochka3 + '\n')
    file6.close()

file2.close()
 
 
 
 
##########################   Файл 2 (без пробелов) с шагом 2      ####################
 
file2 = open(file_noSpace, "r")
cont_noSpace = file2.read()
 
arr1 = []
 
j = 0
i = 0
while i < len(cont_noSpace)-1:
    char = cont_noSpace[i] + cont_noSpace[i+1] 
    arr1.append(char)
    i+=2
    j+=1
 
 
arr = []
thisset = set()
for char in arr1:
    thisset.add(char) 
for c in thisset:
    arr.append(c)
 
arr.sort()
for i in range(0, len(arr)):
    
    k = (cont_noSpace.count(arr[i]))/j
    strochka3 = arr[i] + "\t " +str(cont_noSpace.count(arr[i])) + "\t " +  str(k)
    file7 = open(file_bigramms_noSpace_2, "a")
    file7.write(strochka3 + '\n')
    file7.close()
file2.close()
 
 
 
 
 
##########################   Файл 3 (с пробелами) с шагом 1      #####################
 
file3 = open(file_Space, "r")
cont_Space = file3.read()
 
arr1 = []
j = 0
for i in range(0,len(cont_Space)-1):
    char = cont_Space[i] + cont_Space[i+1]
    arr1.append(char)
    j+=1
arr = []
thisset = set()
for char in arr1:
    thisset.add(char) 
for c in thisset:
    arr.append(c)
 
arr.sort()

for i in range(0, len(arr)):
    
    k = (cont_Space.count(arr[i]))/j
    strochka3 = arr[i] + "\t " +str(cont_Space.count(arr[i])) + "\t " +  str(k)
    file8 = open(file_bigramms_Space_1, "a")
    file8.write(strochka3 + '\n')
    file8.close()
file3.close()
 
 
 
 
########################   Файл 3 (с пробелами) с шагом 2      #######################
 
file3 = open(file_Space, "r")
cont_Space = file3.read()
 
arr1 = []
 
j = 0
i = 0
while i < len(cont_Space)-1:
    char = cont_Space[i] + cont_Space[i+1]
    arr1.append(char)
    i+=2
    j += 1
 
arr = []
thisset = set()
for char in arr1:
    thisset.add(char)
for c in thisset:
    arr.append(c)
 
arr.sort()
for i in range(0, len(arr)):
    
    k = (cont_Space.count(arr[i]))/j
    strochka3 = arr[i] + "\t " +str(cont_Space.count(arr[i])) + "\t " +  str(k)
    file9 = open(file_bigramms_Space_2, "a")
    file9.write(strochka3 + '\n')
    file9.close()
 
file3.close()
