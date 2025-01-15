import pandas as pd

#A Series is a one-dimensional object containing a sequence of values, very similar to a column of data in an Excel spreadsheet. 
# The Series data structure has an associated index which can be either numbers, or strings (ie. named labels).

series_obj = pd.Series([10,20,30,40,50])
print(series_obj)
print(series_obj[0])

# A label can be used to identify each data point (row) by providing a list of the desired labels to the index property of the Series object.
series_obj = pd.Series([10,20,30,40,50], index = ["CA", "FL", "NY", "PA", "TX"])
print(series_obj)

print(series_obj["CA":"TX"]) #When selecting a slice of entries using named labels, the end point (stopping point) is inclusive.

# If you're requesting more than one label (index), they must be placed within a list:

print(series_obj[["CA", "NY", "TX"]])

# Creating a sample DataFrame using a dictionary of lists of values.

data = {"Name": ["Tim Miller", "Ann Carter", "Ellen Lee", "Sam Carr", "Al Ball", "Carl Zee", "Sara Martin"], 
        "Gender": ["Male", "Female", "Female", "Male", "Male", "Male", "Female"],
        "Age": [32, 44, 21, 19, 45, 27, 39]}
df = pd.DataFrame(data)

print(df)

# The head() method is used to display only the first 5 rows.

print(df.head()) # == df.head(5)
# The tail() method is used to display only the last 5 rows.

print(df.tail())  # == df.tail(5)

# Returns a column/Series object

print(df['Name'])     # Dictionary notation

# You can also use dot notation to retrieve a column (Series) from a DataFrame, 
# but only if the column name is a valid Python variable name (e.g., no spaces):
df.Name     # Attribute (dot) notation

# You can determine the order of your columns by placing the names in a list, in the desired order:
print(df[["Age", "Gender", "Name"]])    