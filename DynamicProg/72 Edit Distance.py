"""
* Problem: Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
You have the following three operations permitted on a word: (1) Insert a character, (2) Delete a character, (3) Replace
a character by any character.
* Dynamic Programming Algorithm: Let E(i, j) be the minimum number of operations for first i characters of word1, first j
characters of word2. We try to transform the last character word1[i] to the last character word2[j], there are 3 cases:
- Delete word1[i], so E(i, j) = E(i-1, j) + 1
- Replace word1[i] by word2[j] if word1[i] != word2[j] or do nothing if word1[i] != word2[j], so
E(i, j) = E(i-1, j-1) + diff where diff = 1 if word1[i] != word2[j], 0 if word1[i] == word2[j]
- Insert word2[j] after word1[i], so E(i, j) = E(i-1, j-1) + 1
Since we don't know which operation is the best,
E(i, j) = min(E(i-1, j) + 1, E(i, j-1) + 1, E(i-1, j-1) + diff)
The base case E(0, i) = i when word1 is empty and E(i, 0) = i when word2 is empty.
* Time-complexity: O(n^2)
* Space-complexity: O(n^2)
"""
def edit_distance(word1, word2):
    n1 = len(word1)
    n2 = len(word2)

    E = [[None for j in range(n2 + 1)] for i in range(n1 + 1)]

    for i in range(0, n1 + 1):
        E[i][0] = i
    for j in range(0, n2 + 1):
        E[0][j] = j

    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            diff = 0 if word1[i - 1] == word2[j - 1] else 1
            E[i][j] = min(E[i - 1][j - 1] + diff, 1 + E[i - 1][j], 1 + E[i][j - 1])

    return E[n1][n2]
