"""
*Problem: Given a binary array data, return the minimum number of swaps required to group all 1’s present in the array
together in any place in the array. You can swap any two element in the array.
*Algorithm: Sliding window
Let count_1 be the number of 1's. The goal is that from a window of size count_1, swap all 0 inside the window with 1
outside the window; we try to find the window with minimum number of 0.
First calculate the number of 0s in the first window, the next window is different from the previous window in only the
first and the last element, so it's easy to calculate the number of 0's in the next windows based on the previous window.
*Time-complexity: need 2 passes so O(n)
*Space-complexity: don't need to store the number of 0's in all windows, just the current window, so O(1)
"""
def MinSwapGroup1Together(data):
    n = len(data)
    count_1 = 0
    for s in data:
        if s == 1:
            count_1 += 1
    if count_1 <= 1:
        return 0

    current_window_move_count = 0
    for i in range(count_1):
        if data[i] == 0:
            current_window_move_count += 1
    min_move_count = current_window_move_count
    for i in range(1, n+1 - count_1):
        if data[i-1] == 0:
            current_window_move_count -= 1
        if data[i+count_1-1] == 0:
            current_window_move_count += 1
        if min_move_count > current_window_move_count:
            min_move_count = current_window_move_count
    return min_move_count






