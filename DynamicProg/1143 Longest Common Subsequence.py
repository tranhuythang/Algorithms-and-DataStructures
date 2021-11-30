"""
* Problem: Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common
subsequence, return 0. Note: "ace" is a subsequence of "abcde".
* Dynamic Programming algorithm: Let LCS(i, j) be the longest common substring of text1 with first i characters, text2
with first j characters
LCS[i][j] = LCS[i-1][j-1] + 1 if text1[i] = text2[j]
          = max(LCS[i][j-1], LCS[i-1][j]) if text1[i] != text2[j]
* Time-Complexity: O(n1xn2)
* Space-Complexity: O(n1xn2)
"""
def LongestCommonSubsequence(text1, text2):
    n1 = len(text1)
    n2 = len(text2)

    LCS = [[0 for j in range(n2+1)] for i in range(n1+1)]
    for i in range(n1+1):
        LCS[i][0] = 0
    for j in range(n2+1):
        LCS[0][j] = 0

    for i in range(1, n1+1):
        for j in range(1, n2+1):
            if text1[i-1] == text2[j-1]:
                LCS[i][j] = LCS[i-1][j-1] + 1
            else:
                LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])

    lcs_string = ''
    i = n1
    j = n2
    while i != 0 and j != 0:
        print('i = ', i, 'j = ', j)
        if text1[i-1] == text2[j-1]:
            lcs_string += text1[i-1]
            i -= 1
            j -= 1
        else:
            if LCS[i-1][j] > LCS[i][j-1]:
                i = i-1
            else:
                j = j-1
    print(lcs_string[::-1])
    return LCS[n1][n2]

test = [['cde', 'abcde'], ['ycjdjej', 'xabfcgdse'], ['aaabbccddee', 'abxyzbe']]
for t in test:
    print(t, '->', LongestCommonSubsequence(t[0], t[1]))