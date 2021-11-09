def max_heapify(arr, root_index):
    n = len(arr)
    left_child_index = root_index*2 + 1
    right_child_index = root_index*2 + 2
    largest_index = root_index

    if left_child_index < n and arr[left_child_index] > arr[largest_index]:
        largest_index = left_child_index

    if right_child_index < n and arr[right_child_index] > arr[largest_index]:
        largest_index = right_child_index

    if largest_index != root_index:
        arr[largest_index], arr[root_index] = arr[root_index], arr[largest_index]
        max_heapify(arr, largest_index)

def build_max_heap(arr):
    n = len(arr)
    last_non_leaf_node_index = n // 2 -1
    for i in range(last_non_leaf_node_index, -1, -1):
        max_heapify(arr, i)

arr = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]
n = 11
build_max_heap(arr)
print(arr)
