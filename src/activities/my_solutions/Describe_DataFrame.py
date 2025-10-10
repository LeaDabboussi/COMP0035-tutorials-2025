import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

def describe_dataframe(dataframe):
    """This function describes the data in the DataFrame.
    Parameters:
    dataframe : dataframe name as read by pandas (csv or xlsx)
    Returns:
    None (This function does not return a value, only prints the description.)
    """
    #Number of rows and columns in data
    rows,columns= dataframe.shape
    print(f"The number of rows and columns respectively are {rows} and {columns}.")
    #First 5 rows and last 5 rows
    pd.set_option("display.max_columns", None) #changing pandas settings to see all columns
    print("The first and last rows respectively are: \n"+ str(dataframe.head(5)) +"\n" + "and " + str(dataframe.tail(5))+".")
    #Print the column labels
    print("The column labels are:")
    print(list(dataframe.columns))
    # Print the column datatypes
    print(f"The column datatypes are : \n {dataframe.dtypes}.")
    # Print the info
    dataframe.info()
    # Print the results of describe
    print(dataframe.describe())


## MISSING VALUES _____________________________________________

def missing_values(dataframe):
    """This function describes the quality of the dataframe by identifying missing values.
    Parameters:
    dataframe : dataframe name as read by pandas (csv or xlsx)
    Returns:
    None (This function does not return a value, only prints the description.)
    """

    ## Copy of dataset that shows only the rows with missing values
    
    # Missing rows
    num_missing_rows = dataframe.isna().any(axis=1).sum()
    missing_rows = dataframe[dataframe.isna().any(axis=1)]

        # Printing missing rows if present.
    if num_missing_rows == 0:
        print ("There are no missing rows.")
    else:
        if num_missing_rows ==1:
            print(f"There is {num_missing_rows} missing row.")
        else: 
            print(f"There are {num_missing_rows} missing rows.")
        print(f"Here are the missing rows:\n {missing_rows}")

    # Missing columns

    num_missing_columns = dataframe.isna().any(axis=0).sum()
    missing_columns = dataframe.loc[:,dataframe.isna().any(axis=0)]
    #missing_column_index = dataframe.columns[dataframe.isna().any()]
    
        # Printing missing columns if present.
    if num_missing_columns == 0:
        print ("There are no missing columns.")
    else:
        if num_missing_columns ==1:
            print(f"There is {num_missing_columns} missing column.")
        else: 
            print(f"There are {num_missing_columns} missing columns.")
        print(f"Here are the missing columns:\n {missing_columns}")

##Plots__________________________________________________________

def histogram(dataframe, columns):
    """
    Plots histogram from certain columns specified from the dataframe

    Input:
    dataframe: dataframe specified
    columns (list of str) : lsit of columns to plot. the columns must contain numerical data
    
    Output:
    The fucntion displays a histogram plot on a figure.
    """
    dataframe[columns].plot.hist()
    plt.show()

def boxplot(dataframe):
    """
    Creates Box plots to help to get an idea of the data distribution which in turn 
    helps us to identify the outliers more easily.

    input:
    dataframe

    Output:
    This function creates a figure with the desired box plots (numerical columns in dataset)

    """
    # dataframe[variables].boxplot()
    # plt.show()
    numerical_columns = dataframe.select_dtypes(include='number').columns
    num_columns = len(numerical_columns)
    ncols = 4  # number of columns per row
    nrows = math.ceil(num_columns / ncols)

    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(5*ncols, 5*nrows))
    axes = axes.flatten()
    
    for i, col in enumerate(numerical_columns):
        dataframe.boxplot(column=col, ax=axes[i])
        axes[i].set_title(col)
    plt.show()


def timeseries(dataframe, x, male_participants, female_participants):
    """
    Time series comparing male and female participants over a time.

    Inputs:
    dataframe : dataset containing participant data.
    x (str): column name for  x-axis
    male_participants : str : male participant number
    female_participants : str: female participant number.
    
    Output:
    This function does not return a value; only a plot.
    """
    plt.figure(figsize=(10, 5))
    plt.plot(dataframe[x], dataframe[male_participants], marker='o', label='Male')
    plt.plot(dataframe[x], dataframe[female_participants], marker='o', label='Female')

    plt.title("Male vs Female Participants Over Time")
    plt.xlabel(x)
    plt.ylabel("Number of Participants")
    plt.grid(True)
    plt.legend()
    ax = plt.gca()
    ax.set_xticks(ax.get_xticks()[::4])  # limiting bumber of labels on the x axis
    plt.show()


## Indentifying values in categorical data

def unique_values(dataframe,colname):
    print(dataframe[colname].unique())
    print(dataframe[colname].value_counts())






## MAIN_____________________________

if __name__ == "__main__":
    # path to csv or excel sheet
    from importlib.resources import files
    paralympics_raw_csv = files("activities.data").joinpath("paralympics_raw.csv")
    student_data_raw_csv = files("activities.data").joinpath("student_data.csv")
    npc_codes_raw_csv = files("activities.data").joinpath("npc_codes.csv")

    # Read the data from the files
    paralympic_csv_df = pd.read_csv(paralympics_raw_csv)
    student_data_csv_df = pd.read_csv(student_data_raw_csv)
    npc_codes_csv_df = pd.read_csv(npc_codes_raw_csv)

    # Describing dataframe using function defined above
    # describe_dataframe(paralympic_csv_df)
    # describe_dataframe(student_data_csv_df)
    # describe_dataframe(ncp_codes_csv_df)

    # missing_values(paralympic_csv_df)
    # missing_values(student_data_csv_df)
    # missing_values(ncp_codes_csv_df)
    
    #histogram(paralympic_csv_df, ["participants_m","participants_f"])
    #The distributions don’t really tell you much in this dataset. It may be more useful for larger datasets.

    #boxplot(paralympic_csv_df)
    #timeseries(paralympic_csv_df, "start", "participants_m", "participants_f")

    #unique_values(paralympic_csv_df,"type")