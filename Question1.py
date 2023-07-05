# Consider the below code to answer further questions:
# import numpy as np
# list_ = [ ‘1’ , ’2’ , ‘3’ , ‘4’ , ‘5’ ]
# array_list = np.array(object = list_)

# Q1. Is there any difference in the data type of variables list_ and array_list? If there is then write a code
# to print the data types of both the variables.

import numpy as np
list_ = [ '1' , '2' , '3' , '4' , '5' ]
array_list = np.array(object = list_)
print(array_list)
print(type(list_))
print(type(array_list))

# Yes there is difference between the both the variable and that's because list is converted non dimentional array