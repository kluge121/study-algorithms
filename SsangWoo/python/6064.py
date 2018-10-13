# M과 N보다 작거나 같은 두개의 x,y 를 <x:y> 형식으로 표현
# 첫번째 해 <1:1> 두번째 해 <2:2>
# 지금 해 <x:y> 다음 해 <x':y'> 일 때,
#
# x < M -> x' = x + 1
# x >= M -> x' = 1
#
# y < N -> y' = y + 1
# y >= N -> y = 1
#
# <M:N> -> 종-말
#
# 예) M:10 N:12
#
# 1 1 -> 1
# 2 2 -> 2
# 3 3 -> 3
# ...
# 10 10 -> 10
# 1 11 -> 11
# 2 12 -> 12
# 3 1 -> 13
#
# 각각 뺑뺑이를 도는데, 예를 보면 되는지 안되는지 확인도 해야한다.
# 처음 든 생각은 각 자릿수를 계속 뺑뻉이 도는 완전 탐색법이었으나
# 입력의 수를 보니 40000 이하였다. 이는 최악의 경우 40000*40000
# -> O(N^2)인데, 시간 제한은 1초기 때문에 안 될 것이라 판단했다.
# 그리고 T의 크기를 안알려줬다... 무진장 큰 수도 나올 것 같았다.
#
# 두번쨰 든 생각은 '계산식을 만들어야겠다'였다.
# 일단 M과 N은 modulo로 활용이 될 것이고, 일단 M과 N이 둘 다
# 크기가 다를 수 있으니 M이 큰 경우, 같은 경우, N이 큰 경우 세가지로
# 나누기로 했다.
#
# M이 큰 경우엔 숫자가 아마 M의 크기에 따라 의존을 하게 될 것이라 생각햇다.
# 예제의 입력에서의 <13:11>, <5:6>? 을 주먹구구로 한 번 시도해보았다.
#
# 13 11
# 5 6
# 1 1   -> 1
# 11 11 -> +10 11
# 13 2  -> +2 13
# 1 3    -> +1 14
# 9 11  -> +8 22
# 13 4 -> +4 26
# 1 5  -> +1 27
# ...
#
# 괜히 했다는 생각이 들었다. 식을 만들기가 여간 힘들 것 같았고,
# 알고 보니 한 숫자에만 의존하지 않고 서로 의존하는 것을 알 수 있었다.
#
# 뭔가 식 하나로 딱 해결될 수 있을 것 같다는 느낌은 있지만,
# 일단 안 될 것 같다고 생각했던 완전탐색을 해보기로 했다.
#
# ```Python
# for _ in range(int(input())):
#     M, N, x, y = list(map(int, input().split()))
#
#     # <1:1> 부터 시작
#     tryX, tryY = 1, 1
#     # 카운트
#     count = 1
#     # 반복
#     while True:
#         # x 증가
#         if tryX < M:
#             tryX += 1
#         elif tryX >= M:
#             tryX = 1
#         # y 증가
#         if tryY < N:
#             tryY += 1
#         elif tryY >= N:
#             tryY = 1
#
#         # 카운트 증가
#         count += 1
#
#         # 찾으려는 수와 동일하면 횟수 리턴
#         # 아니면 카운트 증가
#         if tryX == x and tryY == y:
#             print(count)
#             break
#
#         # 끝까지 했을 경우 -1 출력후 종료
#         if tryX == M and tryY == N:
#             print(-1)
#             break
#
# ```
#
# 시간 측정도 해봤다. M, N, x, y를 모두 40000으로 해본 결과
# 내 컴퓨터의 CPU는 i5 8세대이기 떄문에... 소용이 없었다(ㅎㅎ;)
# 그래도 혹시나 해서 백준에 올려본 결과... 당연하다는 듯 시간초과가 떴닼ㅋ
#
# 그래서 일단 이 코드를 기반으로 좀 고쳐보자는 생각이 들었다.
# 완전 탐색보다는 크기를 좀 줄여보기로 했다.
# 위에서 시도했던 M이 1일 때의 경우로 한 번 도전해봤다.
# 그런데 문제는, M만큼 좀 더 빠르게 올라가는 대신에 어떻게 답을
# 찾아낼 것인가? 라는 생각이 들었다.
# 아니! 다시 생각해보니 **tryX를 주어진 x일 때 의 경우로 도전하면 그만아닌가??**
# 라는 생각이 들었다.
#
# tryX가 x일 때를 계속 체크해봤다가, 모든 경우의 수 이상을 지나치면 -1을 반환하면 될 것이다!
#
# 콘솔에 예제 입력이 진행되는 과정을 출력해놓고, 규칙을 찾아보았다.
# 일단 x가 M마다 같은 수가 되는 것은 알았고,
# y의 식은 `((y+M)%N)+1` 정도가 아닐까 했고,
# 모든 경우의 수를 어떻게 세나... 고민을 하다가 일단 count가 M*N을 넘지 않는 것 같아서
# 임시로 `M*N < count`로 종료 조건을 해놓았다.
#
# 해본 결과 y의 식이 잘못되어 다시 계산해보니 -1을 뺀 `(tryY + M) % N`가
# 맞는 답이었다. 이제 도전 수를 엄청 줄였으니 백준에 올렸더니, 틀렸다고 나왔다!!!
# 왜지??? 보니까 역시 종료 조건이 문제였다.
# 여기서 구글에 검색해보니, M과 N의 최소공배수를 넘으면 종료인 거였다.
# 출처: http://mygumi.tistory.com/325
# 그래서 최소공배수를 최소공약수(gcd)를 이용해 구하는 법을 구해서 만들었다.
#
# 다시 도전했는데 또 틀렸다... 알고보니 처음 수를 잘못 설정했다.
# 처음 수를 다시 설정했는데.. 잘 가다가 또 틀렸다.
# count가 잘못되었던 거였다. 그런데 또 틀렸다!!!
# y를 변경하는 것도 나머지를 고려하지 않아서 틀렸다.
# 이렇게 자잘한 실수로 8전 9기 끝에 맞았습니다!!!를 봤다...ㅠㅠ
#
# 자잘한 실수때문에 문제를 풀 수 있다는 생각이 엄청 흐트러질 수 있겠구나..를 느꼈다.
#

from timing import timing

test = [
    [10, 12, 3, 9],
    [10, 12, 7, 2],
    [13, 11, 5, 6],
    # [100, 50, 23, 30]
    # [40000, 40000, 40000, 40000]
]

from math import gcd


def problem(M, N, x, y):
    # 최소공배수(마지막)
    last = M * N / gcd(M, N)

    # 처음 수 만들어줌
    tryY = N if x % N == 0 else x % N
    count = x % (M + 1)

    # 반복
    while True:
        # 끝까지 했을 경우 -1 출력후 종료
        if last < count:
            print(-1)
            break

        # 찾으려는 수와 동일하면 횟수 리턴
        # 아니면 카운트 증가
        if tryY == y:
            print(count)
            break

        # y 변경
        tryY = N if (tryY + M) % N == 0 else (tryY + M) % N
        # 카운트 증가
        count += M


for _ in range(int(input())):
    M, N, x, y = list(map(int, input().split()))
    problem(M, N, x, y)

# for i in range(3):
#     M, N, x, y = test[i]
#     print(M, N, x, y)
#     problem(M, N, x, y)