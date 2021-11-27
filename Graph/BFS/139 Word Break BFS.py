"""
* Problem: Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a
    space-separated sequence of one or more dictionary words. Note that the same word in the dictionary may be
    reused multiple times in the segmentation.
* Algorithm: BFS
* Time-Complexity: (n is the string's length)
- All the nodes (numbers) to explore is put in the queue startpos_to_explore. The numbers increase so there are at most
n numbers, and hence O(n)
- The end increases from current_start to n+1 so O(n)
- The substring s from current_start index to end index so O(n)
=> O(n^3)
* Space-Complexity: the BFS queue and the visited contains numbers at most from 1 to n so O(n)
"""
from collections import deque
def wordBreak(s, wordDict):
    n = len(s)
    startpos_to_explore = deque()
    startpos_to_explore.append(0)
    visited = set()
    word_set = set(wordDict)
    while startpos_to_explore:
        current_start = startpos_to_explore.popleft()
        if current_start not in visited:
            for end in range(current_start + 1, n + 1):
                if s[current_start:end] in word_set:
                    if end == n:
                        return True
                    else:
                        startpos_to_explore.append(end)
        visited.add(current_start)
    return False

test = [["aaaaaaa", ["aaaa","aaa"]], ["aaaaaaa", ["aaaa","aa"]], ['feetnode', ['feet', 'node']], ['applepenapple', ['apple', 'pen']], ['catsandog', ['cats', 'dog', 'sand', 'and', 'cat']]]
test = [["aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]]]
for t in test:
    print(t, '->', wordBreak(t[0], t[1]))