import glob
import os

from PIL import Image


def create_thumb_pic(path, size=(128, 128)):
    """
    等比压缩
    """
    for infile in glob.glob(str(path)):
        file, ext = os.path.splitext(infile)
        im = Image.open(infile)
        bg_mode = im.mode
        if bg_mode != 'RGB':
            im = im.convert("RGB")
        im.thumbnail(size)
        file_name = file.split('/')[-1]
        new_file = file.replace(file_name, 'thumb' + file_name)
        im.save(new_file + ext, "JPEG")
        thum_path = '/' + new_file + ext
        return thum_path
