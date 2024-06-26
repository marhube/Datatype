import pandas as pd


from typing import Optional

def get_class_of_series(series: pd.Series) -> str: ...
def extract_class_name(text: str) -> Optional[str]: ...
def get_classes_from_dtypes(dtypes: pd.Series) -> dict: ...
def get_data_type_from_values(values: pd.Series) -> Optional[str]: ...
def robust_get_data_type_from_values(df: pd.DataFrame) -> dict: ...
def find_date_columns(df: pd.DataFrame,robust: bool = True) -> list: ...
