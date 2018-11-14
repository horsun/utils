import time
from PIL import Image, ImageFont, ImageDraw

BASE_IMAGE_PATH = 'share_base.jpg'


def mark_my_pic(user_head=None, background=Image.open(BASE_IMAGE_PATH)):
    """

    :param user_head: 用户头像/或者 你想添加的水印图
    :param background: 被添加水印的base图
    :return:
    """
    # 修改image的mode 为RGB格式
    bg_mode = background.mode
    if bg_mode != 'RGB':
        background = background.convert("RGB")
    avatar = Image.open(user_head)

    # 头像初始化大小
    im = avatar.resize((50, 50))
    big_size = (im.size[0] * 3, im.size[1] * 3)

    # 制作圆形头像
    mask = Image.new('L', big_size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + big_size, fill=255)
    mask = mask.resize(im.size, Image.ANTIALIAS)
    im.putalpha(mask)

    # (100, 1050) 水印的位置
    background.paste(im, (100, 1050), im)

    draw = ImageDraw.Draw(background)

    # 内容
    text = '这里是水印内容'

    # 字体
    font = ImageFont.truetype('microsoft_yahei.ttf', size=40)

    # 文字颜色
    fillcolor = "#000000"

    # (100, 1050)文字水印的位置
    draw.text((200, 1050), str(text), font=font, fill=fillcolor)
    path_name = 'share' + str(time.time())[:10] + '.jpg'
    background.save(path_name, 'jpeg')
    return path_name


if __name__ == '__main__':
    mark_my_pic(user_head='my_head.jpeg')
