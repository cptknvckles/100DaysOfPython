#text based calculator
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}
single_line = []
num1 = int(input("Enter first number: "))
for operands in operations:
    single_line.append(operands)
print(" ".join(single_line))
keep_going = True
while keep_going:
    operand_symbol = input('choose operation from list above: ')
    num2 = int(input("Enter next number: "))
    answer = operations[operand_symbol](num1,num2)
    print(f"{num1} {operand_symbol} {num2} = {answer}")

    if input(f'y/n continue with {answer}, or exit: ') == 'y':
        num1 = answer
    else:
        print('see ya!')
        keep_going = False