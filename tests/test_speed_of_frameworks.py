"""
Before running this test , please run django with gunicorn, fastapi with uvicorn and aiohttp like in my video.
You can run this test or just run test_speed_of_frameworks.sh.
"""

import logging
import re
import subprocess
from unittest import TestCase

wrk_output = 'Running 2s test @ http://127.0.0.1:8000/db_query_sleep_100_milliseconds\n  8 threads and 400 connections\n  Thread Stats   Avg      Stdev     Max   +/- Stdev\n    Latency     1.02s   549.99ms   1.88s    62.50%\n    Req/Sec     6.65      3.95    10.00     82.35%\n  17 requests in 2.03s, 4.73KB read\n  Socket errors: connect 0, read 228, write 7, timeout 1\nRequests/sec:      8.37\nTransfer/sec:      2.33KB\n'
wrk_output_10 = 'Running 2s test @ http://127.0.0.1:8000/db_query_sleep_100_milliseconds\n  8 threads and 400 connections\n  Thread Stats   Avg      Stdev     Max   +/- Stdev\n    Latency     1.02s   549.99ms   1.88s    62.50%\n    Req/Sec     6.65      3.95    10.00     82.35%\n  17 requests in 2.03s, 4.73KB read\n  Socket errors: connect 0, read 228, write 7, timeout 1\nRequests/sec:  10.37\nTransfer/sec:      2.33KB\n'

speed = "Requests/sec:"
wrk_command = "/opt/homebrew/bin/wrk -t8 -c400 -d2s"


def parse_wrk_output(output):
    """
    >>> parse_wrk_output(wrk_output)
    8
    >>> parse_wrk_output(wrk_output_10)
    10

    """
    return int(re.search(r"Requests/sec:\s*(\d+)", str(output)).group(1))


def run_wrk(framework_data):
    output = subprocess.check_output(framework_data['command'], shell=True)
    print(output)
    return {"framework": framework_data['framework'], speed: parse_wrk_output(output)}


class TestSpeedFrameworks(TestCase):
    urls = [
        {"framework": "django", "command": f"{wrk_command} http://127.0.0.1:8000"},
        {"framework": "fastapi", "command": f"{wrk_command} http://127.0.0.1:9999"},
        {"framework": "aiohttp", "command": f"{wrk_command} http://127.0.0.1:8080"},
    ]

    def test_speed(self):
        results = [run_wrk(url) for url in self.urls]

        logging.info(results)
        first = results[0]['framework']
        logging.info(first)

        for previous in results:
            for index, result in enumerate(results[1:]):
                difference = int(result[speed] - previous[speed])
                if difference > 0:
                    logging.info(f"{result['framework']} faster than {previous['framework']} on {difference} requests")
