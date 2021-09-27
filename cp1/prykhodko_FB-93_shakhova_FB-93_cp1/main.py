import io
from math import log

file=io.open("with_spaces.txt", mode="r", encoding="utf-8")
file1=io.open("without_spaces.txt", mode="r", encoding="utf-8")

textWithSpaces = file.read()
textWithoutSpaces = file1.read()


alphabetWithSpaces = ['а','б','в','г','д','е','ж','з','и','й','к',
            'л','м','н','о','п','р','с','т','у','ф','х','ц',
            'ч','ш','щ','ы','ь','э','ю','я',' ']

alphabetWithoutSpaces = ['а','б','в','г','д','е','ж','з','и','й','к',
            'л','м','н','о','п','р','с','т','у','ф','х','ц',
            'ч','ш','щ','ы','ь','э','ю','я']

#розбиваю текст на різні біграми
CrossBigramWithSpaces = [textWithSpaces[i:i+2] for i in range(len(textWithSpaces))] #перехресна з пробілами
NoCrossBigramWithSpaces = [textWithSpaces[i:i+2] for i in range(0,len(textWithSpaces),2)] # не перехресна з пробілами
CrossBigramWithoutSpaces = [textWithoutSpaces[i:i+2] for i in range(len(textWithoutSpaces))] #перехресна без пробілів
NoCrossBigramWithoutSpaces = [textWithoutSpaces[i:i+2] for i in range(0,len(textWithoutSpaces),2)] # не перехресна без пробілів

def letters(alphabet,text):
    len_text = len(text)
    #створили словник
    dict = {}

    #заповнення словника ключ - літера , значення - частота
    for i in range(len(alphabet)):
        dict[alphabet[i]]=text.count(alphabet[i])/len_text

    #новий словник, значення у якому відсортовані
    sorted_dict = {}
    sorted_values = sorted(dict.values(),reverse=True)

    for i in sorted_values:
        for k in dict.keys():
            if dict[k]==i:
                sorted_dict[k] = dict[k]
                break
    print(sorted_dict)

    #підрахунок H1 безпосередньо за значенням
    h1 = 0
    for i in range(len(alphabet)):
        h = round(-dict.get(alphabet[i])*log(dict.get(alphabet[i]),2),3)
        h1 = h1+h

    print("H1 =",round(h1,4))


def bigram(alphabet,bigram_list):
    lenght = len(bigram_list)

    # створили матрицю розміром алфавіту + 1
    n = len(alphabet)+1
    matrix = [0] * n
    for i in range(n):
        matrix[i] = [0] * n

    matrix[0][0]="/"

    #присвоїли першому рядку значення букв
    for i in range(1, len(matrix[0])):
        matrix[0][i]=alphabet[i-1]

    #присвоїли першому стовпчику значення букв
    for i in range(1,len(matrix[0])):
        matrix[i][0]=alphabet[i-1]

    #порахували частоту для біграм
    for i in range(1,len(matrix[0])):
        for j in range(1,len(matrix[0])):
            big = matrix[0][i]+matrix[j][0]
            matrix[i][j]= ('{:.4f}'.format(bigram_list.count(big)/lenght))

    #вивід матриці
    for i in range(len(matrix)):
        for j in range(23,len(matrix)):
            if(i==0):
                print(matrix[i][j],"      ",end="")
            else: print(matrix[i][j]," ",end="")
        print()

    #підрахунок Н2 безпосередньо за значенням
    h2=0
    for i in range(1,len(matrix[0])):
        for j in range(1,len(matrix[0])):
            if(float(matrix[i][j])!=0):
                h2=h2+(-float(matrix[i][j])*(log(float(matrix[i][j]),2)))

    h2=round(h2/2,4)
    print("H2=",h2)

#letters(alphabetWithSpaces,textWithSpaces)
#letters(alphabetWithoutSpaces,textWithoutSpaces)
#bigram(alphabetWithSpaces,CrossBigramWithSpaces)
#bigram(alphabetWithSpaces,NoCrossBigramWithSpaces)
#bigram(alphabetWithoutSpaces,CrossBigramWithoutSpaces)
bigram(alphabetWithoutSpaces,NoCrossBigramWithoutSpaces)