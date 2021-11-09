def LongestSubstringNoRepeatingVer1(arr):
    """
    3. Longest Substring Without Repeating Characters
    Given a string s, find the length of the longest substring without repeating characters.
    """
    length = len(arr)
    LSNP_at_i = []
    current_LSNP = set()
    for i in range(length):
        current_LSNP = set()
        for j in range(i, length):
            if arr[j] not in current_LSNP:
                current_LSNP.add(arr[j])
                if j == length - 1:
                    LSNP_at_i.append(j-i+1)
            else:
                LSNP_at_i.append(j-i)
                break
    return max(LSNP_at_i)

def LongestSubstringNoRepeatingVer2(arr):
    """
    Problem: Given a string s, find the length of the longest substring without repeating characters.
    
    Idea: scan the string for index i = 0 to len() - 1 and calculate the length of the longest substring to the current index i.
    Use a window with start_index_current_substr_wo_repetition and then extend it to i.
    
    This solution uses extra space to store the last indexes of already visited characters. The idea is to scan the string from left to right, keep track of the maximum length Non-Repeating Character Substring seen so far in res. When we traverse the string, to know the length of current window we need two indexes.
    1) Ending index (j): We consider current index as ending index. 
    2) Starting index (i): It is same as previous window if current character was not present in the previous window. To check if the current character was present in the previous window or not, we store last index of every character in an array lasIndex[]. If lastIndex[str[j]] + 1 is more than previous start, then we updated the start index i. Else we keep same i.
    """
    length = len(arr)
    substring_without_repetition_length = []
    
    # start_index of a current substring without repetition
    start_index_current_substr_wo_repetition = 0
    
    # dictionary of last index of all characters. This dictionary will be increased gradually by i
    last_index = {}
    
    for i in range(length):
            
        if arr[i] in last_index:
            
            start_index_current_substr_wo_repetition = max(last_index[arr[i]] + 1, start_index_current_substr_wo_repetition) 
            
        substring_without_repetition_length.append(i - start_index_current_substr_wo_repetition + 1)
        
        last_index[arr[i]] = i
        
    return max(substring_without_repetition_length)
                          
list = ['abcabcbb', 'pwwkew', 'abcdefgh', 'ab', 'abcda', 'enjoyalgorithms']
for s in list:
    print(LongestSubstringNoRepeatingVer1(s), LongestSubstringNoRepeatingVer2(s))