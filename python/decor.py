def my_decorator(func):
    import functools

    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        value = func(*args, **kwargs)
        return value

    return wrapper_decorator


@my_decorator
def say_whee():
    print("Whee!")


@my_decorator
def pow(a, b):
    return a**b


if __name__ == "__main__":
    print("d" * 80)
    print(__name__)
    print(pow(2, 16))
    say_whee()
