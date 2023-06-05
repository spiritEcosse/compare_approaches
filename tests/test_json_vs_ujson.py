"""
In this test, I compare speed json and ujson speed approach.

If you know other interesting approaches let me know in the comments
then I can create other video to compare them all
I would appreciate it.


https://github.com/spiritEcosse/compare_approaches/blob/main/tests/test_json_vs_ujson.py
"""

import timeit


class TestJsonVsUjson:

    def test_json_vs_ujson(self):
        print("\n")
        data = dict()
        data['json_dumps_time'] = timeit.Timer("""
import json
json.dumps([{"key": "value"}, 81, True])
        """).timeit()
        data['ujson_dumps_time'] = timeit.Timer("""
import ujson
ujson.dumps([{"key": "value"}, 81, True])
        """).timeit()
        print(data, "improvement:", round(data['json_dumps_time'] / data['ujson_dumps_time'], 2))

        data = dict()
        data['json_loads_time'] = timeit.Timer("""
import json
json.loads('[{"key": "value"}, 81, true]')
        """).timeit()
        data['ujson_loads_time'] = timeit.Timer("""
import ujson
ujson.loads('[{"key": "value"}, 81, true]')
        """).timeit()
        print(data, "improvement:", round(data['json_loads_time'] / data['ujson_loads_time'], 2))
