import sys;
print(sys.argv);
sum = 0;
for s in sys.argv[1:]:
    sum = sum + int(s);
print(sum);