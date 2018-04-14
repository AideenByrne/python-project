
#Aideen Byrne 26th March 2018 
#Code for investigating Iris Data Set for Programming & Scripting module project 

#Select only the rows of the Virginica flowers and assign it to virginica 
import pandas as pd #import pandas library 
df1 = pd.read_csv("data/iris.csv")  #label contents of iris.csv file as dataframe
my_columns = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Species"] #borrowed from Jeff Tratner at https://stackoverflow.com/questions/17018638/assigning-column-names-from-a-list-to-a-table
df1.columns = my_columns
species = df1[["Species"]] #to select column named Species
virginica = df1.loc[(df1["Species"] == "Iris-virginica")] #select rows that contain virginica flowers in species column
print (virginica)#prints only rows that contain virginica flowers in species column

#Select only the Sepal Length of the Virginica flowers and assign it 
vsepallength = virginica["Sepal Length"]
print (vsepallength)

#Calculate the mean, median, variance and standard deviation of the Virginica Sepal Length
print ("The mean of Virginica Sepal Length is", vsepallength.mean())
print ("The median of Virginica Sepal Length is", vsepallength.median())
print ("The variance of Virginica Sepal Length is", vsepallength.var())
print ("The standard deviation of Virginica Sepal Length is", vsepallength.std())

#Select only the numerical columns
selectnumcol = df1[["Sepal Length", "Sepal Width", "Petal Length", "Petal Width"]]
print (selectnumcol)

#Calculate the mean of all the numerical variables
print ("The mean per numerical column is", selectnumcol.mean())
print ("The mean of all numerical columns is", selectnumcol.mean().mean())
