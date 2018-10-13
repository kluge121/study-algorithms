# 정문부터 걸어서 가장 짧은 거리의 방 선호
# W개 방 있는 H층 건물(1~99)
# 엘리베이터 가장 왼쪽
# 같은 거리면 아래층 방 더 선호
# 그냥 나머지와 나눗셈으로 풀 수 있는 문제였다

for i in range(int(input())):
    H, W, N = list(map(int, input().split()))

    floor = (N-1) % H + 1
    unit = int((N-1) / H) + 1

    print("{}{:02d}".format(floor, unit))
