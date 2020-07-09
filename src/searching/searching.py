# arr = [1,2,5,6,8,9,7,15,78,3,56,55]
# target = 2

def linear_search(arr, target):
    # Your code here
    n = len(arr)
    for i in range(0, n):
        if arr[i] == target:
            return i

    return -1   # not found

# linear = linear_search(arr, target)
# print(linear)

# # Write an iterative implementation of Binary Search
# arr = [-5,-3,-2,-1,6,8,9,7,15,56,55,78]
# arr = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
# target = 8
def binary_search(arr, target):
    # Your code here
    start = 0
    # print(start)
    end = (len(arr) -1)
    # print(end)
    while end >= start:
        #getting the middle point
        middle_index = (start + end) // 2
        # print(middle_index)
        #compare the value in the middle with target
        #if the middle value is the same as target return target. 
        if arr[middle_index] == target:
            return middle_index
            #move start or end index closer to one another, and shrink our area of search. aka bracketing
        else:
            if target < arr[middle_index]:
                end = middle_index - 1
            if target > arr[middle_index]:
                start = middle_index + 1
    
    return -1  # not found

# binary = binary_search(arr, target)
# print(binary)


