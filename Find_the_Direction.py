# cook your dish here
t=int(input())
directions = ["North","East","South","West"]
for i in range(t):
    x=int(input())
    facing_direction=directions[x%4]
    print(facing_direction)
