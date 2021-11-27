"""
* Problem: Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a
    space-separated sequence of one or more dictionary words. Note that the same word in the dictionary may be
    reused multiple times in the segmentation.
* Algorithm: Recursion. Let word_detect(start) to be True/False if the input string from start index can be broken by the
dictionary then word_detect(start) = word_detect(start+k) if the input substring from start to start+k is in the dictionary
* Time-Complexity: In the following implementation
- The for loop takes O(n)
- The substring s[start_index:end_index+1:] takes O(n)
- How long does the recursive call word_detect(end_index+1) takes? In the worst case word_detect(0) calls word_detect(1),
 which calls word_detect(2), ..., which call word_detect(n) so n calls, and word_detect(n) is O(1), so totally O(n).
=> totally it takes O(n^3)
* Space-Complexity: Using memoization so the recursive stack needs at most n, and hence O(n)
"""
def wordBreak(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """
    wordDict_set = set([])
    for word in wordDict:
        wordDict_set.add(word)
    n = len(s)
    word_detect_memo = {}

    def word_detect(start_index):
        if start_index >= n:
            return True
        if start_index in word_detect_memo:
            return word_detect_memo[start_index]
        for end_index in range(start_index, n):
            if s[start_index:end_index+1:] in wordDict_set:
                if word_detect(end_index+1):
                    return True
        word_detect_memo[start_index] = False
        return False
    return word_detect(0)

test = [["aaaaaaa", ["aaaa","aaa"]], ["aaaaaaa", ["aaaa","aa"]], ['feetnode', ['feet', 'node']], ['applepenapple', ['apple', 'pen']], ['catsandog', ['cats', 'dog', 'sand', 'and', 'cat']]]
# test = [["aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]]]
for t in test:
    print(t, '->', wordBreak(t[0], t[1]))
