import sys

def calc(left_operand, right_operand, operation):
    try:
        left_operand = int(left_operand)
        right_operand = int(right_operand)
    except ValueError:
        print('Left and Right operands must be int')
        sys.exit()

    if (operation == '/' or operation == '%') and right_operand == 0:
        print('Division by zero is not allowed')
        sys.exit()
    if(operation == "+"):
        result = left_operand + right_operand
    elif(operation == "-"):
        result = left_operand - right_operand
    elif(operation == "*"):
        result = left_operand * right_operand
    elif(operation == "/"):
        result = left_operand / right_operand
    elif(operation == "%"):
        result = left_operand % right_operand
    return result


if (len(sys.argv) != 2) and (len(sys.argv) != 4):
    print('Arg len should be 2 or 4')
    sys.exit()

allowed_operations = ['+', '-', '/', '*', '%']

if(len(sys.argv) == 2):
    operation = None
    for operation_item in allowed_operations:
        operands = sys.argv[1].split(operation_item)
        if(len(operands) >= 2):
            operation = operation_item
            left_operand, right_operand = operands
            break
    if(operation == None):
        print('Operation is not allowed')
        sys.exit()   
elif(len(sys.argv) == 4):
    left_operand = sys.argv[1]
    right_operand = sys.argv[3]
    operation = sys.argv[2]
    if operation not in allowed_operations:
        print('Operation is not allowed')
        sys.exit()



print(calc(left_operand, right_operand, operation))

