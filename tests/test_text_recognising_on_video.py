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
