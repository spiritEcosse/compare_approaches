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
