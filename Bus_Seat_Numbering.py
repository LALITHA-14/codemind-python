# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    if n<=10:
        print("Lower Double")
    elif n>10 and n<=15:
        print("Lower Single")
    elif n>15 and n<=25:
        print("Upper Double")
    else:
        print("Upper Single")
