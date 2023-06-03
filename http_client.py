import asyncio
from dataclasses import dataclass

import aiohttp
import requests
from aiohttp import ClientTimeout

HOST_API_URL = "pokeapi.co"
HOST_API_TOKEN = ""


@dataclass
class HttpClient:
    """
    A class representing a http_client

    >>> http_client = HttpClient(urls=['example.com/1', 'example.com/2'], token="1234567890", server="example.com/3")
    >>> http_client.urls
    ['example.com/1', 'example.com/2']
    >>> http_client.server
    'example.com/3'
    >>> http_client.token
    '1234567890'
    >>> http_client._header
    {'X-RapidAPI-Key': '1234567890', 'X-RapidAPI-Host': 'example.com/3'}

    """

    urls: list
    server: str = HOST_API_URL
    token: str = HOST_API_TOKEN

    @property
    def server_name(self) -> str:
        """
        >>> http_client = HttpClient(urls=['example.com/1'], server="example.com/3")
        >>> http_client.server_name
        'https://example.com/3'
        """
        return f"https://{self.server}"

    @property
    def _header(self, *args, **kwargs) -> dict:
        """A property to get the http_client header

        >>> http_client = HttpClient(urls=[], server='example.com', token='1234567890')
        >>> http_client._header
        {'X-RapidAPI-Key': '1234567890', 'X-RapidAPI-Host': 'example.com'}
        """
        return {
            'X-RapidAPI-Key': self.token,
            'X-RapidAPI-Host': self.server
        }

    async def request(self, response, url):
        if response.status < 500:
            data = await response.json()
            return url, response.status, data['name']
        return url, response.status, await response.text()

    async def get_response(self, session, url):
        async with session.get(url) as response:
            return await self.request(response, url)

    async def gather_tasks(self):
        async with aiohttp.ClientSession(self.server_name, headers=self._header, timeout=ClientTimeout(10 * 60)) as session:
            tasks = (asyncio.ensure_future(self.get_response(session, url)) for url in self.urls)
            return await asyncio.gather(*tasks)

    async def run(self):
        return await self.gather_tasks()

    def sync_run(self):
        with requests.Session() as session:
            return [
                self.sync_response(url, session.get(f"{self.server_name}{url}"))
                for url in self.urls
            ]

    def sync_response(self, url, response):
        if response.status_code < 500:
            return url, response.status_code, response.json()['name']
        return url, response.status_code, response.text()
