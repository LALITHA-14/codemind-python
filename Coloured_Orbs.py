# cook your dish here
R, B = map(int, input().split())
pairs = min(R, B)
skill = 5 * pairs + (R - pairs) * 1 + (B - pairs) * 2
print(skill)
