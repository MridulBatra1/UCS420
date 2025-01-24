A = {34, 56, 78, 90} 
B = {78, 45, 90, 23}
print("Union : ", A.union(B));
print("Intersection : ", A.intersection(B));
print("Symmetric difference : ", A-B);
print("Symmetric difference : ", B-A);
print("If A is subset of B ",A.issubset(B));
print("If B is subset of A ",B.issubset(A));
n = int(input("Enter the score you want to delete : "));
if(n in A):
    A.remove(n)
    print("After deletion : ", A);
else:
    print(n, "does not exist in Set A");
