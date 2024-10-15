

def generate_diamond(size):
    result = ""

    for line in range(size):
        width = 2*line -1
        initial_blanks = int(((2*size-1) - (width))/2)
        result += " " * initial_blanks + "#" * (width) +  "\n"

    for line in range(size):
        width = 2 * (size - line) - 1
        initial_blanks = int(((2 * size - 1) - (width)) / 2)
        result += " " * initial_blanks + "#" * (width) + "\n"

    return result


# /Users/efeberkev/Desktop/Python/CMPE150/pythonQuizes/testFileRead_week3 for input file
input_file = input("Input file path: ")
# /Users/efeberkev/Desktop/Python/CMPE150/pythonQuizes/testFileWrite_week3 for output file
answer_file_name = input("Output file path: ")


# Reading part
reading_scale = open(input_file, "r")
scale_of_diamond = int(reading_scale.readline())  # Reading value from file
reading_scale.close()

# Writing part
answer = open(answer_file_name, "w")
answer.write(generate_diamond(scale_of_diamond))
answer.close()
