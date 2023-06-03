import io

import pypdfium2 as pdfium


class PYPdfiumToImage:

    def __init__(self, file_name):
        self.file_name = file_name

    def run(self):
        pil_image = pdfium.PdfDocument(self.file_name)[0].render().to_pil()
        img_byte_arr = io.BytesIO()
        pil_image.save(img_byte_arr, format='PNG')
        return img_byte_arr.getvalue()
