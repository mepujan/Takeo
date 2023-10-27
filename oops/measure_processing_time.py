import time


def processing_time(func):
    def calculate_time(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        time.sleep(2)
        end_time = time.time()
        time_elapsed = end_time - start_time
        print("Function Execution time is: ", time_elapsed, "ms")
        return result

    return calculate_time


@processing_time
def greet(text):
    print(text)


greet("Hello How are you?")
