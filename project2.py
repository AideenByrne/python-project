#Aideen Byrne 10th April 2018
#Using Numpy library to analyse Fisher's Iris data set

import numpy as np #imports numpy library
data = np.genfromtxt("data/iris.csv", delimiter = ',') #numpy opens iris.csv file
firstcol = data[:,0] #selects first column of file
print ("The average Sepal Length is:", np.mean(firstcol))#prints mean of first column
secondcol = data[:,1]
print ("The average of Sepal Width is:", np.mean(secondcol))
thirdcol = data[:,2]
print ("The average Petal Length is:", np.mean(thirdcol))
fourthcol = data[:,3]
print ("The average Petal Width is:", np.mean(fourthcol))
fifthcol = data[:,4]
alllength = np.array([firstcol, thirdcol])#builds array of data related to length measurements
allwidth = np.array([secondcol, fourthcol])#builds array of data related to width
print ("The average of all length measurements is:", np.mean(alllength)) #prints mean of all length measurements
print ("The average of all width measurements is:", np.mean(allwidth)) #prints mean of all width measurements
print ("The maximum Sepal Length is:", max(firstcol))#prints max of first column
print ("The minimum Sepal Length is:", min(firstcol))#prints mean of first column
print ("The maximum Sepal Width is:", max(secondcol))
print ("The minimum Sepal Width is:", min(secondcol))
print ("The maximum Petal Length is:", max(thirdcol))
print ("The minimum Petal Length is:", min(thirdcol))
print ("The maximum Petal Width is:", max(fourthcol))
print ("The minimum Petal Width is:", min(fourthcol))
print ("The standard deviation of length measurement is:", np.std(alllength))#finds standard deviation of all length measurements
print ("The standard deviation of all width measurements is:", np.std(allwidth))#finds standard deviation of all width measurements

#to generate histogram representations of data 
import matplotlib.pyplot as pl
pl.hist(firstcol, color="red")#calls histogram of first column and displays in red
pl.ylabel("Frequency")#labels y axis of histogram
pl.xlabel("Sepal Length")#labels x axis of histogram
pl.show()#shows histogram
pl.hist(secondcol, color="blue")
pl.ylabel("Frequency")
pl.xlabel("Sepal Width")
pl.show()
pl.hist(thirdcol, color="green")
pl.ylabel("Frequency")
pl.xlabel("Petal Length")
pl.show()
pl.hist(fourthcol, color="yellow")
pl.ylabel("Frequency")
pl.xlabel("Petal Width")
pl.show()

#To generate histogram representation of all measurements
x = [firstcol]
y = [secondcol]
z = [thirdcol]
w = [fourthcol]

pl.hist(x, label="Sepal Length", color="red")
pl.hist(y, label="Sepal Width", color="blue")
pl.hist(z, label="Petal Length", color="green")
pl.hist(w, label="Petal Width", color="yellow")
pl.legend(loc='upper right')
pl.show()


