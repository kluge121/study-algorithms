def isHansu(digits):
    return digits[1] - digits[0] == digits[2] - digits[1]

hansuCount = 0

for i in range(1, int(input()) + 1):
    if i < 100:
        hansuCount += 1
        continue
    elif i == 1000:
        break

    digits = list(map(int, list(str(i))))
    if isHansu(digits):
        hansuCount += 1

print(hansuCount)
