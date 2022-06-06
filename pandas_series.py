# exercise part 1

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

# 'kiwi'

# 10. Determine the string value that occurs least frequently in fruits.

# fruits.value_counts().tail()
# fruits.value_counts().nsmallest(n=1, keep='all')
fruits.value_counts().idxmin()
# 'strawberry'

# exercise part 2

# 1. Capitalize all the string values in fruits.

fruits.str.upper()
# 0                 KIWI
# 1                MANGO
# 2           STRAWBERRY
# 3            PINEAPPLE
# 4           GALA APPLE
# 5     HONEYCRISP APPLE
# 6               TOMATO
# 7           WATERMELON
# 8             HONEYDEW
# 9                 KIWI
# 10                KIWI
# 11                KIWI
# 12               MANGO
# 13           BLUEBERRY
# 14          BLACKBERRY
# 15          GOOSEBERRY
# 16              PAPAYA
# dtype: object

# 2. Count the letter "a" in all the string values (use string vectorization).

fruits.str.count('a').sum()
# 14

# 3. Output the number of vowels in each and every string value.

## method a
# vowel_counts = pd.Series(0, index = range(17), dtype = 'int')
# vowels = ['a','e','i','o','u']

# for vowel in vowels:
#     vowel_counts += fruits.str.count(vowel)


## method b
# def vowel_counter(string):
#     counter = 0
#     for char in string:
#         if char in 'aeiou':
#             counter += 1
#     return counter


## method c
fruits.str.count(r'[aeiou]')
# 0     2
# 1     2
# 2     2
# 3     4
# 4     4
# 5     5
# 6     3
# 7     4
# 8     3
# 9     2
# 10    2
# 11    2
# 12    2
# 13    3
# 14    2
# 15    4
# 16    3
# dtype: int64

# 4. Write the code to get the longest string value from fruits.

fruits[fruits.str.len().idxmax()]
# 'honeycrisp apple'

# 5. Write the code to get the string values with 5 or more letters in the name.

morethanfive = fruits.str.len() > 5
fruits[morethanfive]
# 2           strawberry
# 3            pineapple
# 4           gala apple
# 5     honeycrisp apple
# 6               tomato
# 7           watermelon
# 8             honeydew
# 13           blueberry
# 14          blackberry
# 15          gooseberry
# 16              papaya
# dtype: object

# 6. Find the fruit(s) containing the letter "o" two or more times.

omorethantwo = fruits.str.count('o') >= 2
fruits[omorethantwo]
# 6         tomato
# 15    gooseberry
# dtype: object

## using lambda
fruits[fruits.apply(lambda fruit: fruit.count('o')> 1)]

# 7. Write the code to get only the string values containing the substring "berry".

substr = 'berry'
fruits[fruits.str.contains(substr)]
# 2     strawberry
# 13     blueberry
# 14    blackberry
# 15    gooseberry
# dtype: object

# 8. Write the code to get only the string values containing the substring "apple".

substr = 'apple'
fruits[fruits.str.contains(substr)]
# 3           pineapple
# 4          gala apple
# 5    honeycrisp apple
# dtype: object

# 9. Which string value contains the most vowels?

vowel = fruits.str.count('[aeiou]')
fruits[vowel.idxmax()]
# honeycrisp apple

# exercise part 3

# Use pandas to create a Series named letters from the following string.

letters = pd.Series(list('hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy'
))

# 1. Which letter occurs the most frequently in the letters Series?

letters.value_counts().idxmax()
# 'y'

# 2. Which letter occurs the Least frequently?

letters.value_counts().nsmallest(n=1, keep='all')
# l    4
# dtype: int64

# 3. How many vowels are in the Series?

letters.str.count('[aeiou]').sum()
# 34

# 4. How many consonants are in the Series?

letters.str.count('[bcdfghjklmnpqrstvwxzy]').sum()
# 166

# 5. Create a Series that has all of the same letters but uppercased.

letters.str.upper()
# 0      H
# 1      N
# 2      V
# 3      I
# 4      D
#       ..
# 195    R
# 196    O
# 197    G
# 198    U
# 199    Y
# Length: 200, dtype: object

# 6. Create a bar plot of the frequencies of the 6 most commonly occuring letters.

letters.value_counts().nlargest(n=5, keep='all')
# y    13
# p    12
# w    10
# b     9
# n     9
# k     9
# m     9
# dtype: int64

letters.value_counts().nlargest(n=5, keep='all').plot.bar()

# Use pandas to create a Series named numbers from the following list:

numbers = pd.Series(['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23'])

