# Importing necessary libraries
import pandas as pd  # Importing pandas to work with DataFrames
from sklearn.impute import SimpleImputer  # Importing SimpleImputer to handle missing data

# Example DataFrame with missing values
data = {'Age': [25, None, 30, 22, None], 'Salary': [50000, 60000, None, 40000, 35000]}
# Creating a dictionary with 'Age' and 'Salary' columns, where 'None' represents missing values

df = pd.DataFrame(data)  # Converting the dictionary into a pandas DataFrame
print(df)  # Printing the original DataFrame with missing values

# Handling missing values by filling with the mean
imputer = SimpleImputer(strategy='mean')  # Initializing the SimpleImputer to fill missing values with the mean
# The strategy='mean' argument specifies that missing values will be replaced by the column mean

df['Age'] = imputer.fit_transform(df[['Age']])  # Applying the imputer to the 'Age' column and updating it with the filled values
# fit_transform() computes the mean and replaces missing values in the 'Age' column with that mean

df['Salary'] = imputer.fit_transform(df[['Salary']])  # Similarly, applying the imputer to the 'Salary' column
# The missing values in the 'Salary' column are replaced by the computed mean

print(df)  # Printing the updated DataFrame with missing values filled
