import random as r;
A = list(range(100,901));
L = r.sample(A,100);
even = 0;
odd = 0;
prime = 0;
for i in L:
    flag = 0;
    for j in range(2,i):
        if(i % j == 0):
            flag = 1;
            break;
    if(flag == 0):
        prime = prime + 1;
        print(i,end = " ");
print("No of prime numbers are",prime);
print("\n");
for i in L:
    if(i % 2 == 0):
        even = even + 1;
    elif(i % 2 == 1):
        odd = odd + 1;
print("No of even numbers are",even);
for i in L:
    if(i % 2 == 0):
        print(i,end = " ");
print("\n");
print("No of odd numbers are",odd);
for i in L:
    if(i % 2 == 1):
        print(i,end = " ");