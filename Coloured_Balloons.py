t = int(input())  # Number of test cases

for _ in range(t):
    n = int(input())  # Number of balloon colours
    arr = list(map(int, input().strip().split()))  # Number of balloons bought for each colour

    # Safety check: arr should have exactly n elements
    if len(arr) != n:
        raise ValueError(f"Expected {n} numbers, got {len(arr)}")

    # Total cost calculation
    total_cost = sum((i + 1) * arr[i] for i in range(n))
    print(total_cost)
