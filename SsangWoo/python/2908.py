A, B = input().split()
AR = ''.join(list(A)[::-1])
BR = ''.join(list(B)[::-1])
print(AR if AR > BR else BR)
