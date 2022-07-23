def double_zero(array):
    if type(array) != list:
        return 'Argument of function is not list'
    elif (len(array) == 0):
        return 'The list is empty'
    else:
        ind = 0
        while(ind < len(array)):
            if(array[ind] == 0):
                array.insert(ind + 1, 0)
                ind = ind + 1
            ind = ind + 1
        return array

print(double_zero([1,0,2,3,0,4,5,0]))
print(double_zero([1,2,3]))
print(double_zero([3,4,0,7,12,0,2,8,0,0,2]))
print(double_zero([]))
print(double_zero(2))
print(double_zero(['cat',0,'dog',3,0,'0',5,0]))