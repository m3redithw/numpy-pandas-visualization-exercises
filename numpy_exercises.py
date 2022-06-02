import numpy as np

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

# 1. How many negative numbers are there?
a[a < 0]
# array([-2, -1, -6, -7]) --- 4

# 2. How many positive numbers are there?
a[a > 0]
# array([ 4, 10, 12, 23,  3]) --- 5

# 3. How many even positive numbers are there?
a[(a > 0) & (a % 2 == 0)]
# array([ 4, 10, 12]) --- 3

# 4. If you were to add 3 to each data point, how many positive numbers would there be?
addthree = a + 4
len(addthree[a > 3])
# --- 4

# 5. If you squared each number, what would the new mean and standard deviation be?
squared = a  ** 2
squared.mean()
# --- 74.9

squared.std()
# --- 144.024

# 6.
# A common statistical operation on a dataset is centering. 
# This means to adjust the data such that the mean of the data is 0.
# This is done by subtracting the mean from each data point. Center the data set.

a.mean()

minuesmean = a-a.mean()
minuesmean.mean()

# 7. Calculate the z-score for each data point.
zscore = (a-a.mean())/a.std()
zscore
# array([ 0.12403473,  0.86824314,  1.11631261,  2.48069469, -0.62017367,
    #    -0.49613894, -0.3721042 , -0.3721042 , -0.3721042 , -1.11631261,
    #     0.        , -1.24034735])