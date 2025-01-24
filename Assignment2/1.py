l = [10,20,30,40,50,60,70,80];
print("Original list is",l);
l.append(200);
l.append(300);
print("List after appending elements is",l);
l.remove(10);
l.remove(30);
print("List after removing elements is",l);
l.sort();
print("List after sorting in ascending order is",l);
l.sort(reverse=True)
print("List after sorting in descending order is",l);