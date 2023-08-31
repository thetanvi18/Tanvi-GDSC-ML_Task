def perform_operation(numbers, operands):
    result = numbers[0]
    for i in range(len(operands)):
        if operands[i] == "+":
            result += numbers[i+1]
        elif operands[i] == "-":
            result -= numbers[i+1]
        elif operands[i] == "*":
            result *= numbers[i+1]
        elif operands[i] == "/":
            try:
                result /= numbers[i+1]
            except ZeroDivisionError:
                print("You tried to divide by 0! So this program will be terminated")
                exit()
    return str(result)

exp = input("Enter an expression: ")
numbers, operands = [], []

if len(numbers) <= 10 and len(operands) <= 10:
    result = perform_operation(numbers, operands)
    if float(result).is_integer():
        print(int(float(result)))
    else:
        print(result)
else:
    print("Too many numbers or operators.")
