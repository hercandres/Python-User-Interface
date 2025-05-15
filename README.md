# Python-User-Interface
This repository stores code to process flexible CSV Data sets and display such information using matplotlib library.
During the process of building this code, some doubts and problems arose. These were solved by using python.org website. I find this not only a good resource to be able to complete my code, but also to learn new functions and to improve my abilities to find answers when I don’t have a teacher or mentor with me at the moment.
Data Set
For this project, I chose a dataset collected using a Uneekor golf simulator. Launch monitors provide a wide range of variables related to golf performance that can be analyzed.
The dataset is organized with the first column representing the club used for each repetition, followed by 11 additional variables describing the ball’s movement. My code not only calculates statistics and generates graphs for the collected variables, but it also accepts any CSV file where the first column contains a descriptive key. This flexibility means the tool is not limited to golf data but can be applied to any dataset.
Data Cleaning
First, I had to implement 3 data cleaning functions, these ones are in charge of deleting empty rows, getting rid of non-numerical rows, and changing mixed string-number cells to only number cells (ex. 3 L -> -3, 4 R -> 4).
Statistical Analysis
Using while loops, I designed a program to process any number of columns in the dataset and calculate the average and standard deviation for each column, grouped by the key—in this case, the golf club used. This while also returning instant data with the proper labels that are also obtained from the data set. Such values are stored within the first row of  the imported CSV file, and also the first element of every row. 
Data Visualization & Analysis 
The code offers two options for data analysis. First, it generates a summary in a text file, providing the average and standard deviation for each variable and club, giving users full access to the data. Second, it includes a visualization option that lets users view the progression of a variable across all clubs in the dataset or compare different variables using a scatter plot. These two different plots aloud the user to investigate and find relations between variables and general tendencies across all the golf clubs that were included in the data set.  
