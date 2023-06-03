"""
In this test we are going to compare speed of running 'metaclass' to set a decorator and 'inspect' to set a decorator.

If you know other interesting approaches let me know in the comments
then I can create different video to compare them all,
I would appreciate it.

https://github.com/spiritEcosse/compare_approaches/blob/main/tests/python_tools_set_decorators.py
"""

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
