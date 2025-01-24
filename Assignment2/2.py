t = (45, 89.5, 76, 45.4, 89, 92, 58, 45);
a = max(t);
print("Maximum element of tuple is",a,"and its index is",t.index(a));
b = min(t);
print("Minimum element of tuple is",b,"and it appears",t.count(b),"times");
l = list(t);
print(l);
if(76 in t):
    print(t.index(76));
else:
    print("Not present");