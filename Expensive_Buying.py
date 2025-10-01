# cook your dish here
import sys

data = sys.stdin.read().strip().split()
t = int(data[0])
idx = 1   # start reading after t
for _ in range(t):
    n = int(data[idx]); k = int(data[idx+1])
    idx += 2
    prices = list(map(int, data[idx:idx+n]))
    idx += n
    prices.sort(reverse=True)
    print(sum(prices[:k]))
