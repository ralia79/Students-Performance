# creator des : ali roshan nia in student number : 9813114105



# import library

import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv(r'./exams.csv')

print("head of dataset :")
print(df.head())
print("\n")



# change columns name for quick access to data
print("change columns name")
df=df.rename(columns={"race/ethnicity":"race_ethnicity","parental level of education":"Education","test preparation course":"test_preparation_course","math score":"math_score","reading score":"reading_score","writing score":"writing_score"})
print(df.head())
print("\n")

print("tail of dataset" )
print(df.tail())
print("\n")

print("describe of dataset")
print(df.describe()) 
print("\n")


print("data types : ")
print(df.dtypes)
print("\n")

print("num of null data in dataset")
print(df.isnull().sum())
print("\n")

print("shapes : ")
print(df.shape)
print("\n")


print("column name of dataset : ")
print(df.columns)
print("\n")

# histogram chart
df.hist()


# Define an array of columns name
category1 = ["gender","race_ethnicity","Education","lunch","test_preparation_course"]


# boxplot for all col
def bar_plot(variable):
    var = df[variable]
    varValue = var.value_counts()
    plt.figure(figsize =(5,5))
    plt.bar(varValue.index, varValue)
    plt.xticks(varValue.index, varValue.index.values,rotation=45)
    plt.title(variable)
    plt.show()
    


for item in category1:
    bar_plot(item)



# count plot for all col 
def Count_plot(variable ):
    sns.countplot(data=df,x=variable)
    plt.show()


for col in category1 :
    Count_plot(col)    


# circle grap for all col

def circle_plot(data) : 
    labels = df[data].value_counts().index
    sizes = df[data].value_counts()
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
    ax1.axis('equal') 
    plt.show()

for item in category1 : 
    circle_plot(item)