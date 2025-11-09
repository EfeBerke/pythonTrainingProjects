"""
Task
Write a recursive function that calculates the sum of all numbers in a nested list structure,
but it should only sum the numbers that are greater than a given threshold.
E.G. 
Input: [3, [7, [1, 9], 4], 10, [2, [5, 11]]], threshold = 5
Output: 7 + 9 + 10 + 11 = 37
"""

def recursion_sum(lst_of_lsts, sum = [0]):
    for data in lst_of_lsts:
        if type(data) == list:
            recursion_sum(data, sum)
        elif data > 5:
            sum[0] += data
    return sum[0]


 # Test Lists
test_list1 = [3, [7, [1, 9], 4], 10, [2, [5, 11]]] # 37
test_list2 = [1, [4, [6, 8]], 3, [10, [2, [15]]]] # 39
test_list3 = [[5, [5, [5]]], [4, [6, [7, [8]]]]] # 21
test_list4 = [[], [1, [2, [3]]], [[[[10]]]], 9] # 19

print(recursion_sum(test_list1, [0]))
print(recursion_sum(test_list2, [0]))
print(recursion_sum(test_list3, [0]))
print(recursion_sum(test_list4, [0]))