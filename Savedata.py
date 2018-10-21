from os import listdir
from Dataprocessing import load_file
from Dataprocessing import clean_file
from Createvocab import save_file
import pickle as pkl

print("In Savedata.py")
print("Creating .pkl files")

#LOADING VOCABULARY
#For 1000 review data
##vocab=load_file('1000vocab.txt')
#For 12500 review data
vocab=load_file('12500vocab.txt')

vocab=vocab.split()
#print(vocab)

def file_to_line(dir):
 doc=load_file(dir)
 tokens=clean_file(doc)
 #print(tokens)
 return ' '.join(tokens)


def convert_files(directory):
    lines=[]
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
##ptrainpath='Datasets/txt_sentoken/train/pos/'
##ntrainpath='Datasets/txt_sentoken/train/neg/'
##ptestpath='Datasets/txt_sentoken/test/pos/'
##ntestpath='Datasets/txt_sentoken/test/neg/'

##Positivetrain = convert_files(ptrainpath)
#save_file(Positivetrain, '1000positivetrain.txt')
##Negativetrain = convert_files(ntrainpath)
###save_file(Negativetrain, '1000negativetrain.txt')
##Train_x = Positivetrain + Negativetrain
##Train_y = [1] * len(Positivetrain) + [0] * len(Negativetrain)

###save_file(Train_x,"1000train.txt")

##Positivetest=convert_files(ptestpath)
#save_file(Positivetest,'1000positivetest.txt')
##Negativetest=convert_files(ntestpath)
###save_file(Negativetest,'1000negativetest.txt')
##Test_x=Positivetest+Negativetest
##Test_y=[1]*len(Positivetest)+[0]*len(Negativetest)

###save_file(Test_x,"1000test.txt")

##f=open('1000train.pkl','wb')
##pkl.dump((Train_x,Train_y),f,-1)
##f.close()

##f=open('1000test.pkl','wb')
##pkl.dump((Test_x,Test_y),f,-1)
##f.close()


#For 12500 review data
ptraindirectory='Datasets/aclImdb/train/pos/'
ntraindirectory='Datasets/aclImdb/train/neg/'
ptestdirectory='Datasets/aclImdb/test/pos/'
ntestdirectory='Datasets/aclImdb/test/neg/'

positivetrain = convert_files(ptraindirectory)
###save_file(positivetrain, '12500positivetrain.txt')
negativetrain = convert_files(ntraindirectory)
###save_file(negativetrain, '12500negativetrain.txt')
train_x=positivetrain+negativetrain
train_y=[1]*len(positivetrain) + [0]*len(negativetrain)
###save_file(train_x,"12500train.txt")

positivetest = convert_files(ptestdirectory)
###save_file(positivetest, '12500positivetest.txt')
negativetest = convert_files(ntestdirectory)
###save_file(negativetest, '12500negativetest.txt')
test_x=positivetest+negativetest
test_y=[1]*len(positivetest)+[0]*len(negativetest)

###save_file(test_x,"12500test.txt")

f=open('12500train.pkl','wb')
pkl.dump((train_x,train_y),f,-1)
f.close()

f=open('12500test.pkl','wb')
pkl.dump((test_x,test_y),f,-1)
f.close()

print(".pkl files created\n")


