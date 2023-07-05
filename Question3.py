# Consider the below code to answer further questions:
# import numpy as np
# list_ = [ ‘1’ , ’2’ , ‘3’ , ‘4’ , ‘5’ ]
# array_list = np.array(object = list_)


# Q3. Considering the following changes in the variable, array_list:
# array_list = np.array(object = list_, dtype = int)
# Will there be any difference in the data type of the elements present in both the variables, list_ and
# array_list? If so then print the data types of each and every element present in both the variables, list_
# and arra_list.

import numpy as np
list_ = [ '1' , '2' , '3' , '4' , '5' ]
array_list = np.array(object = list_)
array_list = np.array(object = list_, dtype = int)


# Yes there is change in the array_list now as the dytpe is changed to int while converting a string list to int array 

print(type(list_[0]))
print(type(list_[1]))
print(type(list_[2]))
print(type(list_[3]))
print(type(list_[4]))
print(type(array_list[0]))
print(type(array_list[1]))
print(type(array_list[2]))
print(type(array_list[3]))
print(type(array_list[4]))