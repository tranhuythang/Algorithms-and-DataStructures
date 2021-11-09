
def LongestPalindromSubstring(arr):
    """
    5 Longest Palindromic Substring
    Find the longest palindrome substrings of a given string arr

    :param arr:
    :return:
    """
    # The following is wrong
    # L = len(arr)
    # p = [-1 for i in range(L)]
    # p[0] = 1
    # maxLength = [1, 0]
    # if arr[1] == arr[0]:
    #     p[1] = 2
    #     maxLength[0] = 1
    #     maxLength[1] = 1
    # else:
    #     p[1] = 1
    #     maxLength[0] = 1
    #     maxLength[1] = 1
    # for n in range(1, L-1):
    #     if arr[n+1] == arr[n - p[n]]:
    #         p[n+1] = p[n] + 2
    #     else:
    #         if arr[n+1] == arr[n]:
    #             p[n+1] = 2
    #         else:
    #             p[n+1] = 1
    #     if maxLength[0] < p[n+1]:
    #         maxLength[0] = p[n+1]
    #         maxLength[1] = n+1
    # print('*********')
    # print("p = ", p)
    # for i in range(L):
    #     print(arr[i - p[i] +1 : i+1 : 1])
    # return (maxLength[0], arr[maxLength[1]-maxLength[0]+1:maxLength[1]+1:1])

    def findRadius(left, right):
        radius = 0
        while left >= 0 and right <= L - 1:
            if arr[left] == arr[right]:
                radius += 1
                left -= 1
                right += 1
            else:
                break
        return radius

    L = len(arr)
    longestPalindrom = [0, [0, 0]]
    palindromSubstr = []
    for i in range(L):
        oddRadius = findRadius(i-1, i+1)
        evenRadius = findRadius(i, i+1)
        if 2*oddRadius + 1 > longestPalindrom[0]:
            longestPalindrom[0] = 2*oddRadius + 1
            longestPalindrom[1] = [i - oddRadius, i + oddRadius]
        if 2*evenRadius > longestPalindrom[0]:
            longestPalindrom[0] = 2*evenRadius
            longestPalindrom[1] = [i+1 - evenRadius, i + evenRadius]
        #
        # if evenRadius == 0:
        #     if oddRadius != 0:
        #         palindromSubstr.append([i, i])
        # else:
        #     palindromSubstr.append([i + 1 - evenRadius, i + evenRadius])
        # palindromSubstr.append([i - oddRadius, i + oddRadius])
    return longestPalindrom[1]


test = ["babad", "cbbd", "ac", "abcdefedcba", "abcdefedcaba", "babcbabcbaccba", "yabadabadoo", "aabactgaaccaat", "abab", "abbab", "aaabaaab", ]
for s in test:
    print(s, "->",LongestPalindromSubstring(s))