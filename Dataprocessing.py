from nltk.corpus import stopwords
from os import listdir
import string
print("In Dataprocessing.py")
print("Creating Load_File and Create_File functions")
path='Datasets/txt_sentoken/train/pos/cv000_29590.txt'

#FUNCTION FOR LOADING A SINGLE FILE
def load_file(path):
  #For 1000 review data
  ##file = open(path, 'r')
  #For 12500 review data
  file=open(path,'r',encoding='utf-8')

  text=file.read()
  file.close()
  return text


#FUNCTION FOR LOADING FILE IN A SPECIFIC DIRECTORY
#def load_files(directory):
#    for file in listdir(directory):
#     if not file.endswith(".txt"):
#        continue
#    path=directory+'/'+file
#    doc=load_file(path)
#    print('Loaded %s' %file)
#    return None


#FUNCTION FOR CLEANING FILE
def clean_file(text):
    tokens=text.split()

    table=str.maketrans('','',string.punctuation)
    tokens=[w.translate(table) for w in tokens]
    stop_words=stopwords.words('english')
    tokens=[word for word in tokens if word.isalpha() and word not in stop_words and len(word)>1]
    return(tokens)


    #print(tokens)
    #print(table)

#FUNCTION FOR EXTRACTING WORDS FROM USER INPUT
def words(sentences):
    result = []
    stop = stopwords.words('english')
    trash_characters = string.punctuation+'0123456789'
    trans = str.maketrans(trash_characters, ' '*len(trash_characters))

    for text in sentences:
        text = text.replace('<br />', ' ')
        #text = text.replace('--', ' ').replace('\'s', '')
        text = text.translate(trans)
        text = ' '.join([w for w in text.split() if w not in stop])

        words = []
        for word in text.split():
            word = word.lstrip('-\'\"').rstrip('-\'\"')
            if len(word)>2 :
                words.append(word.lower())
        text = ' '.join(words)
        result.append(text.strip())
    return result
#a=['This','is','nice']
#b=words(a)
#print(b)


#directory='Datasets/txt_sentoken/pos'
#text=load_file(path)
#print(text)
#print(type(text))
#tokens=clean_file(text)
#print(tokens)
#print(type(tokens))

#print(string.punctuation)
print("Load_File and Create_File functions created\n")
