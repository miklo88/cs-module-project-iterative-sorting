# arr = [2,5,8,12,18,16,3,7,20,10]
# # TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
# This is the loop that says we will go through each item in our collection, one at a time.
    # outer loop
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        #inner loop
#we need to loop through all the items that come after the current index to find the one with the lowest value. We do this with another for loop. With each item, we check if it is smaller than the current smallest and replace the smallest index if so.
        for j in range(cur_index + 1, len(arr)):
# At the end, before we increment our outer loop, we swap the item that is located in the current index with the smallest item that we located during our loop.
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        # Your code here
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]

    return arr
# #runtime complexity of O(n^2)
# sortedArr = selection_sort(arr)
# print(sortedArr)
# # print(arr)

# TO-DO:  implement the Bubble Sort function below
# arr = [80,95,84,92,91,87,88,99,81,96]

def bubble_sort(arr):
    # Your code here #declaring the arr len as n and to pass as the sort len
    n = len(arr)
#traversing through the elements
    for i in range(n):
        #last i elements are in place already.
        for j in range(0, n - i - 1):
#traverse the array from 0 to n-i-1
#swap if the element bound is greater than the next element.
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr
# new_bubble = bubble_sort(arr)
# print(new_bubble)
'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
## O(n+k) worst case O(k)

'''
# def counting_sort(arr, maximum=None):
#     # Your code here


#     return arr
# stretch = counting_sort(arr)
# print(stretch)