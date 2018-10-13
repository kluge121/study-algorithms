S = list(input())
output = [-1]*26

for charIndex, char in enumerate(S):
    index = ord(char) - 97
    if output[index] == -1:
        output[index] = charIndex

print(' '.join(list(map(str, output))))