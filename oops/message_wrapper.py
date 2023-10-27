def print_message(func):
    def wrapper(*args, **kwargs):
        print("This is the message printing before calling the function.")
        message = func(*args, **kwargs)
        print("Message After calling the function.")
        return message

    return wrapper


@print_message
def greet():
    print("Hi I am Pujan Gautam. I am doing well.")


@print_message
def ask():
    print("Why python is so flexible language?")


greet()
ask()
