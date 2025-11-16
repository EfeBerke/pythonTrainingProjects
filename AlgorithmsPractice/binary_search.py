def my_binary_search(ls, x):
    ind = len(ls) //2
    if ls[ind] < x and ls[ind] != ls[-1]:
        return my_binary_search(ls[(ind+1):], x)
    elif ls[ind] > x and ls[ind] != ls[0]:
        return my_binary_search(ls[:ind], x)
    else:
        if ls[ind] == x:
            return f"{x} is found in list"
        else:
            return f"there is no such {x} in list"
        


# Test cases
ls = [2, 2, 3, 3]
x = 1   
y = 2
z = 4

print(my_binary_search(ls, x))
print(my_binary_search(ls, y))
print(my_binary_search(ls, z))

