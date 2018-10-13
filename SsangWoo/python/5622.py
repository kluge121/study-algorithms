num = {
    'ABC': 3,
    'DEF': 4,
    'GHI': 5,
    'JKL': 6,
    'MNO': 7,
    'PQRS': 8,
    'TUV': 9,
    'WXYZ': 10
}
output = 0
string = list(input())
for char in string:
    for key in num.keys():
        if char in key:
            output += num[key]
            break

print(output)

# char = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# list(map(lambda x: ord(x),list(input())))