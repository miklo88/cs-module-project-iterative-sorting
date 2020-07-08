# arr = [1,2,5,6,8,9,7,15,78,3,56,55]
# target = 2

def linear_search(arr, target):
    # Your code here
    n = len(arr)
    for i in range(0, n):
        if arr[i] == target:
            return i

    return -1   # not found

# print(linear_search(arr, target))

# # Write an iterative implementation of Binary Search
# def binary_search(arr, target):
#     # Your code here
#     start = arr[0]
#     end = (len(arr) - 1)

#     found = False
#     while end >= start and not found:
#         #getting the middle point
#         middle_index = (start + end) // 2
#         #compare the value in the middle with target
#         #if the middle value is the same as target, set found to True
#         if arr[middle_index] == target:
#             found = True
#             #move start or end index closer to one another, and shrink our area of search. aka bracketing
#         else:
#             if target < arr[middle_index]:
#                 end = middle_index - 1
#             if target > arr[middle_index]:
#                 start = middle_index + 1
#     # return found
#     return -1  # not found

# random_nums.sort()
# print(binary_search(random_nums, num_to_find))
