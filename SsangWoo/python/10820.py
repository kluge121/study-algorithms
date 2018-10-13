def isInteger(char):
    try:
        int(char)
        return True
    except ValueError:
        return False


result = []


while True:
    try:
        low, up, num, space = 0, 0, 0, 0

        # 입력
        string = input()

        for char in string:
            if char.islower():
                low += 1
            elif char.isupper():
                up += 1
            elif isInteger(char):
                num += 1
            elif char == ' ':
                space += 1

        result.append([low, up, num, space])

    except EOFError:
        break

# 출력
for counts in result:
    for i in counts:
        print(i, end=" ")
    print()
