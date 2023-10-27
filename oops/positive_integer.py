#  rules is parameters in add_two_numbers(a,b) function should be positive integer number

def is_positive_number(func):
    def check(*args, **kwargs):
        for num in args:
            if not isinstance(num, int) or num < 0:
                raise ValueError("Number must be positive integer value.")
        return func(*args, **kwargs)
    return check


@is_positive_number
def add_two_numbers(a, b):
    print("Sum is: ", a+b)


add_two_numbers(-4, 5)
