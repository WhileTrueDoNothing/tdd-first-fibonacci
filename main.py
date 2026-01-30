def first_fib(num1, num2):
    if num2-num1 > num1:
        return (num1, num2)
    else:
        return first_fib((num2-num1), num1)