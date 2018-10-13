croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
string = list(input())
output = 0
while len(string) > 0:
    char = ''.join(string[:2])
    if char in croatia:
        output += 1
        string = string[2:]
    else:
        char = ''.join(string[:3])
        if char == 'dz=':
            output += 1
            string = string[3:]
        else:
            output += 1
            string = string[1:]

print(output)