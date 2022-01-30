"""
* Problem: 315. Count of Smaller Numbers After Self
You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].
Example 1: Input: nums = [5,2,6,1] -> Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
* Algorithm: Divide and Conquer (use Merge Sort template)
Use the divide and conquer template of merge sort, divide the problem into 2 subproblems: left and right. We can assume
we have solution for left, right (i.e. for each elemnt in left, right, we know the number of smaller elemnts on the right)
and we can also assume both left and right are sorted ascendingly.
Now the "merge" part: we need to calculate for each element, the number of smaller elements by using the number of smaller
elements for each element in left and right.
    // left, right are arrays of elements of the form [value, index, smallerNumberCount]
    right_counter = 0
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i][0] <= right[j][0]:
            result.append(left[i])
            result[-1][2] += right_counter
            i += 1
        else:
            result.append(right[j])
            right_counter += 1
            j += 1
* Time-Complexity: O(nlogn) similar to Merge Sort
* Space-Complexity: recursive call use local variables, and those local variables will be released after the call is done.
 The only variable that stays in the memory is the array storing the result, so O(n).
"""

def NumberOfGreaterAfterSelf(nums):
    def merge(left, right):
        result = []
        left_len = len(left)
        right_len = len(right)
        left_counter = right_counter = 0
        i = j = 0
        while i < left_len and j < right_len:
            if left[i][0] <= right[j][0]:
                result.append(left[i])
                result[-1][2] += right_counter
                i += 1
            else:
                result.append(right[j])
                right_counter += 1
                j += 1
        while i < left_len:
            result.append(left[i])
            result[-1][2] += right_counter
            i += 1
        while j < right_len:
            result.append(right[j])
            result[-1][2] += left_counter
            j += 1
        return result

    def greater_self(input):
        n = len(input)
        if n <= 1:
            return input[::]
        mid = len(input) // 2
        left = greater_self(input[:mid:])
        right = greater_self(input[mid::])
        return merge(left, right)
    # print(f'original input = {nums}')
    n = len(nums)
    input = [[nums[i], i, 0] for i in range(n)]
    immediate_result = greater_self(input)
    final_result = [None for i in range(n)]
    print(immediate_result)
    for s in immediate_result:
        final_result[s[1]] = s[2]
    return final_result


a = [5,2,6,1]
a = [5, 2]
# a = [-1,-1, -1, -1]
print(NumberOfGreaterAfterSelf(a))