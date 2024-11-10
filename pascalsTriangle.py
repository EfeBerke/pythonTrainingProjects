

def pascal_line_creator(pascal_line):
    next_pascal_line = []
    for index1, num1 in enumerate(pascal_line):
        for index2, num2 in enumerate(pascal_line):
            if num1 == 0 and num2 == 0 and index1 == index2:
                next_pascal_line.append(0)
            elif index1 == index2 - 1:
                next_pascal_line.append(num1 + num2)
    return next_pascal_line


def pascal_triangle_list_creator(n):
    initial_list = [0, 1, 0]
    pascal_triangle_list = [[0, 1, 0]]
    i = 0
    while i < n:
        pascal_triangle_list.append(pascal_line_creator(initial_list))
        initial_list = pascal_line_creator(initial_list)
        i += 1
    return pascal_triangle_list


def pascal_triangle_creator(pascal_triangle_list):
    # Cleaning zeros
    for row in pascal_triangle_list:
        for number in row:
            if number == 0:
                row.remove(number)

    for visual_row in pascal_triangle_list:
        print(" " * (len(pascal_triangle_list) - len(visual_row)), end=" ")
        for piece in visual_row:
            print(piece, end=" ")
        print()


pascal_triangle_creator(pascal_triangle_list_creator(6))
