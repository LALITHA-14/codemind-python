t = int(input())
for _ in range(t):
    A, B = map(int, input().split())
    if (B - A) % 3 <= 1:
        print("YES")
    else:
        print("NO")
