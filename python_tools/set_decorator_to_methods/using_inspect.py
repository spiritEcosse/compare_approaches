import functools
import inspect
import time


class MyClass:

    def func1(self):
        pass

    def func2(self):
        pass

    def func3(self):
        pass

    def func4(self):
        pass

    def run(self):
        self.func1()
        self.func2()
        self.func3()
        self.func4()


def measure_time_of_execution(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        end = time.time()
        diff = end - start
        # print(f"{function.__name__} took {diff} seconds, {diff / 60} minutes.")
        return result
    return wrapper


for name, fn in inspect.getmembers(MyClass, inspect.isfunction):
    setattr(MyClass, name, measure_time_of_execution(fn))
