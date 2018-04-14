# python-project
Programming &amp; Scripting module project on Fisher's Iris data set.

### Summary 
Fisher's Iris data set was established by British statistician Ronald Fisher in 1936 and it is one of the first standard models of statistical classification.  The data contains 50 samples of three types of Iris flowers (Iris setosa, Iris virginica and Iris versicolor) measured along four variables - the measurements in centimetres of sepal length, sepal width, petal length and petal width. It has become one of the most widely used data test cases for many statistical classification techniques. [Wikipedia](https://en.wikipedia.org/wiki/Iris_flower_data_set) <br>

While researching for this project I found a blog detailing some exercises (albeit in R) for this data set that I've borrowed as a guideline for a script I needed to write - Link (https://joelkuiper.eu/R-workshop).  My script demonstrating these exercises is saved in this repository as **Project1.py** <br>

###### Project1.py includes:
1.  Select only the rows of the Virginica flowers and assign it to virginica 
2.  Select only the Sepal Length of the Virginica flowers and assign it
3.  Calculate the mean, median, variance and standard deviation of the Virginica Sepal Length
4.  Select only the numerical columns
5.  Calculate the mean of all the numerical variables

Further online research led me to understand the need to import a library into my Python code to better facilitate this analysis, and I decided to try [Pandas](https://pandas.pydata.org/pandas-docs/stable/).  My understanding of this package is that it provides the means to efficiently analyse and model data as it incorporates the functionlity of NumPy and MatPlotLib as well as its own particular features. It is also already included in the version of Anaconda I have downloaded to my machine so it was relatively easy to "call it"! 

As I continued with this project I began to read more and more about NumPy and I decided to try incorporate it too, so I wrote a script that imported it which is saved in this repository as **Project2.py**.  

###### Project2.py includes code that calculates:
1. The average Sepal Length
2. The average Sepal Width
3. The average Petal Length
4. The average Petal Width
5. The average total length
6. The average total width
7. The standard deviation of total length 
8. The standard deviation of total width
9. Plots a histogram of Sepal Length measurements in red
10. Plots a histogram of Sepal Width measurements in blue
11. Plots a histogram of Petal Length measurements in green
12. Plots a histogram of Petal Width measurements in yellow
