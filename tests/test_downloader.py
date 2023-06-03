import asyncio
import sys
import time
from unittest import TestCase

from http_client import HttpClient


class TestHttpClient(TestCase):
    maxDiff = None
    urls = [
        f"/api/v2/pokemon/{index}" for index in range(1, 151)
    ]

    def setUp(self) -> None:
        self.http_client = HttpClient(
            urls=self.urls
        )

    def test_async_and_sync_http_client_compare(self):
        print(f"Python version: {sys.version}")
        start = time.time()

        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.http_client.run())

        end = time.time()
        async_time = end - start
        print(f"async_time: {async_time}")

        start = time.time()

        self.http_client.sync_run()

        end = time.time()
        sync_time = end - start
        print(f"sync_diff: {sync_time}")
        print(f"sync_diff / async_diff: {sync_time / async_time}")
