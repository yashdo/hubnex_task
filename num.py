
import numpy as np
Numpy is Numerical Python.
It is a library consisting of multidimensional array objects and a collection of routines for processing of array.

Numpy Functions
array1 = np.array([[1,2,3,4],[5,6,7,8]])
array1
array([[1, 2, 3, 4],
       [5, 6, 7, 8]])
# np.zeros
array2 = np.zeros((4,3) , dtype=int)   # Default dtype = float
array2
array([[0, 0, 0],
       [0, 0, 0],
       [0, 0, 0],
       [0, 0, 0]])
# np.ones
array3 = np.ones((2,3) , dtype=int)
array3
array([[1, 1, 1],
       [1, 1, 1]])
# np.arange
array4 = np.arange(6,20,2)
array4
array([ 6,  8, 10, 12, 14, 16, 18])
# linspace
# to get the number of evenly spaced values between intervals
# Parameters for the function - np.linespace(start, stop, num, endpoint, retstep, dtype)
array5 = np.linspace(10,20,5)
array5
array([10. , 12.5, 15. , 17.5, 20. ])
# random
# to get an array with random input integral elements of desired shape
# Parameters for the function - np.full(start,end,size)
array6 = np.random.randint(0,25,size=(3,4))
print(array6)
[[15 11 22 24]
 [ 2  4  5 22]
 [ 2 22 20  6]]
# np.full
# To get an array with specified input element of desired shape
# Parameters for the function - np.full(shape,value)
array7 = np.full((3,2,2),5)
print(array7)
[[[5 5]
  [5 5]]

 [[5 5]
  [5 5]]

 [[5 5]
  [5 5]]]
# identity
# to get an identity matrix
array8 = np.identity(4)
print(array8)
[[1. 0. 0. 0.]
 [0. 1. 0. 0.]
 [0. 0. 1. 0.]
 [0. 0. 0. 1.]]
# asarray
# convert list to ndarray
list_ = [1,2,3]
array9 = np.asarray(list_)
array9
array([1, 2, 3])
a = np.random.randint(1,5,(2,4))
a
array([[3, 4, 3, 2],
       [4, 4, 2, 4]])
b = np.random.randint(5,10,(2,4))
b
array([[7, 6, 6, 7],
       [7, 9, 5, 5]])
# Multiply
np.multiply(a,b)
array([[21, 24, 18, 14],
       [28, 36, 10, 20]])
# Divide 
np.divide(a,b)
array([[0.42857143, 0.66666667, 0.5       , 0.28571429],
       [0.57142857, 0.44444444, 0.4       , 0.8       ]])
# divide
divide = np.divide(10,2)
div
5.0
# multiplication
multiply = np.multiply(186, 200)
multiply
37200
Aggregation Operations
data = np.random.randint(1,10,(2,4))
data
array([[9, 2, 7, 4],
       [5, 4, 9, 9]])
# Sum
print(np.sum(data)) 
print(np.sum(data,axis=0))
print(np.sum(data,axis=1))
49
[14  6 16 13]
[22 27]
data.max()
9
data.min()
2
Numpy array attributes
ndarray.shape
This returns a tuple consisting of array dimensions.
array_1 = np.array([[1,2,3],[4,5,6]])
print(array_1.shape)
(2, 3)
array_2 = np.array([[[1,2,3],[4,5,6]],
                       [[1,2,3],[4,5,6]],
                       [[1,2,3],[4,5,6]],
                       [[1,2,3],[4,5,6]]])
print(array_2.shape)
(4, 2, 3)
ndarray.ndim
This returns the number of array dimensions.
array_3 = np.array([[1,2,3],[4,5,6]])
print(f"The dimension of array_3: ",array_3.ndim)
The dimension of array_3:  2
ndarray.size
This returns the total number of elements in the array
array_4 = np.array([[1,2,3],[4,5,6]])
print(f"The total number of elements in array_4 =  {array_4.size}")
The total number of elements in array_4 =  6
ndarray.dtype
This returns the data type of the array
array_5 = np.array([1,2,3,4,5])
print(array_5.dtype)
int32
array_6 = np.array([1,2,3,4,5,5.678,-6])
print(array_6.dtype)
float64
ndarray.astype
This changes the data type of an array.
array_7 = np.array([2,3,4])
print(array_7.dtype)
print(array_7)
array_7_ = array_7.astype('float64')
print(array_7_.dtype)
print(array_7_)
int32
[2 3 4]
float64
[2. 3. 4.]
Array Manipulation
np.transpose(array)
array_8 = np.array(np.random.randint(1,6,(6,2)))
array_8
array([[5, 1],
       [5, 3],
       [4, 5],
       [4, 1],
       [2, 3],
       [2, 2]])
transpose_arr = np.transpose(array_8)
transpose_arr
array([[5, 5, 4, 4, 2, 2],
       [1, 3, 5, 1, 3, 2]])
np.reshape(array,shape)
To Change shape of an array
array_9 = np.array(np.random.randint(1,6,(6,2)))
array_9
array([[2, 3],
       [3, 1],
       [4, 1],
       [2, 4],
       [4, 1],
       [4, 3]])
new_shape = (3,2,2)
reshaped_arr = np.reshape(array_9,new_shape)
reshaped_arr
array([[[2, 3],
        [3, 1]],

       [[4, 1],
        [2, 4]],

       [[4, 1],
        [4, 3]]])
flatten
array_10 = np.array(np.random.randint(1,6,(6,2)))
array_10
array([[2, 1],
       [1, 3],
       [4, 1],
       [4, 4],
       [3, 4],
       [1, 5]])
array_10.flatten()
array([2, 1, 1, 3, 4, 1, 4, 4, 3, 4, 1, 5])
 