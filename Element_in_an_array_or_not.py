n=int(input())
lst=list(map(int,input().split()))
key=int(input())
for i in range(n):
     if(key==lst[i]):
         print("True")
     else:
         print("False")
