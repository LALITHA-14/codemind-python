lst = [12, 17, 16, 94, -12]
key = 100
for i in range(len(lst)):
    if lst[i] == key:
        print("Found")
        break
else: 
    print("Not Found")
