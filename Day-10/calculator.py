# sum
def sum(num1 , num2):
    return num1 + num2
# sub
def sub(num1 , num2):
    return num1 - num2
# sum
def mul(num1 , num2):
    return num1 * num2
# sum
def div(num1 , num2):
    return num1 / num2

operations = {
    "+" : sum,
    "-" : sub,
    "*" : mul,
    "/" : div,
}

def calculator():
    num1 = int(input("Number one: "))
    for key in operations:
        print(key)
    continue_operation = True

    while continue_operation:
        operation_symbol = input("Give the symbol ")
        num2 = int(input("Number two: "))
        calculate_function = operations[operation_symbol] # get from the operation list
        answer= calculate_function(num1, num2)

        print(f"The {num1} {operation_symbol} {num2} = {answer}")
        response = input("Want to do a new calculation 'yes' or 'no' ")
        if response == "yes":
            answer = num1
        else:
            continue_operation = False
            calculator()

calculator()