# cook your dish here
t = int(input())
for i in range(t):
    x, y = map(int,input().split())
    chef_floor = (x-1)//10
    chefina_floor = (y-1)//10
    print(abs(chefina_floor-chef_floor))
        
