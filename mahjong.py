#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random


random.seed()


hai = list()
hai_count_d = dict()


# 数牌を作成
def make_suhai():
    H = [str(i) + suhai for suhai in ["man", "sou", "pin"]
         for i in range(1, 10)]
    l = list()
    for i in range(0, 3):
        l.append(H[i*9:(i+1)*9])
    return l

JIHAI = ["ton", "nan", "sha", "pei", "haku", "hatsu", "chun"]
SUHAI = make_suhai()


def insert_dict(hai):
    if hai in hai_count_d:
        hai_count_d[hai] += 1
    else:
        hai_count_d[hai] = 1


# 雀頭をつくる
def head(i=random.randrange(4)):
    if i == 3:
        j = random.randrange(8)
        # 字牌がhai_count_dに含まれていないか含まれていても4個以下の場合
        if JIHAI[j] not in hai_count_d or hai_count_d.get(JIHAI[j]) <= 4:
            hai.append(JIHAI[j])
            hai.append(JIHAI[j])
        else:
            head(i)
    else:
        j = random.randrange(9)
        print(SUHAI[i][j])
        # 数牌がhai_count_dに含まれていないか含まれていても4個以下の場合
        if SUHAI[i][j] not in hai_count_d or hai_count_d.get(SUHAI[i][j]) <= 4:
            hai.append(SUHAI[i][j])
            hai.append(SUHAI[i][j])
        else:
            head(i)
