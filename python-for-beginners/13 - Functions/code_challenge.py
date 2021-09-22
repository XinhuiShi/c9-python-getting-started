# Create a calculator function
# The function should accept three parameters:
# first_number: a numeric value for the math operation
# second_number: a numeric value for the math operation
# operation: the word 'add' or 'subtract'
# the function should return the result of the two numbers added or subtracted
# based on the value passed in for the operator

def calculator(first_number, second_number, operation):
    try:
        if (str(operation.lower()) == 'add'):
            return first_number+second_number
        elif (str(operation.lower()) == 'subtract'):
            return first_number-second_number
        elif (str(operation.lower()) == 'divide'):
            return first_number/second_number
    except:
        print("An error has occured")
        return 'null'



num = calculator(6, 4, 'add')
num2 = calculator(6, 4, 'subtract')
num3 = calculator(6, 4, 'divide')
num4 = calculator('asdf', 4, 'divide')

print(num)
print(num2)
print(num3)
print(num4)
# Test your function with the values 6,4, add 
# Should return 10
#
# Test your function with the values 6,4, subtract 
# Should return 2
# 
# BONUS: Test your function with the values 6, 4 and divide 
# Have your function return an error message when invalid values are received

