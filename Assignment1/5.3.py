n = int(input("Enter a number: "));
sum = 0;
for i in range (2,n+1):
    flag = 0;
    for j in range(2,i):
        if i % j == 0:
            flag = 1;
            break;
    if flag != 1:
        sum += i;
print(sum);