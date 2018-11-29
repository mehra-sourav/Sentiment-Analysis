import matplotlib.pyplot as plt
import numpy as np


n=3
SVM=(78.25,86.64,87.388)
NB=(77.75,83.07,83.431)

fig,ax=plt.subplots()
index=np.arange(n)
bar_width=0.35
opacity=0.8

rects1=plt.bar(index,SVM,bar_width, alpha=opacity, color='#4f81bc',label='SVM')
rects1=plt.bar(index+bar_width,NB,bar_width, alpha=opacity, color='#c0504e',label='NB')

plt.xlabel('Datasets')

plt.ylabel('Accuracy')

plt.title("Accuracy Comparison")
plt.xticks(index+bar_width-0.15,('1600 Reviews Dataset','10000 Reviews Dataset','25000 Reviews Dataset'))
plt.legend()
plt.tight_layout()
plt.show()