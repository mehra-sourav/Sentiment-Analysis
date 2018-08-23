from os import listdir
from Dataprocessing import load_file
from Dataprocessing import clean_file
from Createvocab import save_file
import pickle as pkl

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
#ppath='Datasets/txt_sentoken/pos/'
#npath='Datasets/txt_sentoken/neg/'

#positive = convert_files(ppath)
#save_file(positive, '1000positive.txt')
#negative = convert_files(npath)
#save_file(negative, '1000negative.txt')


#For 12500 review data
#ptraindirectory='Datasets/aclImdb/train/pos/'
#ntraindirectory='Datasets/aclImdb/train/neg/'
#ptestdirectory='Datasets/aclImdb/test/pos/'
#ntestdirectory='Datasets/aclImdb/test/neg/'

#positivetrain = convert_files(ptraindirectory)
#save_file(positivetrain, '12500positivetrain.txt')
#negativetrain = convert_files(ntraindirectory)
#save_file(negativetrain, '12500negativetrain.txt')
#positivetest = convert_files(ptestdirectory)
#save_file(positivetest, '12500positivetest.txt')
#negativetest = convert_files(ntestdirectory)
#save_file(negativetest, '12500negativetest.txt')




print("Positive and negative files created")


