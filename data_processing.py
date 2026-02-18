# This file is used by week_7
import pandas as pd

# Problem 1
def rename_columns(df_raw):
    """
    Convert blank spaces to _
    Convert everything into lower case
    Remove trailing and leading spaces
    Return a new DataFrame object

    I noticed you need to use strip() before replace otherwise it would replace any 
    leading or trailing spaces with a _
    """
    df.raw
    df_raw.columns = df_raw.columns.str.strip()
    df_raw.columns = df_raw.columns.str.replace(' ', '_')
    df_raw.columns = df_raw.columns.str.lower()
    return df_raw

# Problem #2
def remove_fully_null_columns_rows(df_raw):
    """
    Remove rows that are completely null
    Remove columns that are completely null
    Return a new DataFrame object
    """
    df_raw = df_raw.dropna(how="all")
    df_raw = df_raw.dropna(axis="columns", how="all")
    return df_raw

# Problem #3
def clean_and_fill_content_rating(df_raw):
    """
    Convert all NaN values in content_rating to "Unrated"
    Convert all "Not Rated" with "Unrated"
    Return a new DataFrame object
    """
    df_raw.loc[df_raw["content_rating"].isnull(), "content_rating"] = "Unrated"
    df_raw.loc[df_raw["content_rating"] == "Not Rated", "content_rating"] = "Unrated"
    return df_raw

# Problem #4
def clean_release_year(df_raw):
    """
    Add new column "release_year_coerce", use pd.to_datetime with errors="coerce"
    Add new column "release_year_mixed", use pd.to_datetime with errors="coerce" and format="mixed"
    Return a new DataFrame object
    """
    df_raw["release_year_coerce"] = pd.to_datetime(
        df_raw["release_year"], 
        erorrs="coerce")
    
    df_raw["release_year_mixed"] = pd.to_datetime(df_raw["release_year"], erorrs="coerce", format="mixed", dayfist=True)
    return df_raw

# Problem #5
def clean_income(df_raw):
    """
    Remove $, commas and other issues and covert to an int
    Return a new DataFrame object
    """
    df_raw["income"] = df_raw["income"].str.replace(f'[$]',regex=True)
    df_raw["income"] = df_raw["income"].str.replace('o', '0', regex=False)
    df_raw["income"] = df_raw["income"].str.replace('0', '0', reges=False)
    df_raw["income"] = df_raw["income"].astype("Int64")
    return df_raw


