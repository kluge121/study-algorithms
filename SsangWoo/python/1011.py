# 이동거리를 급격하게 늘릴 경우 결함이 생기기때문에
# 이전에 k 광년 이동했을때는 k-1 ~ k+1 밖에 이동
# x지점 y지점 최소한 작동거리
# **y에 도착하기 전에는 반드시 1광년** 이어야 함
# 베스킨라벤스31과 비슷한 문제.
#
# k광년씩 움직였어도 도착 전에 1광년이 되어야함
# 작동 횟수 최솟값을 구해야 하는 것이므로 처음도 1광년이어야 함
# 그럼 1-> 2-> 3 ... 순으로 가능 줄일때도 3 -> 2 -> 1 순으로만 가능
#
# 직접 이동하려면 엄청난 계산량이 필요하기 때문에
# 무조건 최소화 해야함
# 최대한 갈 수 있는 거리를 늘린 다음 마지막에 1로 될 수 있는 경우를
# 찾아야 함
#
# 사다리꼴 모양으로 만들면 된다
# http://blog.naver.com/occidere/220982644540의 사진 참고

from math import pow

for i in range(int(input())):
    x, y = list(map(int, input().split()))
    distance = y - x

    powDistance = int(pow(distance, 0.5))
    if distance > powDistance**2 + powDistance:
        powDistance += 1

    criterion = powDistance * 2 - 1
    if distance <= powDistance**2:
        print(criterion)
    else:
        print(criterion+1)
