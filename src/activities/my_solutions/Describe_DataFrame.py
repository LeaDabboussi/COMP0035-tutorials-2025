import pandas as pd
import matplotlib.pyplot as plt

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
