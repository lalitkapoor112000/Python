def outer_func():
    def inner_func():
        print("Inside inner function")
    return inner_func

var=outer_func()
var()
