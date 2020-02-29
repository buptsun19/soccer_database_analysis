# -*- coding: utf-8 -*-

"""
    作者：sun19
    版本：v1.0
    日期：2020.02
    文件名：main.py主程序
    功能：对soccer.db数据库中的球员信息进行提取、处理，最终输出球员姓名、年龄、身高、体重以及在FIFA中的评分信息等
    备注：scooer.db为球员信息数据库，table_structure.csv为数据库中表的结构及解释信息
"""

import sqlite3
import json

import tools
import file_convert

# 获取文件路径
db_filepath = './datafile/soccer.db'
json_savepath = './player_info.json'


def soccer_info(cur, player_num=None):

    # 构造SQL语句
    if player_num is None:
        sql_query = 'select * from Player;'
    else:
        sql_query = 'select * from Player limit {};'.format(player_num)

    results = cur.execute(sql_query).fetchall()

    player_list = []
    for each_result in results:
        player = dict()
        player['name'] = each_result[2]
        player['weight'] = each_result[5]
        player['height'] = each_result[6]

        birthday_str = each_result[4]
        player['age'] = tools.get_age(birthday_str)

        player_api_id = each_result[1]
        player['average_rating'] = tools.get_rating(cur, player_api_id)

        player_list.append(player)

    with open(json_savepath, 'w') as f:
        json.dump(player_list, f)


def main():

    # 连接数据库
    conn = sqlite3.connect(db_filepath)
    cursor = conn.cursor()

    # 数据获取和分析
    soccer_info(cursor, player_num=50)

    # 关闭数据库
    conn.close()

    # 对输出的json文件进行处理，写入到CSV文件中，并使用pandas进行排序处理
    file_convert.process_file('./player_info.json')


if __name__ == '__main__':
    main()
