from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score as ACC
from sklearn import svm as SVM
#import numpy as np
from Dataprocessing import words
import pickle as pkl
#For 1000 review data
##f=open('1000train.pkl','rb')
##train=pkl.load(f)
##f.close()

##f=open('1000test.pkl','rb')
##test=pkl.load(f)
##f.close()

#For 12500 review data
f=open('12500train.pkl','rb')
train=pkl.load(f)
f.close()

f=open('12500test.pkl','rb')
test=pkl.load(f)
f.close()
#print(type(train[0]))

vect=TfidfVectorizer()

trainfeat=vect.fit_transform(train[0])
testfeat=vect.transform(test[0])

svm=SVM.LinearSVC()
svm.fit(trainfeat,train[1])
predict=svm.predict(testfeat)

print("Accuracy:-{ACC}%\n".format(ACC=100*ACC(test[1],predict)))

while True:
    review=[]
    line=input("Enter a sentence('Quit' to quit):\n")
    if line!='Quit':
        #print("Words Type:"+type(review).__name__)
        review.append(line)
        #a=words(review)
        #print(a)
        #print("Words Type:"+type(a).__name__)
        data=vect.transform(words(review))
        #print(data)
        predict=svm.predict(data)
        #print(predict)
        #print("Predict 0:"+np.array2string(predict[0]))
        if(predict[0]==1):
            print("POSITIVE\n")
        else:
            print("NEGATIVE\n")
    elif line == 'Quit':
        break
