# Exercise 1
# 1. Run python -m pip install pymysql from your terminal to install the mysql client (any folder is fine)

# 2. cd into your exercises folder for this module and run echo env.py >> .gitignore

# 3. Create a function named get_db_url. It should accept a username, hostname, password, and database name and return a url connection string formatted like in the example at the start of this lesson.

import pandas as pd

# 4. Use your function to obtain a connection to the employees database.
from env import host, user, password

get_db_url = f'mysql+pymysql://{user}:{password}@{host}/employees'

pd.read_sql('SELECT * FROM employees LIMIT 5 OFFSET 50', get_db_url)

# def get_db_url(username, hostname, password, database_name):
#     return f'mysql+pymysql://{user}:{password}@{host}/(database_name)'
    
# url = get_db_url(username, host, password, 'employees')
# # pd.read_sql(query, url)

# 5. Once you have successfully run a query:
## a. Intentionally make a typo in the database url. What kind of error message do you see?

pd.read_sql('SELECT * FROM employees LIMIT 5 OFFSET 50', get_db_url)
# OperationalError

## b. Intentionally make an error in your SQL query. What does the error message look like?

pd.read_sql('SELECT FROM employees LIMIT 5 OFFSET 50', get_db_url)
# ProgrammingError

# 6. Read the employees and titles tables into two separate DataFrames.
query = '''
SELECT *
FROM employees
'''
employees = pd.read_sql(query, get_db_url)
employees

query = '''
SELECT *
FROM titles
'''
titles = pd.read_sql(query, get_db_url)
titles

# 7. How many rows and columns do you have in each DataFrame? Is that what you expected?

# employees: 300024 rows
# titles: 443308 rows

# 8. Display the summary statistics for each DataFrame.

employees.describe(include = 'all')
# 	emp_no 	birth_date 	first_name 	last_name 	gender 	hire_date
# count 	300024.000000 	300024 	300024 	300024 	300024 	300024
# unique 	NaN 	4750 	1275 	1637 	2 	5434
# top 	NaN 	1952-03-08 	Shahab 	Baba 	M 	1985-06-20
# freq 	NaN 	95 	295 	226 	179973 	132
# mean 	253321.763392 	NaN 	NaN 	NaN 	NaN 	NaN
# std 	161828.235540 	NaN 	NaN 	NaN 	NaN 	NaN
# min 	10001.000000 	NaN 	NaN 	NaN 	NaN 	NaN
# 25% 	85006.750000 	NaN 	NaN 	NaN 	NaN 	NaN
# 50% 	249987.500000 	NaN 	NaN 	NaN 	NaN 	NaN
# 75% 	424993.250000 	NaN 	NaN 	NaN 	NaN 	NaN
# max 	499999.000000 	NaN 	NaN 	NaN 	NaN 	NaN

titles.describe(include = 'all')
#  	emp_no 	title 	from_date 	to_date
# count 	443308.000000 	443308 	443308 	443308
# unique 	NaN 	7 	6393 	5888
# top 	NaN 	Engineer 	1998-10-25 	9999-01-01
# freq 	NaN 	115003 	132 	240124
# mean 	253075.034430 	NaN 	NaN 	NaN
# std 	161853.292613 	NaN 	NaN 	NaN
# min 	10001.000000 	NaN 	NaN 	NaN
# 25% 	84855.750000 	NaN 	NaN 	NaN
# 50% 	249847.500000 	NaN 	NaN 	NaN
# 75% 	424891.250000 	NaN 	NaN 	NaN
# max 	499999.000000 	NaN 	NaN 	NaN

# 9. How many unique titles are in the titles DataFrame?

len(titles.groupby(by = 'title'))
# there are 7 unique titles

# 10. What is the oldest date in the to_date column?

titles.sort_values(by = 'to_date').head(1)
# 	emp_no 	title 	from_date 	to_date
# 16064 	20869 	Engineer 	1985-02-17 	1985-03-01
## 1985-03-01


# 11. What is the most recent date in the to_date column?

