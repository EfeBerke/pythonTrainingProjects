

# Q1
def square_func(x):
    return x * x


# Q2
def is_even(x):
    if x % 2 == 0:
        return f"{x} is even."
    else:
        return f"{x} is odd."


# Q3
def sum_of_list(num_list):
    total = 0
    for number in num_list:
        total += number
    return total


# Q4
def reverse_string(string):
    return string[::-1]


# Q5
def return_the_largest(num_list):
    num_list.sort()
    return num_list[-1]


# Q6
def is_palindrome(word):
    if reverse_string(word) == word:
        return f"{word} is a palindrome."
    else:
        return f"{word} is not a palindrome."


# Q7
def concatenate_strings(first_string, second_string):
    return first_string + second_string


# Q8
def raise_number_to_power(number, power):
    return number ** power


# Q9
def absolute_value_of_number(x):
    if x < 0:
        return -x
    else:
        return x


# Q10
def length_of_str(string):
    char_counter = 0
    for _ in string:
        char_counter += 1
    return char_counter


# Testing functions
print(square_func(4))
print(is_even(8))
print(sum_of_list([5, -43, 1, -7, 134, 0]))
print(reverse_string("efeberke"))
print(return_the_largest([5, -43, 1, -7, 134, 0]))
print(is_palindrome("afarafa"))
print(concatenate_strings("efe", "berke"))
print(raise_number_to_power(7, 3))
print(absolute_value_of_number(-23))
print(length_of_str("vatansever"))

