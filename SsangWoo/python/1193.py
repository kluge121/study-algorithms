# 지그재그로 가는 것에 이해를 하는 데 시간이 약간 걸렸다.
# 가다가 벽에 부딪히면 x+1, y+1을 해주면 되는거다.
# 문제에 적힌 번호가 x/y 기준으로 거꾸로(y/x) 적혀있다는 것에 유의(헷갈릴 수 있음)
#
# 0,0 -> 1,0 -> 0,1 -> 0,2 -> 1,1 -> 2,0 -> 3,0 -> ...
# 어떤 경우에 아래로 가고 어떤 경우에 위로 가는지를 따져보자
#
# 오른쪽으로 가는 경우: x == 0 -> y+1
# 왼쪽 아래로 가는 경우: 오른쪽으로 가는 경우 다음부터 y == 0일 때까지 -> x-1 y+1
# 아래로 가는 경우: 왼쪽 아래로 가는 경우 다음 이후로 -> y+1
# 오른쪽 위로 가는 경우: 아래로 가는 경우 다음 이후로 x == 0일 때까지 -> x+1 y-1
# 오른쪽으로 가는 경우: 오른쪽 위로 가는 경우 다음 이후로 -> x+1
#
# 다했다. 코딩해보자

(x, y) = (0, 0)
# state = ['right', 'leftDown', 'down', 'rightUp']

X = int(input())-1
arrState = 'right'
for i in range(X):
    if arrState == 'right':
        x += 1
        arrState = 'leftDown'
    elif arrState == 'leftDown':
        x, y = x - 1, y + 1
        if x == 0:
            arrState = 'down'
    elif arrState == 'down':
        y += 1
        arrState = 'rightUp'
    elif arrState == 'rightUp':
        x, y = x + 1, y - 1
        if y == 0:
            arrState = 'right'
    else:
        print('오류!')
        break

print("{}/{}".format(y + 1, x + 1))
