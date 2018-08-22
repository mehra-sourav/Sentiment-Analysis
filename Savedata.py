from os import listdir
from Dataprocessing import load_file
from Dataprocessing import clean_file
from Createvocab import save_file

#LOADING VOCABULARY
#For 1000 review data
vocab=load_file('1000vocab.txt')
#For 12500 review data
#vocab=load_file('12500vocab.txt')
vocab=vocab.split()
#print(vocab)

def file_to_line(dir):
 doc=load_file(dir)
 tokens=clean_file(doc)
 #print(tokens)
 return ' '.join(tokens)


def convert_files(directory):
    lines=list()
    for file in listdir(directory):
     if not file.endswith(".txt"):
        continue
     path=directory+file
     #print('Loaded %s' %file)
     line=file_to_line(path)
     #print(line)
     #print(len(line))
     lines.append(line)
     #print(lines)
    return lines

#For 1000 review data
ppath='Datasets/txt_sentoken/pos/'
npath='Datasets/txt_sentoken/neg/'

positive = convert_files(ppath)
save_file(positive, '1000positive.txt')
negative = convert_files(npath)
save_file(negative, '1000negative.txt')


#For 12500 review data
#ppath='Datasets/aclImdb/train/pos/'
#npath='Datasets/aclImdb/train/neg/'

#positive = convert_files(ppath)
#save_file(positive, '12500positive.txt')
#negative = convert_files(npath)
#save_file(negative, '12500negative.txt')




print("Positive and negative files created")


