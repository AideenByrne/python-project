#Aideen Byrne 26th March 2018 
#Code for investigating Iris Data Set for Programming & Scripting module project 
#Select only the rows of the Virginica flowers and assign it to virginica 

import pandas as pd #import pandas library 
df1 = pd.read_csv("data/iris.csv")  #label contents of iris.csv file as dataframe
my_columns = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Species"] #borrowed from Jeff Tratner at https://stackoverflow.com/questions/17018638/assigning-column-names-from-a-list-to-a-table
df1.columns = my_columns
species = df1[["Species"]] #to select column named Species
virginica = isin(["Iris-virginica"]) #need to fix this - trying to select virginica flowers from species column
print (virginica)