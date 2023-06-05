"""
In this test I am going check, how to recognize text from video.

If you know other interesting approaches let me know in the comments
then I can create different video to compare them all
I would appreciate it.

https://github.com/spiritEcosse/compare_approaches/blob/main/tests/test_text_recognising_on_video.py
"""

import asyncio
from unittest import TestCase

from aws.text_recognising_on_video import TextRecognisingOnVideo


class TestTextRecognisingOnVideo(TestCase):

    def test_text_detection(self):
        loop = asyncio.get_event_loop()
        recognising = TextRecognisingOnVideo("text_recognising_on_video.mov")
        real = loop.run_until_complete(recognising.run())
        self.assertSetEqual(
            {
                'Third', 'Fourth', 'Second',
                'Seco', 'Fourt', '+', 'Fo',
                'untitled', 'First', 'Thi', 'F', '1'
            },
            real
        )
