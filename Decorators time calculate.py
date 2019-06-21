from functools import wraps
import time
def calculate_time(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print(f"You called {func.__name__} function")
        print("{}".format(func.__doc__))
        func()
    return wrapper


@calculate_time
def timer():
    t1=time.time()
    print("Aldsadfsdf")
    t2=time.time()
    print(f"Time took={t2-t1}")
timer()
