>**Note**: Please **fork** the current repository so that you will have a **remote** repository in **your** Github account. Clone the remote repository to your local machine.

![Bikeshare](divvy.jpg)
### Date created
>Created on the 13th of October 2023

### Project Title
## _Explore US Bikeshare Data_

### Description
#### Overview
In this project, we make use of **`Python` to explore data related to bike share systems for three major cities in the United States** namely; 
- Chicago 
- New York City
- Washington. 

We will write code to import the data and **compute descriptive statistics** about it. We will also write a script that takes in raw input to create an interactive experience in the terminal to present the said statistics.
In this project, We will use data provided by [Motivate]((https://motivateco.com/)), a bike share system provider for many major cities in the United State.

#### Software Needed
To complete this project, the following software requirements apply:
- `Python 3`, [`NumPy`](https://numpy.org/), and [`pandas`](https://pandas.pydata.org/) installed using `Anaconda`
- A text editor, like [`Sublime`](https://www.sublimetext.com/) or [`Atom`](https://github.blog/2022-06-08-sunsetting-atom/)
- A terminal application (Terminal on` Mac` and `Linux` or `Cygwin on Windows`).

### Installation of Software
Kindle note that Python, Numpy, and Pandas are included with [Anaconda](https://www.anaconda.com/download#downloads). Follow the link to install Anaconda as per your operating system. Window use can install and configure [Git](https://medium.com/@GalarnykMichael/install-git-on-windows-9acf2a1944f0) to run Python. 
##### Installing a specific version of Numpy or Pandas
- Install a version of choice for Numpy or Pandas as shown below
```
# Use either one command
conda install numpy=X.XX
conda install pandas=X.XX
pip install --upgrade numpy==X.XX
```
where `X.XX` is a specific version number

##### Importing Numpy and Pandas
- It's a common rule of thumb for import the Numpy and Pandas libraries as shown
```
import pandas as pd
import numpy as np
```
>In this project we used `Anaconda 23.7.4`having `Python 3.11.4`, `Numpy 1.24.3`, and `Pandas 1.5.3`.
Though there are a number of ways you can go about tackling this project, we recommend using NumPy and pandas. Using these libraries is the industry standard for working with data in Python.

##### Some useful pandas methods
```
df.head()
df.columns
df.describe()
df.info()
df['column_name'].value_counts()
df['column_name'].unique()
```
### The Datasets
Randomly selected data for the **first six months of 2017** are provided for all three cities. All three of the data files contain the same **core six (6) columns**:

- Start Time (e.g., 2017-01-01 00:07:57)
- End Time (e.g., 2017-01-01 00:20:53)
- Trip Duration (in seconds - e.g., 776)
- Start Station (e.g., Broadway & Barry Ave)
- End Station (e.g., Sedgwick St & North Ave)
- User Type (Subscriber or Customer)

The Chicago and New York City files also have the following two columns:
- Gender
- Birth Year

#### Interactive Experience
The `bikeshare.py` file is set up as a script that takes in raw input to create an interactive experience in the terminal that answers questions about the dataset. The experience is interactive because depending on a user's input, the answers to the questions on the previous page will change! There are four questions that will change the answers:
- Would you like to see data for Chicago, New York, or Washington?
- Would you like to filter the data by month, day, or not at all? 
- (If they chose month) Which month - January, February, March, April, May, or June?
- (If they chose day) Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?

The answers to the questions above will determine the city and timeframe on which We'll do data analysis. After filtering the dataset, users will see the statistical result of the data, and choose to start again or exit.

Before choosing to start again or exit, the script will reuests to display 5 rows of the raw data of the filtered dataset. The request is repeqted to display more rows in multiples of 5. 

### Files used
The data files of the 3 cities used for the project are the following `.csv` files
```
chicago.csv
new_york_city.csv
washington.csv
```

### Credits
Our acknowledgements go to:
 - **[Motivate]((https://motivateco.com/)), a bike share system provider for many major cities in the United State, from where our data was obatianed**
 - **The entire Udacity Team for the amazing skills dished out**
 - **Advanced Africa and Access Bank for the Scholarship Opportunity**

