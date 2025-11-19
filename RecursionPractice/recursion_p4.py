# Write a recursive function to compute the sum of a list.

def sum_of_list(lst):
    if len(lst) == 0:
        return 0
    
    return lst[0] + sum_of_list(lst[1:])


lst1 = [5, 8, 12, 75, 100]
lst2 = []

#print(sum_of_list(lst1))
#print(sum_of_list(lst2))


# Write recursion to count how many times the number 5 appears in a nested list.

def finding_5(nlst):
    count = 0
    for elm in nlst:
        if elm == 5:
            count += 1
        elif isinstance(elm, list):
            count += finding_5(elm)
    
    return count


nested_list = [3, [7, [1, 9], 5], 5, [2, [5, 11]]]

print(finding_5(nested_list))