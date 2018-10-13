# 중앙 1, 아래부터 시작해서 2 다음 3 4 5 6 7
# 그다음 8 9 10 주위돌면서...
# 1
# 2 3 4 5 6 7
# 8 9 10 11 12 13 14 15 16 17 18 19
# 20 ~ 37
# 38 ~ 61
# 1 (6) (12) (18) (24) -> 1+6*n 으로 증가
# 이때 근접한 방을 통해 몇개의 최소 갯수 방을 지나는가의 문제
# 1과 마지막 포함 거리 구해라
# 범위에 주의해야함
# 몇번째 범위에 있는 수인지 알아야 함
# 계속 더해서 n과 비교 후 거리 출력


def pr(n):
    if n == 1:
        return 1
    else:
        distance = 2
        beeHome = 1
        for mul in range(1, 18258):
            beeHome += 6 * mul
            if n > beeHome:
                distance += 1
            else:
                break
        return distance


# print(pr(int(input())))

# test

# 1+6*n이 1000000000 이하 만큼이 될 때의 n을 구하는 테스트
# n = 1
# count = 1
# while True:
#     n += 6 * count
#     if n > 1000000000:
#         print(count)
#         break
#     else:
#         count += 1

#
# for i in range(1, 99):
#     if i % 10 == 0:
#         print()
#     print("{}:{}".format(i, pr(i)), end=' ')
