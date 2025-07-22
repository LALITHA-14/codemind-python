# cook your dish here
# Train Even or Odd
T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    odd_days_sum = sum(A[i] for i in range(0, N, 2))   # Days 1, 3, 5, ...
    even_days_sum = sum(A[i] for i in range(1, N, 2))  # Days 2, 4, 6, ...
    print(max(odd_days_sum, even_days_sum))
