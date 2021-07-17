# -*- coding: utf-8 -*-
import time


def day_of_the_week(week_day, lang_type='en'):
    """
    Check Day Of The Week
    0:Mon(월), 1:Tue(화), 2:Wed(수), 3:Thu(목), 4:Fri(금), 5:Sat(토), 6:Sun(일)
    :param week_day: Week Day
    :param lang_type: Return Lang(Default:En)
    :return:
    """
    tm = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    if lang_type == 'ko':
        tm = ['월', '화', '수', '목', '금', '토', '일']
    return tm[week_day]


if __name__ == '__main__':
    # 오늘 날짜의 요일
    wday = time.localtime().tm_wday
    print(wday)

    # 오늘 날짜의 요일 변환
    print(day_of_the_week(wday))
    print(day_of_the_week(wday, 'ko'))

    # 오늘의 날짜
    today = "{year}년 {month}월 {day}일 {wday}요일".format(
       year=time.localtime().tm_year, month=time.localtime().tm_mon,
       day=time.localtime().tm_mday, wday=day_of_the_week(time.localtime().tm_wday, 'ko')
    )
    print(today)

