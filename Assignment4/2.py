import numpy as np;
arr = np.array([1,2,3,6,4,5]);
print("Original array : ", arr);
arr1 = np.flip(arr);
print("The array after reversing is : ", arr1);

x = np.array([1,2,3,4,5,1,2,1,1,1]);
print("Original array : ", x);
a = np.bincount(x);
mode = np.argmax(a);
print("Most frequant number in array is : ", mode);
print("Index of most frequant element is ");
index = np.where(x == mode)[0];
print(index);

y = np.array([1, 1, 1, 2, 3, 4, 2, 4, 3, 3, ]);
print("Original array : ", y);
b = np.bincount(y);
mode1 = np.argmax(b);
print("Most frequant number in array is : ", mode1);
print("Index of most frequant element is ");
index1 = np.where(y == mode1)[0];
print(index1);