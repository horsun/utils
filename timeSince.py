from datetime import datetime


def my_timeSince(value):
    """

    if now 2018-10-10 22:01:00
    transform 2018-10-10 22:00:00 >>>>  1 分钟前

    django 自带的也有这个方法
    详见 django-人性化 官方文档： https://docs.djangoproject.com/en/dev/ref/contrib/humanize/

    :param value: datetime
    :return:
    """
    day_log = str(datetime.now() - value)

    if 'day' in day_log:
        return str(int(day_log.split('day')[0])) + '天前'
    # elif
    else:
        all_log = day_log.split(':')
        if str(int(all_log[0])) != '0':
            return all_log[0] + '小时前'
        else:
            if int(all_log[1]) < 10:
                return '刚刚'
            return str(int(all_log[1])) + '分钟前'
