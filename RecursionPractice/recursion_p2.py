"""
Question: Nested Dictionary Value Sum (with Conditions)
You are given a nested dictionary that can contain:
integers
lists
dictionaries
or any combination of them
Write a recursive function:
that returns the sum of all integers that are:
Odd numbers,
Greater than 10,
And are NOT inside a list that contains the number 0.
"""

def conditional_sum(structure, sum = 0):
    
    if isinstance(structure, dict):
        for value in structure.values():
            sum += conditional_sum(value)

    elif isinstance(structure, list):
        if not 0 in structure:
            for value in structure:
                sum += conditional_sum(value)

    else: # If it is integer
        if structure % 2 == 1 and structure > 10:
            sum += structure

    return sum


data = {
    "a": 5,
    "b": [15, 2, {"x": 23, "y": [0, 99]}],
    "c": {"d": [11, 7, 14], "e": {"f": 21}}
} # Expected output: 15 + 23 + 21 = 59

data2 = [0, [11, 13, 15]] # Expected output: 0

data3 = [0, {"a": {"b": [11, 13, 15]}}] # Expected output: 0

print(conditional_sum(data))
print(conditional_sum(data2))
print(conditional_sum(data3)) 