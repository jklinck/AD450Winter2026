def rename_columns(df_raw):
    """
    Problem #1
    Convert blank spaces to _
    Convert everything into lower case
    Remove trailing and leading spaces
    Return a new DataFrame object
    """
    return 1

def remove_fully_null_columns_rows():
    """
    Problem #2
    Remove rows that are completely null
    Remove columns that are completely null
    Return a new DataFrame object
    """
    return 1

def clean_and_fill_content_rating():
    """
    Problem #3
    Convert all NaN values in content_rating to "Unrated"
    Convert all "Not Rated" with "Unrated"
    Return a new DataFrame object
    """
    return 1

def clean_release_year():
    """
    Problem #4
    Add new column "release_year_coerce", use pd.to_datetime with errors="coerce"
    Add new column "release_year_mixed", use pd.to_datetime with errors="coerce" and format="mixed"
    Return a new DataFrame object
    """
    return 1

def clean_income():
    """
    Problem #5
    Remove $, commas and other issues and covert to an int
    Return a new DataFrame object
    """
    return 1


