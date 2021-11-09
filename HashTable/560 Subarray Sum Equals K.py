def ContinuousSubarraySumK(arr, k):
    """
    560 Subarray Sum Equals K
    Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals
    to k.
    :param arr:
    :param k:
    :return:
    """
    print("--- Arr =", arr, "K =", k)
    
    length = len(arr)
    
    count = 0
    sum_i_dict = {}

    sum = 0
    for i in range(length):
        sum += arr[i]
        if sum not in sum_i_dict:
            sum_i_dict[sum] = [i]
        else:
            sum_i_dict[sum].append(i)
    print("sum_i_dict = ", sum_i_dict)
    complement = 0
    for sum in sum_i_dict.keys():
        if sum == k:
            print("from 0 to", sum_i_dict[sum])
            count += len(sum_i_dict[sum])
        complement = sum - k
        if complement in sum_i_dict:
            print("from", sum_i_dict[sum], "to", sum_i_dict[complement])
            count += len(sum_i_dict[complement])*len(sum_i_dict[sum])
    return count

test = [([1, 1, 2], 2), ([1, 2, 3, -1, 1, 1, 1], 3), ([1, 0, 2, 3, 5], 5)] 
for s in test:
    print(ContinuousSubarraySumK(s[0], s[1]))