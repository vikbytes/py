def contains2d(text, pattern):
    pattern_rows = len(pattern)
    pattern_columns = len(pattern[0])
    text_rows = len(text)
    text_columns = len(text[0])
    for row_x in range(text_rows - pattern_rows + 1):
        for column_x in range(text_columns - pattern_columns + 1):
            sub_matrix = []
            for row_y in range(pattern_rows):
                line_matrix = []
                for column_y in range(pattern_columns):
                    line_matrix.append(text[row_x+row_y][column_x+column_y])
                sub_matrix.append(line_matrix)
            if sub_matrix == pattern:
                return True
    return False
    
    
first = input().split(" ")
n1, m1 = int(first[0]), int(first[1])
first_matrix = []
for n in range(n1):
    first_matrix.append(list(input()))
    
second = input().split(" ")
n2, m2, = int(second[0]), int(second[1])
second_matrix = []
for n in range(n2):
    second_matrix.append(list(input()))
    
print(contains2d(first_matrix, second_matrix))
