list = ["apple", "banana", "apple", "orange", "banana", "apple"]
print(list)
d = {}
sum = 1
for i in list:
    if i in d:
        d[i] += 1
    else:
        d[i] = sum
print(d)
