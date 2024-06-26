#******** Start type hinting
from typing import Optional
#******** Slutt type hinting

import os
import sys # For testing
#
import pandas as pd
import re
import datetime as dt


def get_class_of_series(series: pd.Series) -> str:
    return series.dtype.type.__name__


def extract_class_name(text: str) -> Optional[str]:
    match = re.search(r"<class '([^']+)'>", text)
    if match is None:
        raise Exception(f"No class is found")
    
    return match.group(1)


def get_classes_from_dtypes(dtypes: pd.Series) -> dict:
    class_dict = {}
    for col in dtypes.index:
        class_dict[col] =  extract_class_name(str(dtypes[col].type))
    #
    return class_dict


#Memo to self: "get_data_type_from_values" only works if the pandas series has length > 0
def get_data_type_from_values(values: pd.Series) -> Optional[str]:
    if len(values.dropna()) == 0:
        raise ValueError("Cannot deduce data type from values when there are no non-missing values")
    
    data_type = list(set([extract_class_name(str(elem.__class__)) for elem in values.dropna()]))    
    return data_type[0]



# Some simple utility functions. Assign "NA" to columns
def robust_get_data_type_from_values(df: pd.DataFrame) -> dict:
    data_types : dict =  {}
    for col in df.columns:
        data_types[col] = None
        values = df[col].dropna()
        if len(values.dropna()) > 0 :
            data_types[col] = get_data_type_from_values(values)
    #
    return data_types
            
def find_date_columns(df: pd.DataFrame,robust: bool = True) -> list:
    data_types = robust_get_data_type_from_values(df)
    date_cols = [col for col in data_types if data_types[col] == "datetime.date"]
    return date_cols
# 
      
    