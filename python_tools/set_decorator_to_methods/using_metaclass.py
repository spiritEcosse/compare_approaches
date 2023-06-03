import functools
import time
import types


class MeasureTimeOfExecutionMeta(type):
    def __new__(cls, name, bases, attrs):
        for attr_name, attr_value in attrs.items():
            if isinstance(attr_value, types.FunctionType):
                attrs[attr_name] = cls.measure_time_of_execution(attr_value)

        return super().__new__(cls, name, bases, attrs)

    @classmethod
    def measure_time_of_execution(cls, function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = function(*args, **kwargs)
            end = time.time()
            diff = end - start
            # print(f"{function.__name__} took {diff} seconds, {diff / 60} minutes.")
            return result
        return wrapper


class MyClass(metaclass=MeasureTimeOfExecutionMeta):

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
