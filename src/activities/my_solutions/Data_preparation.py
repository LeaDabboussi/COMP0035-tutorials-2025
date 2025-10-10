import pandas as pd
import os

#Removing columns after creating dataframe
def removing_columns(dataframe, cols_to_remove):
    """
    This funciton removes the columns that are not rquired during analysis after the dataframe was created.

    Inputs:
    dataframe : the dataframe we want to create a copy of and alter
    cols_to_remove (list of strings) : specifies the list of columns we want to remove from the original dataframe

    Outputs:
    New cleaned up dataframe
    """
    
    df=dataframe.drop(columns=cols_to_remove)
    #print(df.columns)

    return df

##Intermediaire function
def missing_rows(dataframe):
    """
    This function returns the rows with the missing values.

    Input:
    Dataframe

    Output: 
    missing_val : Rows with missing values
    
    """
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
        #print(f"Here are the missing rows:\n {missing_rows}")
    
    return missing_rows 



#Resolve missing or incorrect values

def drop_missing_values(dataframe,missing_data):
    """
    This function removes rows with missing data and outputs a new dataframe.
    It also resets the indexes.
    Input:
    Dataframe
    Missing_data : rows with missing data 

    Ouput:
    df : cleaned dataframe
    """
    
    df=dataframe.drop(missing_data.index, axis=0)
    df=df.reset_index(drop=True)
    return df

##REPLACING anything with an uppercase with a lowecase and any whitespace

def replacing_lowecase_whitespace(dataframe,column):
    """
    This fucntion checks if the column has strings with leading 
    or trailing whitespace and removes it or has any uppercase 
    letters and turns the whoel word into lowercase.

    Input:
    Dataframe
    Column (str) : the column that needs to be cleaned

    Output:
    df : cleaned dataframe

    """

    df=dataframe.copy()
    for row_index in range(len(df[column])):
        value_to_check=df.at[row_index, column]
        if value_to_check == str:
            value_to_check=value_to_check.strip() #removing whitespace
            for character in value_to_check:
                if any(character.isupper()):
                    value_checked=value_to_check.lower()
                df=df.at[row_index,column] = value_checked       

    return df

# Change datatypes to specified one
def change_dtypes(dataframe,columns_change,data_type):
    """
    This function changes specified columsn data type into a specified datatype.

    Input:
    dataframe (pandas.dataframe)
    columns_change (list of str): columns that need changing data types of
    data_type (str): specified datatype to change to 
                ("float64", "int64", "Int64", "int", "DatetimeTZDtype")

    Output:
    df (pandas.dataframe): changed dataframe
    
    """
    if data_type == "DatetimeTZDtype":
       for col in columns_change:
        dataframe[col] = pd.to_datetime(dataframe[col], format='%d/%m/%Y')
        dataframe[col].dt.tz_localize('Europe/London')

    else: 
        for col in columns_change:
            dataframe[col] = dataframe[col].astype(data_type)

    df=dataframe

    return df

def object_to_string(dataframe):
    """
    This function changes object dattype columns to strings.

    Input:
    dataframe (pandas.dataframe): dataframe to change

    Output:
    df (pandas.dataframe): changed dataframe

    """
    for col in dataframe.columns:
        if dataframe[col].dtypes == "object":
            dataframe[col] = dataframe[col].astype("string")

    df = dataframe

    return df

def computing_duration(df):
    
    duration_values =(df['end'] - df['start']).dt.days.astype('Int64')
    df.insert(df.columns.get_loc('end') + 1, 'duration', duration_values)

    return df


#_________________________________________________________
# FINAL FUNCTION FOR DATA PREP
def df_clean(dataframe, input_file_type):
    """
    Cleans/prepares the dataframe for analysis and processing then 
    saves it as a csv or xlsx

    Input(csv or xlsx):
    Dataframe
    input_file_type (str): either "excel" or "csv"

    Output (csv or xlsx):
    Prepared dataset as a saved file.

    """

    cols=['URL','disabilities_included', 'highlights']
    new_df= removing_columns(dataframe,cols)
    #print(missing_rows(new_df))
    
    new_df=drop_missing_values(new_df,missing_rows(new_df))
    #print(new_df)
    
    new_df=replacing_lowecase_whitespace(new_df,"type")
    #print(new_df)
    
    columns_to_change= ['countries','events', 'participants_m', 'participants_f', 'participants']
    new_df= change_dtypes(new_df,columns_to_change,"int")
    #print(new_df)

    date_columns = ["start", "end"]
    new_df= change_dtypes(new_df,date_columns,"DatetimeTZDtype")
    
    #Showing entire dataset (no ...)
    # pd.set_option('display.max_rows', None)
    # pd.set_option('display.max_columns', None)
    #print(new_df)

    new_df = object_to_string(new_df)
    #print(new_df.dtypes)

    new_df = computing_duration(new_df)
    #print(new_df["duration"])



    #Save as csv
    # os.makedirs("data/outputs", exist_ok=True)
    # output_path = os.path.join("data/outputs", "paralympics_prepared.csv")
    # if input_file_type == "csv":
    #     new_df.to_csv(output_path, index=False)
    # elif input_file_type == "excel":
    #     new_df.to_excel(output_path, index=False)
    # else:
    #     print("Invalid output file type")

    # print("Cleaned data saved in data outputs.")
    
    # return new_df







## MAIN ____________________________________
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



    df_clean(paralympic_csv_df,"csv")
    
    
