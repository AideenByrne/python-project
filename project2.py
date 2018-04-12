#Aideen Byrne 10th April 2018
#Using Numpy library to analyse Fisher's Iris data set

import numpy as np #imports numpy library
data = np.genfromtxt("data/iris.csv", delimiter = ',') #numpy opens iris.csv file
firstcol = data[:,0] #selects first column of file
print (np.mean(firstcol))#prints mean of first column
secondcol = data[:,1]
print (np.mean(secondcol))
thirdcol = data[:,2]
print (np.mean(thirdcol))
fourthcol = data[:,3]
print (np.mean(fourthcol))
all = np.array([firstcol, secondcol, thirdcol, fourthcol])#builds array of of all columns
print (np.mean(all)) #prints mean of all columns
print (max(firstcol))#prints max of first column
print (min(firstcol))#prints mean of first column
print (max(secondcol))
print (min(secondcol))
print (max(thirdcol))
print (min(thirdcol))
print (max(fourthcol))
print (min(fourthcol))
print (np.std(all))#finds standard deviation of all columns
import matplotlib.pyplot as plot #need to fix this!!
print (plot.hist(standarddev))