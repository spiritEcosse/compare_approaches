import io

from pdf2image import convert_from_path


class Pdf2Image:

    def __init__(self, file_name):
        self.file_name = file_name

    def run(self):
        images = convert_from_path(self.file_name)
        img_byte_arr = io.BytesIO()
        images[0].save(img_byte_arr, format='PNG')
        return img_byte_arr.getvalue()
