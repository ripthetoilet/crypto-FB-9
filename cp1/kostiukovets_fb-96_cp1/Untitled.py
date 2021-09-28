#!/usr/bin/env python
# coding: utf-8

# In[56]:


import math
ru_alphabet = [chr(code) for code in range(ord("а"), ord("а") + 32)]
print(ru_alphabet)
f = open("TEXT").read().lower()


# In[101]:


dict_ = {}

for i in f:
    if i not in ru_alphabet:
        if i not in dict_:
            dict_[i] = 0
        else:
            dict_[i] += 1
        
print(dict_)
filtered_f = f
for i in dict_:
    filtered_f = filtered_f.replace(i,' ')
    
filtered_f = ' '.join(filtered_f.split())
nospace_f = filtered_f.replace(' ','')


# In[96]:



ru_alphabet = [chr(code) for code in range(ord("а"), ord("а") + 32)]

char_frequency = {}
for i in ru_alphabet:
    char_frequency[i] = nospace_f.count(i) / len(nospace_f)
    
bigram_frequency = {}
for i,val in enumerate(nospace_f):
    if i +1 >= len(nospace_f):
        break
    temp = nospace_f[i] + nospace_f[i+1]
    if temp not in bigram_frequency:
        bigram_frequency[temp] = nospace_f.count(temp) / (len(nospace_f))
        
    
ru_alphabet.append(" ")
char_frequency_space = {}
for i in ru_alphabet:
    char_frequency_space[i] = filtered_f.count(i) / len(filtered_f)
    

bigram_frequency_space = {}
for i,val in enumerate(filtered_f):
    if i +1 >= len(filtered_f):
        break
    temp = filtered_f[i] + filtered_f[i+1]
    if temp not in bigram_frequency_space and ' ' not in temp:
        bigram_frequency_space[temp] = filtered_f.count(temp) / (len(filtered_f))
        


# In[99]:



def entropy(dict_,n):
    sum_ = 0
    for p in dict_.values():
        sum_ += p * math.log2(p)
    return 1/n * ( -sum_)
    
cfe = entropy(char_frequency,1)
bfe = entropy(bigram_frequency,2)
cfse = entropy(char_frequency_space,1)
bfse = entropy(bigram_frequency_space,2)
print(cfe)
print(bfe )
print(cfse )
print(bfse )


# In[98]:


def redundancy(H,n):
    return 1 - (H/(math.log2(n)))

print(redundancy(cfe,len(ru_alphabet) - 1))
print(redundancy(bfe,len(ru_alphabet) - 1))
print(redundancy(cfse,len(ru_alphabet) - 1))
print(redundancy(bfse,len(ru_alphabet) - 1))

