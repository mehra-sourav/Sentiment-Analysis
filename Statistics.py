from nltk.corpus import stopwords
from Dataprocessing import load_file,clean_file
from collections import Counter
#from Createvocab import load_files,add_file_to_vocab
from os import listdir
from io import open
import string

def Unique_add_file_to_vocab(file, vocab):
    text = load_file(file)
    #tokens = text.split()
    tokens=clean_file(text)
    #print(tokens)
    # print(type(tokens))
    # UPDATING COUNTS
    vocab.update(tokens)


# FUNCTION FOR LOADING FILE IN A SPECIFIC DIRECTORY
def Unique_load_files(directory, vocab):
    for file in listdir(directory):
        if not file.endswith(".txt"):
            continue
        path = directory + file
        Unique_add_file_to_vocab(path, vocab)

def Total_tokens(path):
    text = load_file(path)
    tokens = text.split()
    return tokens
    #print(tokens)
    # print(type(tokens))
    # UPDATING COUNTS
    #return to

def Total_load_files(directory):
    tottokens=[]
    for file in listdir(directory):
        if not file.endswith(".txt"):
            continue
        path = directory + file
        tottokens.extend(Total_tokens(path))
    return tottokens
        #return


#path='Datasets/txt_sentoken/train/pos/cv000_29590.txt'


# For 1600 review data
pdirectory='Datasets/txt_sentoken/train/pos/'
ndirectory='Datasets/txt_sentoken/train/neg/'

# For 10000 review data
pdirectory1 = 'Datasets/10000 review dataset/train/pos/'
ndirectory1 = 'Datasets/10000 review dataset/train/neg/'

# For 25000 review data
pdirectory2 = 'Datasets/aclImdb/train/pos/'
ndirectory2 = 'Datasets/aclImdb/train/neg/'


Total_Tokens=Total_load_files(pdirectory2)+Total_load_files(ndirectory2)
#Total_Tokens=len(Total_Tokens)
#print(Total_Tokens)

vocab=Counter()

Unique_load_files(pdirectory2,vocab)
Unique_load_files(ndirectory2,vocab)
Unique_Tokens=[w for w,c in vocab.items()]
#Unique_Tokens=len(Unique_Tokens)
#print(Unique_tokens)

#tokens = [w for w, c in vocab.items()]# if c >= 5]
#print(type(tokens))
#text=load_file(path)
#print(text)
#print(text)
#tokens=text.split()

#print(string.punctuation)


def Tottokens(sentences):
    result = []
    #stop = stopwords.words('english')
    trash_characters = string.punctuation+'0123456789'
    trans = str.maketrans(trash_characters, ' '*len(trash_characters))

    for text in sentences:
        text = text.replace('<br />', ' ')
        text = text.replace('--', ' ').replace('\'s', '')
        text = text.translate(trans)
        text = ' '.join([w for w in text.split()])# if w not in stop])

        words = []
        for word in text.split():
            word = word.lstrip('-\'\"').rstrip('-\'\"')
            #if len(word)>2 :
            words.append(word.lower())
        text = ' '.join(words)
        result.append(text.strip())
    return result

punct=string.punctuation

def Stopcount(tokens):
    token=Tottokens(tokens)
    coun=0
    lt=[]
    #print(token)
    for wor in token:
     if wor in stop:
        lt.append(wor)
        coun+=1
    return lt,coun

def Puncount(tokens):
  coun=0
  for wor in tokens:
    for c in wor:
     if c in punct:
      coun+=1
  return coun


a='This is the excit$#ing! news!. I !was travelli/ng with my parents on a sunny afternoon. Suddenly, we got powers.'
#print("Original text:"+a)
b=a.split()
#print("Unfiltered Tokens:{b}".format(b=b))
#print(len(b))
stop = stopwords.words('english')

#print(punct)

#print("stop words="+str(Stopcount(b)[0])+"length="+str(Stopcount(b)[1]))

print("Total Tokens before preprocessing="+str(len(Total_Tokens)))
print("Stop words before preprocessing="+str(Stopcount(Total_Tokens)[1]))
print("Punctuation marks before preprocessing="+str(Puncount(Total_Tokens)))

print("\nUnique Tokens after preprocessing="+str(len(Unique_Tokens)))
print("Stop words after preprocessing="+str(Stopcount(Unique_Tokens)[1]))
print("Punctuation marks after preprocessing="+str(Puncount(Unique_Tokens)))

#for word in b:

#print(stopwords.words('english'))


#print("Second time"+b)

