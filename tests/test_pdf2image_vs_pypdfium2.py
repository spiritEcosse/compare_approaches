# import os
# from unittest import TestCase
#
# import boto3
#
# from pdf.lib_pdf2image import Pdf2Image
# from pdf.lib_pypdfium2 import PYPdfiumToImage
# from settings import BASE_DIR
#
#
# class TestComparePdf2imageVsPYPdfium(TestCase):
#     maxDiff = None
#     textract = boto3.client('textract')
#
#     def test_pdf2image_vs_pypdfium2(self):
#         pdf_file = os.path.join(BASE_DIR, 'INV-4653.pdf')
#         image_bytes = Pdf2Image(pdf_file).run()
#         pdf2image_res = self.s3_textract(image_bytes)
#
#         image_bytes = PYPdfiumToImage(pdf_file).run()
#         pypdfium2_res = self.s3_textract(image_bytes)
#
#     def s3_textract(self, image_bytes):
#         return self.textract.analyze_expense(Document={'Bytes': image_bytes})
