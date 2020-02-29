# -*- coding: utf-8 -*-

# 功能：工具文件

import datetime


def get_age(birthday):
    born = int(birthday.split('-')[0])   # '1992-02-29 00:00:00'
    current_year = datetime.datetime.now().date().year
    return current_year - born


def get_rating(cursor, player_id):
    rating_info = cursor.execute("select overall_rating from Player_Attributes where \
                                    player_api_id = {};".format(player_id)).fetchall()
    ratings = [float(rate_one[0])
               for rate_one in rating_info
               if rate_one[0] is not None
               ]
    return sum(ratings)/len(ratings)
