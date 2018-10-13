output = ''
for _ in range(int(input())):
    R, S = input().split()
    string = list(S)
    for char in string:
        output += char*int(R)
    print(output)
    output=''

