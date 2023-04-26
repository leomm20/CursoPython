import numpy as np

ndarray = np.ones((3, 4))
print(ndarray)
print(ndarray[0][0])
print()

ndarray = np.full((3, 4), 2.55)
print(ndarray)
print(ndarray[0][0])
print()

ndarray = np.arange(3, 19, 3)
print(ndarray)
print(ndarray[0])
print()

ndarray = np.random.random((3, 3))
print(ndarray)
ndarray3 = np.copy(ndarray)
print(ndarray3)
print(np.all(ndarray == ndarray3))
print()

ndarray = np.random.random((3, 3))
print(ndarray)
ndarray3 = np.copy(ndarray)
print(ndarray3)
print(ndarray + ndarray3)
print()

