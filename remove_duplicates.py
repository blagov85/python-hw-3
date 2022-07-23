def remove_duplicates(array):
    if type(array) != list:
        return 'Argument of function is not list'
    elif (len(array) == 0):
        return 'The list is empty'
    else:
        for ind in range(1, len(array) - 1):
            if(array[ind-1] > array[ind]):
                return 'List must be sorted ascending'
        ind = 0
        while(ind < len(array)):
            while((ind + 1) < len(array)):
                if(array[ind] == array[ind + 1]):
                    array.pop(ind + 1)
                else:
                    break
            ind = ind + 1
        return array

print(remove_duplicates([1,1,2]))
print(remove_duplicates([0,0,1,1,1,2,2,3,3,4]))
print(remove_duplicates([1,1,1,1,1,1,1,1]))

print(remove_duplicates([0,0,0,1,1,3,3,3,5,6,6,10,10,10,13]))
print(remove_duplicates([0,0,0,1,7,3,3,3,5,3,6,10]))
print(remove_duplicates(4))