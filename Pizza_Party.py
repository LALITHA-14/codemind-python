# cook your dish here
import math
a, b = map(int,input().split())
chef=a+1
boys=chef*4
girls=b*3
sum_of_boys_and_girls=boys+girls
print(math.ceil(sum_of_boys_and_girls/8))
