# 1. Run python -m pip install pymysql from your terminal to install the mysql client (any folder is fine)

# 2. cd into your exercises folder for this module and run echo env.py >> .gitignore

# 3. Create a function named get_db_url. It should accept a username, hostname, password, and database name and return a url connection string formatted like in the example at the start of this lesson.

import pandas as pd

# 4. Use your function to obtain a connection to the employees database.
from env import host, user, password

get_db_url = f'mysql+pymysql://{user}:{password}@{host}/employees'

pd.read_sql('SELECT * FROM employees LIMIT 5 OFFSET 50', get_db_url)

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