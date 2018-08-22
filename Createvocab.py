from os import listdir
from collections import Counter
from Dataprocessing import clean_file
from Dataprocessing import load_file
#path='Datasets/txt_sentoken/pos/cv001_18431.txt'


def add_file_to_vocab(file,vocab):
 text=load_file(file)
 tokens=clean_file(text)
 #UPDATING COUNTS
 vocab.update(tokens)


#FUNCTION FOR LOADING FILE IN A SPECIFIC DIRECTORY
def load_files(directory,vocab):
    for file in listdir(directory):
     if not file.endswith(".txt"):
        continue
     path=directory+file
     add_file_to_vocab(path,vocab)


#FUNCTION FOR SAVING DATA TO FILE
def save_file(lines,file):
    data='\n'.join(lines)
    #print(data)
    #For 1000 review data
    doc=open(file,'w')
    #For 12500 review data
    #doc = open(file, 'w',encoding='utf-8')
    doc.write(data)
    doc.close()

	
#For 1000 review data
pdirectory='Datasets/txt_sentoken/pos/'
ndirectory='Datasets/txt_sentoken/neg/'

#For 12500 review data
#pdirectory='Datasets/aclImdb/train/pos/'
#ndirectory='Datasets/aclImdb/train/neg/'


vocab=Counter()
load_files(pdirectory,vocab)
load_files(ndirectory,vocab)

#print("Original Length of Vocab:-%d"%len(vocab))
#print("50 Most Common Vocab words:-")
#print(vocab.most_common(50))
tokens=[w for w,c in vocab.items() if c>=5]
#print("Length of token greater than 5:-%d"%len(tokens))
#For 1000 review data
save_file(tokens,'1000vocab.txt')

#For 125000 review data
#save_file(tokens,'12500vocab.txt')

print("Add File to Vocab and Save File functions created.Vocab created.")