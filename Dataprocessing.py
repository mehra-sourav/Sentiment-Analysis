from nltk.corpus import stopwords
from os import listdir

import string
path='Datasets/txt_sentoken/pos/cv000_29590.txt'

#FUNCTION FOR LOADING A SINGLE FILE
def load_file(path):
  #For 1000 review data
  file = open(path, 'r')
  #For 12500 review data
  #file=open(path,'r',encoding='utf-8')
  text=file.read()
  file.close()
  return text


#FUNCTION FOR LOADING FILE IN A SPECIFIC DIRECTORY
def load_files(directory):
    for file in listdir(directory):
     if not file.endswith(".txt"):
        continue
    path=directory+'/'+file
    doc=load_file(path)
    print('Loaded %s' %file)
    return None


#FUNCTION FOR CLEANING FILE
def clean_file(text):
    tokens=text.split()

    table=str.maketrans('','',string.punctuation)
    tokens=[w.translate(table) for w in tokens]

    stop_words=stopwords.words('english')
    tokens=[word for word in tokens if word.isalpha() and word not in stop_words and len(word)>1]

    return(tokens)


    #print(tokens)
   # print(table)


#directory='Datasets/txt_sentoken/pos'
#text=load_file(path)
#print(text)
#tokens=clean_file(text)
#print(tokens)

print("Load File and Create File functions created.")