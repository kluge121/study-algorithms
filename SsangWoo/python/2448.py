# http://lazineer.tistory.com/179
# ㅠㅠ

from math import log, pow

stars = ["  *   ", " * *  ", "***** "]


def makeStar(shift):
    for i in range(len(stars)):
        stars.append(stars[i] + stars[i])
        stars[i] = ("   "*shift + stars[i] + "   "*shift)


def go(n):
    k = int(log(int(n/3), 2))
    for i in range(k):
        makeStar(int(pow(2, i)))

    for line in stars:
        print(line)


go(int(input()))
