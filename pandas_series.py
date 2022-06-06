import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fruits = pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"])

# 1. Determine the number of elements in fruits.

fruits.size
# 17

# 2. Output only the index from fruits.

fruits.index
# RangeIndex(start=0, stop=17, step=1)

# 3. Output only the values from fruits.

fruits.values
# array(['kiwi', 'mango', 'strawberry', 'pineapple', 'gala apple',
    #    'honeycrisp apple', 'tomato', 'watermelon', 'honeydew', 'kiwi',
    #    'kiwi', 'kiwi', 'mango', 'blueberry', 'blackberry', 'gooseberry',
    #    'papaya'], dtype=object)

# 4. Confirm the data type of the values in fruits.

fruits.dtype
# dtype('O')

# 5. Output only the first five values from fruits. Output the last three values.

fruits.head(5)
# 0          kiwi
# 1         mango
# 2    strawberry
# 3     pineapple
# 4    gala apple
# dtype: object

## Output the last three values.

fruits.tail(3)
# 14    blackberry
# 15    gooseberry
# 16        papaya
# dtype: object

## Output two random values from fruits.

fruits.sample(2)
# 6        tomato
# 7    watermelon
# dtype: object

# 6. Run the .describe() on fruits to see what information it returns when called on a Series with string values.

fruits.describe()
# count       17
# unique      13
# top       kiwi
# freq         4
# dtype: object

# 7. Run the code necessary to produce only the unique string values from fruits.

# fruits.value_counts().index
fruits.unique()
# array(['kiwi', 'mango', 'strawberry', 'pineapple', 'gala apple',
#        'honeycrisp apple', 'tomato', 'watermelon', 'honeydew',
#        'blueberry', 'blackberry', 'gooseberry', 'papaya'], dtype=object)

# 8. Determine how many times each unique string value occurs in fruits.

fruits.value_counts()
# kiwi                4
# mango               2
# strawberry          1
# pineapple           1
# gala apple          1
# honeycrisp apple    1
# tomato              1
# watermelon          1
# honeydew            1
# blueberry           1
# blackberry          1
# gooseberry          1
# papaya              1
# dtype: int64

# 9. Determine the string value that occurs most frequently in fruits.

# fruits.mode()
# fruits.value_counts().head(1)
# fruits.value_counts().nlargest(n=1).index[0]
fruits.value_counts().idxmax()

# # 'kiwi'

# 10. Determine the string value that occurs least frequently in fruits.

# fruits.value_counts().tail()
# fruits.value_counts().nsmallest(n=1, keep='all')
fruits.value_counts().idxmin()
# 'strawberry'