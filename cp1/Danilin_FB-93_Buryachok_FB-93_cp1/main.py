from collections  import Counter 
import math 

mode = True#mode false means text without spaces
#true - with spaces
alphabet = ['а','б','в','г','д','е','ж','з','и','й','к',
            'л','м','н','о','п','р','с','т','у','ф','х','ц',
            'ч','ш','щ','ы','ь','э','ю','я']

if mode:
  with open("textWithSpaces.txt", encoding="utf-8") as file:
    text = file.read()
  alphabet.append(" ")
else:
   with open("text.txt", encoding="utf-8") as file:
    text = file.read()

length = len(text)

if (length % 2 == 1) :
  text += 'о'
  length += 1

def SetArrayOfBigrams(step):
  i = 0
  array = []
  while i < (length-1):
    array.append(text[i] + text[i+1])
    i += step
  return array

bigramArray1 = SetArrayOfBigrams(1)
bigramArray2 = SetArrayOfBigrams(2)

letters = Counter(text)
bigrams1 = Counter(bigramArray1)
bigrams2 = Counter(bigramArray2)

def CountEntropy(counter, len, n_gram):
    entropy = 0
    for i in counter:
        p = counter[i] / (len)
        entropy -= p*math.log(p,2)
    return entropy / n_gram



print('Entropy for letters: ',CountEntropy(letters, sum(letters.values()), 1))
print('Entropy for bigrams with step 1: ', CountEntropy(bigrams1, sum(bigrams1.values()),2))
print('Entropy for bigrams with step 2: ', CountEntropy(bigrams2, sum(bigrams2.values()),2))


def PrintLettersFreqency():
  for i in alphabet:
    print(i," => " ,(letters[i]/length))

#PrintLettersFreqency()

f1 = open('resultCross.txt', 'w')
def PrintCrossBigramFreqency(bigrams, len):
  for i in alphabet:
    for j in alphabet:
      bg = (i + j)
      p = bigrams[bg] / (len)
      f1.write(bg + "->" + (str('%.6f' % p) + " "))
    f1.write("\n")

PrintCrossBigramFreqency(bigrams1, sum(bigrams1.values()))
f1.close()


f2 = open('resultNotCross.txt', 'w')
def PrintNotCrossBigramFreqency(bigrams, len):
  for i in alphabet:
    for j in alphabet:
      bg = (i + j)
      p = bigrams[bg] / (len)
      f2.write(bg + "->" + (str('%.6f' % p) + " "))
    f2.write("\n")


PrintNotCrossBigramFreqency(bigrams2, sum(bigrams2.values()))
f2.close()

def PrintBigramFreqencyConcole(bigrams):
  for bg in bigrams.most_common():
    print(bg[0] + " : " + str(('%.6f' % (bg[1]/sum(bigrams.values())))))

PrintBigramFreqencyConcole(bigrams2)