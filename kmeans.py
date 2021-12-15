import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from numpy.core.fromnumeric import mean, size

np.set_printoptions(suppress=True)

read = pd.read_csv("vgsales.csv")
readerfull = pd.DataFrame(read)
reader = readerfull.loc[:,['NA_Sales','EU_Sales','JP_Sales']]

k = int(input("\nEnter k-value : "))

rand = np.array(reader.sample(k))
reader = np.array(reader)

count=1
rows,columns=reader.shape

def calc():
    dist=[]
    for i in range(k):
        for j in range(rows):
            temp=np.sqrt(np.sum(np.square(rand[i]-reader[j])))
            dist.append(temp)
    dist=np.array([dist])
    dist=np.transpose(dist.reshape(k,rows))

    distDF = pd.DataFrame(dist)
    mindist = distDF.idxmin(axis=1)

    global finalreader
    finalreader = readerfull.loc[:,['NA_Sales','EU_Sales','JP_Sales']]
    finalreader['mindist'] = mindist

    global meanarray
    meanarray = finalreader.groupby(['mindist']).mean()
    meanarray = np.array(meanarray)

calc()

while 1:
    if (rand == meanarray).all():
        print("Iteration "+str(count)+"\nData Clustered\nCentroid :")
        print(meanarray)

        fig = plt.figure(figsize = (20, 20))
        ax = plt.axes(projection ="3d")
        
        colors=['r','g','b','m','y','c','lime','darkorange','deeppink','maroon']
        for i in range(k):
            graphreader = finalreader.loc[finalreader['mindist'] == i]
            ax.scatter(graphreader['NA_Sales'], graphreader['EU_Sales'], graphreader['JP_Sales'], alpha=0.3, s=10, color=colors[i])

        plt.title('K-Means Cluster')
        ax.set_xlabel('NA_Sales')
        ax.set_ylabel('EU_Sales')
        ax.set_zlabel('JP_Sales')
        plt.show()
        break

    else:
        count += 1
        rand = meanarray
        calc()