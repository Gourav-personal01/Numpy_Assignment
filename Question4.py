# Consider the below code to answer further questions:
# import numpy as np
# num_list = [ [ 1 , 2 , 3 ] , [ 4 , 5 , 6 ] ]
# num_array = np.array(object = num_list)

# Q4. Write a code to find the following characteristics of variable, num_array:
# (i) shape
# (ii) size

import numpy as np
num_list = [ [ 1 , 2 , 3 ] , [ 4 , 5 , 6 ] ]
num_array = np.array(object = num_list)

shape_of_num_array = np.shape(num_array)
print(shape_of_num_array)

size_of_num_array = np.size(num_array)
print(size_of_num_array)