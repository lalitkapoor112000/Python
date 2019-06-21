def decorator_function(any_func):
    def wrapper_func():
        print("This is awesome function:")
        any_func()
    return wrapper_func

@decorator_function #func1=decorator_function(func1)
def func1():
    print("This is functuion 1")
func1()
