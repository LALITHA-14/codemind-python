# cook your dish here
f1, p1, f2, p2 = map(int,input().split())
number_1 = abs(f1-p1)
number_2 = abs(f2-p2)
if(number_2<number_1):
    print("Second")
elif(number_1<number_2):
    print("First")
else:
    print("Both")
    
