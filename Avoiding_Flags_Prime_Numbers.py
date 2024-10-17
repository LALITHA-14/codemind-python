# prime or not 
# Trying to run the loop from 2 to n-1
n = int(input()) # 7 
for i in range(2,n): # 2, 3, 4, 5, 6
    if n % i == 0: # 10 % 2 == 0
        print("Not Prime")
        break
else:
    print("Prime")
