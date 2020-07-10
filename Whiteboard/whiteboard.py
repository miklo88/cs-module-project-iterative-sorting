'''
bi-weekly whiteboard session with a duration of 10 minutes.
start at 20:48 EST
'''
'''
Challenge
Add up and print the sum of the all of the minimum elements of each inner array:
[[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]
The expected output is given by:
4 + -1 + 9 + -56 + 201 + 18 = 175
You may use whatever programming language you'd like.
Verbalize your thought process as much as possible before writing any code. Run through 
the UPER problem solving framework while going through your thought process.
'''

'''
UPER
so for each inner array i have to map or loop over them individually.
as i pass each one i must add up their sum and add it to another list/array 
then add all of these sums up and get the total 175

grabbed all the mins of each nested array. 
looking like i have a nested for loop

'''

arr = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]
##SOLUTION 1
# a = []
# c = []
# for i in arr:
#     a.append(min(i)) 
#     # a = min(i) 
#     # c.append(sum(a))
# print(sum(a))
# print(c)

## UPDATED CODE. FINDING MORE WAYS TO REACH SOLUTION.
##SOLUTION 2
# def min_sum(arr):
#     a = 0
#     for i in arr:
#         a += min(i)
#     print(a)
# minimum = min_sum(arr)

# # SOLUTION 3 WITH LIST COMPREHENSION
# def min_sum(arr):
#     a = sum([min(i) for i in arr])
#     return(a)
# print(min_sum(arr))

#SOLUTION 4 HAVING FUN WITH RECURSION
def min_sum(arr):
    if len(arr) == 1:
        return min(arr[0])   
    else:
        return min(arr[0]) + min_sum(arr[1:])
        
print(min_sum(arr)) #returns 175
#prints to see what is going on step by step in function
print(min_sum(arr[1:])) #returns 171
print(min(arr[0])) #returns 4
print(arr[0]) #returns [8,4]

def max_sum(arr):
    if len(arr) == 1:
        return max(arr[0])
    else:
        return max(arr[0]) + max_sum(arr[1:])
print(max_sum(arr)) #returns 436
print(arr[0]) #returns [8,4]
print(max(arr[0])) #returns 8
print(max_sum(arr[1:])) #returns 428 then which is added to max(arr[0]) to equal 436