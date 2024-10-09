def max_area(N):
    if N < 4:
        return 0
    # Number of sides we can use
    side_sum = N // 2
    
    # Try to split side_sum into two parts as equally as possible
    length = side_sum // 2
    breadth = side_sum - length
    
    # Return the maximum area
    return length * breadth

# Input processing
T = int(input())  # Number of test cases
for _ in range(T):
    N = int(input())
    print(max_area(N))
