def wordBreak(s, wordDict):
    """
    Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated
    sequence of one or more dictionary words. Note that the same word in the dictionary may be reused multiple
    times in the segmentation.
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
