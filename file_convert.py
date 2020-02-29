# -*- coding: utf-8 -*-

"""
    作用：用于读取处理之后的json文件，并转换为CSV文件，使用pandas进行处理
"""
import pandas as pd
import csv
import json


def process_file(file):
    with open(file, 'r') as f:
        json_data = json.load(f)

    with open('player_info_csv.csv', 'w', newline='') as csvfile:
        fieldnames = ["name", "age", "height", "weight", "average_rating"]
        write = csv.DictWriter(csvfile, fieldnames=fieldnames)

        write.writeheader()
        write.writerows(json_data)

    data = pd.read_csv('./player_info_csv.csv')
    data = data.sort_values(by='average_rating', ascending=False)
    data.to_csv("./player_sort_info.csv")
