
def LongestPalindromSubstring(arr):
    """
    5 Longest Palindromic Substring
    Find the longest palindrome substrings of a given string arr

    :param arr:
    :return:
    """

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