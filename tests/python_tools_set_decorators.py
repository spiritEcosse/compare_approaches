import timeit


class TestPythonToolsSetDecorator:

    def test_metaclass_vs_inspect(self):
        print("\n")
        data = dict()
        data['metaclass_time'] = timeit.Timer("""
from python_tools.set_decorator_to_methods.using_metaclass import MyClass
my_class = MyClass()
my_class.run()
        """).timeit()
        data['inspect_time'] = timeit.Timer("""
from python_tools.set_decorator_to_methods.using_inspect import MyClass
my_class = MyClass()
my_class.run()
        """).timeit()
        print(data, "improvement:", round(data['metaclass_time'] / data['inspect_time'], 2))
