def get_lcm(a, b):
    # generating multiples of any one of these numbers
    for i in range(1, b+1):
        m = a*i
        if m%b == 0:
            return m
def my_lcm(*nums):
    lcm = 1
    for i in nums:
        lcm = get_lcm(lcm, i)
    return lcm
print(my_lcm(10, 20))
