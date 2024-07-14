# Using pandas, write a Python function to clean and preprocess a given DataFrame, which involves handling missing values, normalizing numerical columns, and encoding categorical columns.

import pandas as pd
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.impute import SimpleImputer

def preprocess_dataframe(df):
    # Separate numerical and categorical columns
    numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns

    # Handle missing values for numerical columns (fill with median)
    num_imputer = SimpleImputer(strategy='median')
    df[numerical_cols] = num_imputer.fit_transform(df[numerical_cols])

    # Handle missing values for categorical columns (fill with most frequent)
    cat_imputer = SimpleImputer(strategy='most_frequent')
    df[categorical_cols] = cat_imputer.fit_transform(df[categorical_cols])

    # Normalize numerical columns using Min-Max scaling
    scaler = MinMaxScaler()
    df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

    # Encode categorical columns using one-hot encoding
    df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

    return df

# Example usage:
# Assume `data` is a pandas DataFrame that you want to preprocess
# data = pd.read_csv('your_dataset.csv')
# cleaned_data = preprocess_dataframe(data)
# print(cleaned_data.head())
