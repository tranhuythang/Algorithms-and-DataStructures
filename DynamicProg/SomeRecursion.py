from collections import deque 
def gcd(a, b):
    if b == 0:
        return abs(a)
    if a == 0:
        return abs(b)
    m = min(abs(a), abs(b))
    M = max(abs(a), abs(b))
    return gcd(m, M%m)

print("gcd", gcd(24, 27))

def int2binary(number):
    result = []
    def divideby2(num):
        nonlocal result
        if num < 2:
            result.append(num)
            return
        else:
            result.append(num % 2)
            divideby2(num//2)
    divideby2(number)
    return ''.join(map(str, result[::-1]))


def int2binaryVer2(num):
    if num < 2:
        return num
    else:
        return str(int2binaryVer2(num//2)) + str(num % 2)

print(int2binary(13))
print(int2binaryVer2(13))

def removeAdjacentDuplicate(str, index = 0):
    # print(str, index)
    if index == len(str) - 1:
        return str
    for i in range(index, len(str)-1):
        if str[i] == str[i+1]:
            return removeAdjacentDuplicate(str[:i+1:] + str[i+2::], i)
    return str

print(removeAdjacentDuplicate("aabcdeeeeeefghhxyz"))




