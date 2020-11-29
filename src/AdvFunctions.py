# More complicated functions to implement
import math
# Returns both result of integer division and modulo
def int_division(num1, num2):
    return NotImplemented


# Returns factorial of given number
def factorial(num):
    if num == int:
        if num > 0:
            return (math.factorial(num))
        elif num == 0:
            return 1
        else:
            print('We can not make factorial of negative number. Please enter a valid input')
    else:
        print('We need a natural number to count a factorial. Please enter a valid input.')

# Returns all solutions of given quadratic equation
def quadratic_eq(qdr_coef, lin_coef, const):
    if qdr_coef == 0:
        print('The first number must not be zero. Please input a valid number next time.')
    else:
        dis = lin_coef * lin_coef - 4 * qdr_coef - 4 * const
        if dis < 0:
            print("The result is not a real number.")
        else:
            resx1 = (-lin_coef + math.sqrt(dis)) / (2 * qdr_coef)
            resx2 = (-lin_coef - math.sqrt(dis)) / (2 * qdr_coef)
            return resx1, resx2
