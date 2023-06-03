import asyncio
import logging
import aioboto3
from aws.models.video_detect_model import TextDetections
from settings import BUCKET_VIDEO

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class TextRecognisingOnVideo:
    bucket = BUCKET_VIDEO

    def __init__(self, s3_key_video):
        self.s3_key_video = s3_key_video

    async def _text_detection(self):
        session = aioboto3.Session()
        async with session.client("rekognition") as rekognition:
            response = await rekognition.start_text_detection(
                Video={'S3Object': {'Bucket': self.bucket, 'Name': self.s3_key_video}},
            )

            self.startJobId = response['JobId']
            logger.info(f'Start Job Id: {self.startJobId}, file_name: {self.s3_key_video}')

            max_results = 10
            pagination_token = ''
            finished = False

            logger.info(f's3_key : {self.s3_key_video}, file_name: {self.s3_key_video}')
            data = set()

            while not finished:
                await asyncio.sleep(1)
                response = await rekognition.get_text_detection(
                    JobId=self.startJobId,
                    MaxResults=max_results,
                    NextToken=pagination_token
                )

                if response['JobStatus'] == 'IN_PROGRESS':
                    logger.info(f'Job is still in progress , startJobId: {self.startJobId}, file_name: {self.s3_key_video}')
                    continue
                if response['JobStatus'] == 'FAILED':
                    raise Exception(f'Label detection failed for {self.s3_key_video}, response: {response}')

                logger.info(f"JobStatus: {response['JobStatus']}, startJobId: {self.startJobId}, file_name: {self.s3_key_video}")

                for text_detection in response['TextDetections']:
                    text_detections = TextDetections.from_dict(text_detection)
                    data.add(text_detections.TextDetection.DetectedText)

                if 'NextToken' in response:
                    pagination_token = response['NextToken']
                else:
                    finished = True

            return data

    async def run(self):
        return await self._text_detection()
