#task

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
matrix = []

#To Read the matrix content
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)


result = ""

# Iterate
for col in range(m):
    for row in range(n):
        char = matrix[row][col]
        if char.isalnum():
            result += char
        elif char == " ":

            if result and result[-1] != " ":
                result += " "
        else:

            if result and result[-1] != " ":
                result += " "

# Print the result
print(result)