titles.sort_values(by = 'to_date', ascending = False).head(1)
#  	emp_no 	title 	from_date 	to_date
# 0 	10001 	Senior Engineer 	1986-06-26 	9999-01-01
## now


# ----------------------------------------------------------------
# Exercise 2
# 1. Copy the users and roles DataFrames from the examples above.

users = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6],
    'name': ['bob', 'joe', 'sally', 'adam', 'jane', 'mike'],
    'role_id': [1, 2, 3, 3, np.nan, np.nan]
})
users

roles = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['admin', 'author', 'reviewer', 'commenter']
})
roles

# 2. What is the result of using a right join on the DataFrames?

users.merge(roles, left_on='role_id', right_on='id', how='right', indicator=True)
#  	id_x 	name_x 	role_id 	id_y 	name_y 	_merge
# 0 	1.0 	bob 	1.0 	1 	admin 	both
# 1 	2.0 	joe 	2.0 	2 	author 	both
# 2 	3.0 	sally 	3.0 	3 	reviewer 	both
# 3 	4.0 	adam 	3.0 	3 	reviewer 	both
# 4 	NaN 	NaN 	NaN 	4 	commenter 	right_only

# 3. What is the result of using an outer join on the DataFrames?

users.merge(roles, left_on='role_id', right_on='id', how='outer', indicator=True)
#  	id_x 	name_x 	role_id 	id_y 	name_y 	_merge
# 0 	1.0 	bob 	1.0 	1.0 	admin 	both
# 1 	2.0 	joe 	2.0 	2.0 	author 	both
# 2 	3.0 	sally 	3.0 	3.0 	reviewer 	both
# 3 	4.0 	adam 	3.0 	3.0 	reviewer 	both
# 4 	5.0 	jane 	NaN 	NaN 	NaN 	left_only
# 5 	6.0 	mike 	NaN 	NaN 	NaN 	left_only
# 6 	NaN 	NaN 	NaN 	4.0 	commenter 	right_only

# 4. What happens if you drop the foreign keys from the DataFrames and try to merge them?

users.merge(roles, how='inner', on='id').drop(columns='role_id')

# 5. Load the mpg dataset from PyDataset.

from pydataset import data
mpg = data('mpg')
mpg

# 6. Output and read the documentation for the mpg dataset.

data('mpg', show_doc = True)

# 7. How many rows and columns are in the dataset?

mpg.shape
# 234 columns x 11 rows

# 8. Check out your column names and perform any cleanup you may want on them.

mpg.columns
# Index(['manufacturer', 'model', 'displ', 'year', 'cyl', 'trans', 'drv', 'cty',
#        'hwy', 'fl', 'class'],
#       dtype='object')

# 9. Display the summary statistics for the dataset.

mpg.describe()
#  	displ 	year 	cyl 	cty 	hwy
# count 	234.000000 	234.000000 	234.000000 	234.000000 	234.000000
# mean 	3.471795 	2003.500000 	5.888889 	16.858974 	23.440171
# std 	1.291959 	4.509646 	1.611534 	4.255946 	5.954643
# min 	1.600000 	1999.000000 	4.000000 	9.000000 	12.000000
# 25% 	2.400000 	1999.000000 	4.000000 	14.000000 	18.000000
# 50% 	3.300000 	2003.500000 	6.000000 	17.000000 	24.000000
# 75% 	4.600000 	2008.000000 	8.000000 	19.000000 	27.000000
# max 	7.000000 	2008.000000 	8.000000 	35.000000 	

# 10. How many different manufacturers are there?

len(mpg.groupby('manufacturer'))
# 15

# 11. How many different models are there?

len(mpg.groupby('model'))
# 38

# 12. Create a column named mileage_difference like you did in the DataFrames exercises;
# this column should contain the difference between highway and city mileage for each car.

mpg['mileage_difference'] = mpg['hwy']-mpg['cty']

# 13. Create a column named average_mileage like you did in the DataFrames exercises;
# this is the mean of the city and highway mileage.

