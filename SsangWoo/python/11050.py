# 이항 계수 구하기
# (n r) = n! / (r!*(n-r)!)

from math import factorial
n, r = list(map(int, input().split()))
print(int(factorial(n)/(factorial(r)*factorial(n-r))))
