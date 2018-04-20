# python-project
Programming &amp; Scripting module project on Fisher's Iris data set.

### Summary of background information
Fisher's Iris data set was established by British statistician Ronald Fisher in 1936 and it is one of the first standard models of statistical classification.  The data contains 50 samples each of three types of Iris flowers (Iris setosa, Iris virginica and Iris versicolor) measured along four variables - the measurements in centimetres of sepal length, sepal width, petal length and petal width. It has become one of the most widely used data test cases for many statistical classification techniques- [Wikipedia](https://en.wikipedia.org/wiki/Iris_flower_data_set) <br>

While researching for this project I found a [blog](https://joelkuiper.eu/R-workshop) detailing some exercises (albeit in R) for this data set that I've borrowed as a guideline for a script to write to investigate the data. Further online research led me to understand the need to import a library into my Python code to better facilitate this analysis, and I first decided to try [Pandas](https://pandas.pydata.org/pandas-docs/stable/).  My understanding of this package is that it provides the means to efficiently analyse and model data as it incorporates the functionlity of NumPy and MatPlotLib as well as its own particular features. It is also already included in the version of Anaconda I have downloaded to my machine so it was easy to import it. 

My script demonstrating these exercises is saved in this repository as **Project1.py** <br>

### Project1.py includes code to:
1.  Select only the rows of the Virginica flowers and assign it to virginica 
2.  Select only the Sepal Length of the Virginica flowers and assign it
3.  Calculate the mean, median, variance and standard deviation of the Virginica Sepal Length
4.  Select only the numerical columns
5.  Calculate the mean of all the numerical variables

I spent a lot of time figuring out how to use Pandas, mainly from reading the [Pandas Tutorial](https://pandas.pydata.org/pandas-docs/stable/tutorials.html) which really helped me to understand data structures and indexing/selecting data within them, and in some cases by Googling specific issues I didn't know how to resolve and finding other users' advice on Stack Overflow, for example this [post](https://stackoverflow.com/questions/17018638/assigning-column-names-from-a-list-to-a-table) which I used as a guide for naming columns in a dataframe I created containing the Iris data set and also this [post](https://stackoverflow.com/questions/45225841/pandas-data-slicing-by-column-names) which gave me some insight into data slicing.

As I continued with this project I began to read more and more about [NumPy](http://www.numpy.org/) and I decided to try incorporate it too, so I wrote a script that imported it and [MatPlotLib](https://matplotlib.org/) which is saved in this repository as **Project2.py**.  

### Project2.py includes code that calculates:
1. The average Sepal Length
2. The average Sepal Width
3. The average Petal Length
4. The average Petal Width
5. The average total length
6. The average total width
7. The maximum Sepal Length
8. The minimum Sepal Length
9. The maximum Sepal Width
10. The minimum Sepal Width
11. The maximum Petal Length
12. The minimum Petal Length
13. The maximum Petal Width
14. The minimum Petal Length
15. The standard deviation of total length 
16. The standard deviation of total width
##### and also
17. Plots a histogram of Sepal Length measurements in red
18. Plots a histogram of Sepal Width measurements in blue
19. Plots a histogram of Petal Length measurements in green
20. Plots a histogram of Petal Width measurements in yellow
21. Plots a histogram showing above measurements in assigned colours

I found NumPy a little easier and more intuitive to use, perhaps using and learning Pandas helped with that.  When it came to writing code for maximum and minimum I found I didn't need to first check the [NumPy tutorial](https://docs.scipy.org/doc/numpy/user/quickstart.html) but just try "max" and "min". I did need to Google how to find the [standard deviation](https://docs.scipy.org/doc/numpy/reference/generated/numpy.std.html) and [how to label histograms](https://medium.com/python-pandemonium/data-visualization-in-python-histogram-in-matplotlib-dce38f49f89c). 

### References
###### Background Reading: 
* [https://en.wikipedia.org/wiki/Iris_flower_data_set]
* [http://www.jeannicholashould.com/tidy-data-in-python.html] 
* [http://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html] 
https://shapeofdata.wordpress.com/2013/10/01/case-study-1-iris/ 
https://machinelearningmastery.com/machine-learning-in-python-step-by-step/ 
https://joelkuiper.eu/R-workshop 

Project1.py
https://pythonhow.com/data-analysis-with-python-pandas/ - how to import pandas 
https://pandas.pydata.org/pandas-docs/stable/overview.html
https://pandas.pydata.org/pandas-docs/stable/dsintro.html - intro to data structures
https://pandas.pydata.org/pandas-docs/stable/indexing.html - indexing and selecting data
https://medium.com/@msalmon00/helpful-python-code-snippets-for-data-exploration-in-pandas-b7c5aed5ecb9 - for code to select columns 
https://stackoverflow.com/questions/45225841/pandas-data-slicing-by-column-names - data slicing
https://pythonhow.com/pandas-data-analysis-functions/ - mean for dataframes
https://pandas.pydata.org/pandas-docs/stable/basics.html - variance
http://pythonforengineers.com/introduction-to-pandas/ 
https://www.analyticsvidhya.com/blog/2016/01/12-pandas-techniques-python-data-manipulation/
https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html
https://towardsdatascience.com/a-quick-introduction-to-the-pandas-python-library-f1b678f34673 

Project2.py
https://docs.scipy.org/doc/numpy/user/quickstart.html - NumPy tutorial
https://docs.scipy.org/doc/numpy/reference/generated/numpy.std.html - standard deviation
https://medium.com/python-pandemonium/data-visualization-in-python-histogram-in-matplotlib-dce38f49f89c - labelling histogram axes