mpg['average_mileage'] = (mpg['cty'] + mpg['hwy']) /2

# 14. Create a new column on the mpg dataset named is_automatic that holds boolean values denoting whether the car has an automatic transmission.

mpg['is_automatic'] = (mpg['trans'].str.contains('auto'))
mpg.head()

# 15. Using the mpg dataset, find out which which manufacturer has the best miles per gallon on average?

bestmiles = mpg.groupby('manufacturer')[['average_mileage','manufacturer']].mean().sort_values(by='average_mileage', ascending = False)
bestmiles.head()
# honda

# 16. Do automatic or manual cars have better miles per gallon?

better = mpg.groupby('is_automatic')[['trans', 'average_mileage']].mean()
better.head()
# Yes

# 	average_mileage
# is_automatic 	
# False 	22.227273
# True 	19.130573


# ----------------------------------------------------------------
# Exercise 3
# 1. Use your get_db_url function to help you explore the data from the chipotle database.

get_db_url = f'mysql+pymysql://{user}:{password}@{host}/chipotle'
query = '''
SELECT *
FROM orders
'''
chipo = pd.read_sql(query, get_db_url)
chipo

# 2. What is the total price for each order?

changetype = lambda x: float(x[1:-1])
chipo['item_price'] = chipo['item_price'].apply(changetype) 
chipo.head()

chipo['total'] = chipo['quantity']*chipo['item_price']
chipo.groupby(by = ['order_id']).total.sum()
# order_id
# 1       11.56
# 2       33.96
# 3       12.67
# 4       21.00
# 5       13.70
#         ...  
# 1830    23.00
# 1831    12.90
# 1832    13.20
# 1833    23.50
# 1834    28.75

# 3. What are the most popular 3 items?

chipo.groupby('item_name').quantity.sum().sort_values(ascending = False).head(3)
# item_name
# Chicken Bowl           761
# Chicken Burrito        591
# Chips and Guacamole    506

# 4. Which item has produced the most revenue?

chipo.groupby('item_name').total.sum().sort_values(ascending = False).head()
# Chicken Bowl           8044.63

# 5. Join the employees and titles DataFrames together.

et = employees.merge(titles, how = 'inner', left_on = 'emp_no', right_on = 'emp_no')
et

# 6. For each title, find the hire date of the employee that was hired most recently with that title.

et.groupby('title').from_date.max()

# 7. Write the code necessary to create a cross tabulation of the number of titles by department. (Hint: this will involve a combination of SQL code to pull the necessary data and python/pandas code to perform the manipulations.)

query = '''
SELECT e.emp_no, t.title, d.dept_name
FROM employees AS e
    JOIN titles AS t USING(emp_no)
    JOIN dept_emp AS de USING(emp_no)
    JOIN departments as d USING(dept_no)
'''

dept_emp_titles = pd.read_sql(query, get_db_url)
dept_emp_titles
pd.crosstab(dept_emp_titles.dept_name, dept_emp_titles.title, margins=True)
# title 	Assistant Engineer 	Engineer 	Manager 	Senior Engineer 	Senior Staff 	Staff 	Technique Leader 	All
# dept_name 								
# Customer Service 	298 	2362 	4 	2027 	13925 	16150 	309 	35075
# Development 	7769 	58135 	2 	49326 	1247 	1424 	7683 	125586
# Finance 	0 	0 	2 	0 	12139 	13929 	0 	26070
# Human Resources 	0 	0 	2 	0 	12274 	14342 	0 	26618
# Marketing 	0 	0 	2 	0 	13940 	16196 	0 	30138
# Production 	6445 	49649 	4 	42205 	1270 	1478 	6557 	107608
# Quality Management 	1831 	13852 	4 	11864 	0 	0 	1795 	29346
# Research 	378 	2986 	2 	2570 	11637 	13495 	393 	31461
# Sales 	0 	0 	2 	0 	36191 	41808 	0 	78001
# All 	16721 	126984 	24 	107992 	102623 	118822 	16737 	489903