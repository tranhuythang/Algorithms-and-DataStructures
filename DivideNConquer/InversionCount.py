"""
*Problem: Given an array, find the total number of inversions of it. If (i < j) and (A[i] > A[j]), then pair (i, j) is called an
inversion of an array A. Inversion count shows how close an array is to its sorted array.
*Algorithm: Divide and Conquer - Use MergeSort
Split the input into 2 halves a, b
Count the inversion of each half a, b
Call recursively the algorithm on those 2 halves a, b
Merge and sort those 2 halves a, b as in merge sort
Count the inversion of the form a[i], b[j] where a[i] > b[j].
Note that the indices of a are always less than b.

inversion_count(input):
    mid = len(input) // 2
    left_half_inv_count, sorted_left_half = inversion_count(input[:mid:])
    right_half_inv_count, sort_right_half = inversion_count(input[mid::])
    left_right_inv_count, sorted_result = merge(sorted_left_half, sort_right_half)
    return (left_right_inv_count + left_half_inv_count + right_half_inv_count), sorted_result
merge(u, v):
    # see the code below
*Time-complexity: Similar to Merge Sort, so O(nlogn)
*Space-complexity: Similar to Merge Sort, so O(n)
"""

def InversionCount(nums):
    def merge_count_inv(a, b):
        alength = len(a)
        blength = len(b)
        i = 0
        j = 0
        inv_count = 0
        sorted_result = []
        while i < alength and j < blength:
            if a[i] > b[j]:
                sorted_result.append(b[j])
                j += 1
                inv_count += (alength - i)
            else:
                sorted_result.append(a[i])
                i += 1
        while i < alength:
            sorted_result.append(a[i])
            i += 1
        while j < blength:
            sorted_result.append(b[j])
            j += 1
        return inv_count, sorted_result

    def split_sort_merge_count_inv(a):
        n = len(a)
        if n == 1:
            return (0, a)
        if n == 2:
            if a[0] > a[1]:
                return (1, [a[1], a[0]])
            else:
                return (0, a)
        mid = n // 2
        left_inv_count, left_half = split_sort_merge_count_inv(a[:mid:])
        right_inv_count, right_half = split_sort_merge_count_inv(a[mid::])
        left_right_inv_count, result = merge_count_inv(left_half, right_half)
        return (left_right_inv_count + left_inv_count + right_inv_count, result[::])

    return split_sort_merge_count_inv(nums)[0]

a = [7, 3, 5, 2, 0, 1, 4, 9]
# a = [1,0,2]
# a = [1,2,0]
print(InversionCount(a))



