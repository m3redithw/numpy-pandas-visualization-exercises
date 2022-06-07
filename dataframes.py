import pandas as pd
import numpy as np

from pydataset import data

# 1. Copy the code from the lesson to create a dataframe full of student grades.

np.random.seed(123)

students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']

# randomly generate scores for each student for each subject
# note that all the values need to have the same length here
math_grades = np.random.randint(low=60, high=100, size=len(students))
english_grades = np.random.randint(low=60, high=100, size=len(students))
reading_grades = np.random.randint(low=60, high=100, size=len(students))

df = pd.DataFrame({'name': students,
                   'math': math_grades,
                   'english': english_grades,
                   'reading': reading_grades})

type(df)

## a. Create a column named passing_english that indicates whether each student has a passing grade in english.

df['passing_english'] = df.english >= 70
df

## b. Sort the english grades by the passing_english column. How are duplicates handled?

df.sort_values(by='passing_english')[['english','passing_english']]

## c. Sort the english grades first by passing_english and then by student name.
## All the students that are failing english should be first, and within the students that are failing english they should be ordered alphabetically.
## The same should be true for the students passing english.
## (Hint: you can pass a list to the .sort_values method)

df.sort_values(by = ['passing_english', 'name'])[['name', 'english', 'passing_english']]

## d. Sort the english grades first by passing_english, and then by the actual english grade, similar to how we did in the last step.

df.sort_values(by = ['passing_english', 'english'])[['name', 'english', 'passing_english']]

## e. Calculate each students overall grade and add it as a column on the dataframe.
## The overall grade is the average of the math, english, and reading grades.

df['overall_grade'] = (df.math + df.english + df.reading)/3
df.head()

# 2. Load the mpg dataset. Read the documentation for the dataset and use it for the following questions:

data('mpg', show_doc = True)

mpg = data('mpg')
mpg

## How many rows and columns are there?

# 234 rows x 11 columns

## What are the data types of each column?

mpg.dtypes
# manufacturer     object
# model            object
# displ           float64
# year              int64
# cyl               int64
# trans            object
# drv              object
# cty               int64
# hwy               int64
# fl               object
# class            object
# dtype: object

## Summarize the dataframe with .info and .describe
mpg.info()

mpg.describe()

## Rename the cty column to city.
## Rename the hwy column to highway.

mpg = mpg.rename(columns = {'cty': 'city'}).rename(columns = {'hwy': 'highway'})

## Do any cars have better city mileage than highway mileage?

# mpg.head()
mpg[mpg.city > mpg.highway]

# No

## Create a column named mileage_difference this column should contain the difference between highway and city mileage for each car.

mpg['mileage_difference'] = mpg.highway - mpg.city
mpg.head()

## Which car (or cars) has the highest mileage difference?

mpg.sort_values(by='mileage_difference', ascending = False)

# honda civic 2008

## Which compact class car has the lowest highway mileage? The best?

mpg[mpg['class'] == 'compact'].sort_values(by='highway').head(1)

# 220 	volkswagen 	jetta 	2.8 	1999 	6 	auto(l4) 	f 	16 	23 	r 	compact 	7

mpg[mpg['class'] == 'compact'].sort_values(by='highway', ascending = False).head(1)

# 213 	volkswagen 	jetta 	1.9 	1999 	4 	manual(m5) 	f 	33 	44 	d 	compact 	11

## Create a column named average_mileage that is the mean of the city and highway mileage.

mpg['average_mileage'] = (mpg.city + mpg.highway) / 2
mpg.head(5)

## Which dodge car has the best average mileage? The worst?

mpg[mpg['manufacturer'] == 'dodge'].sort_values(by='average_mileage', ascending = False).head(1)

# 38 	dodge 	caravan 2wd 	2.4 	1999 	4 	auto(l3) 	f 	18 	24 	r 	minivan 	6 	21.0

mpg[mpg['manufacturer'] == 'dodge'].sort_values(by='average_mileage').head(1)

# 70 	dodge 	ram 1500 pickup 4wd 	4.7 	2008 	8 	manual(m6) 	4 	9 	12 	e 	pickup 	3 	10.5

# 3. Load the Mammals dataset. Read the documentation for it, and use the data to answer these questions:
data('Mammals', show_doc = True)

m = data('Mammals')
m

## How many rows and columns are there?

m.shape

# 107 rows x 4 columns

## What are the data types?

m.dtypes
# weight      float64
# speed       float64
# hoppers        bool
# specials       bool
# dtype: objec

## Summarize the dataframe with .info and .describe
m.info()

m.describe()

## What is the the weight of the fastest animal?

m.sort_values(by='speed', ascending = False)[['weight', 'speed']].head(1)

# 55.0

## What is the overal percentage of specials?

percentage = m[m['specials'] == True].count() / 107 * 100
percentage

# 9.35%

# How many animals are hoppers that are above the median speed? What percentage is this?

m['median_speed'] = m['speed'].median()

m.head()

m[(m['speed']>m['median_speed']) & (m['hoppers'] == True)].shape

# 7

median_percentage = 7 / 107 * 100
median_percentage

# 49.53%