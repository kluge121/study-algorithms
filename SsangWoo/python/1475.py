# 방 번호가주어졌을 때 필요한 세트 개수
# 6->9, 9->6 가능

from collections import Counter
from math import ceil

N = list(input())
countDict = dict(Counter(N))
countDict.setdefault('6', 0)
countDict.setdefault('9', 0)
min69 = ceil((countDict['6'] + countDict['9']) / 2)
countDict['6'] = countDict['9'] = 0
maxValue = max(countDict.values())

print(maxValue if maxValue > min69 else min69)
