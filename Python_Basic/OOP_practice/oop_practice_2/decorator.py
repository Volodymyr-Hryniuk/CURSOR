from datetime import datetime


def timer(function):
    def wrapper(*arg, **kwargs):
        start = datetime.now()
        result = function(*arg, **kwargs)
        end = datetime.now()
        print("function execution time: {time.seconds}s, {time.microseconds}ms".format(time=end - start))

        return result

    return wrapper
