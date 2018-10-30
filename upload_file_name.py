import time
from datetime import datetime


# Usage:

# 在 ImageField 中的upload_to中调用这个 img_path_name 方法就能实现 修改上传图片的文件名了

# in django models
#
# class OriginImage(BaseModel):
#     img = models.ImageField(upload_to=img_path_name, null=True, blank=True, verbose_name='图片')
#     thumb_img = models.CharField(max_length=255, verbose_name='缩略图地址', blank=True, null=True)
#
#     class Meta:
#         verbose_name = '图片'
#         verbose_name_plural = verbose_name


def img_path_name(instance, filename):
    ext = filename.split('.')[-1]
    new_fileName = str(instance.pk) + str(time.time() * 1000).split('.')[0] + '.' + ext
    return 'exam/{0}/{1}/{2}'.format(datetime.now().year, datetime.now().month, new_fileName)
