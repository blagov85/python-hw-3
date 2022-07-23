def spiral(matrix):
    if type(matrix) != list:
        return 'Argument of function is not list'
    elif (len(matrix) == 0):
        return 'The list is empty'
    for ind_row in range(0, len(matrix)):
        if(len(matrix[ind_row]) == 0):
            return 'The item of list is empty'
    count_first_item = len(matrix[0])
    for ind_row in range(1, len(matrix)):
        if(count_first_item != len(matrix[ind_row])):
            return 'All items of list must be the same size'
    spiral_array = []
    while(len(matrix) > 0):
        for index_column in range(0, (len(matrix[0]))):
            spiral_array.append(matrix[0][index_column])  
        if(len(matrix) > 2):
            for index_row in range(1, (len(matrix) - 1)):
                spiral_array.append(matrix[index_row][len(matrix[index_row]) - 1])  
        if(len(matrix) > 1):
            for index_column in range((len(matrix[len(matrix) - 1]) - 1), -1, -1):
                spiral_array.append(matrix[len(matrix) - 1][index_column]) 
        if(len(matrix) > 2):
            for index_row in range((len(matrix) - 2) , 0, -1):
                spiral_array.append(matrix[index_row][0])
        matrix.pop(0)
        if(len(matrix) > 1):
            matrix.pop(len(matrix) - 1)
        for index_row in range(0, len(matrix)):
            matrix[index_row].pop(len(matrix[index_row]) - 1)
            matrix[index_row].pop(0)
    return spiral_array

array = [
            [1,2,3,4],
            [5,6,7,8],
            [9,10,11,12]
        ]
print(spiral(array))

array = [
            [1,2],
            [5,6],
            [9,10]
        ]
print(spiral(array))

array = [
            [1,2],
            [5,6]
        ]
print(spiral(array))
#
array = [
            [1,2,3,4],
            [5,6,7,8],
            [9,10,12],
            [13,14,15,16],
            [17,18,19,20]
        ]
print(spiral(array))

array = [
            [1,2,3,4]
        ]
print(spiral(array))

array = [
            [1, 2,  3, 4,5, 6,  7,8,  9,10],
            [11,12,13,14,15,16,17,18,19,20],
            [21,22,23,24,25,26,27,28,29,30],
            [31,32,33,34,35,36,37,38,39,40],
            [41,42,43,44,45,46,47,48,49,50],
            [51,52,53,54,55,56,57,58,59,60],
            [61,62,63,64,65,66,67,68,69,70],
            [71,72,73,74,75,76,77,78,79,80],
            [81,82,83,84,85,86,87,88,89,90],
            [91,92,93,94,95,96,97,98,99,100]
        ]
print(spiral(array))

array = [
            []
        ]
print(spiral(array))

array = [
            [1,2,3,4],
            [],
            [9,10,11,12]
        ]
print(spiral(array))
