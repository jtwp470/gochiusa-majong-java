#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random


random.seed(143)


hai = list()
hai_count_d = dict()
used_random_num = list()


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


# 雀頭
def head(i=random.randrange(4)):
    if i == 3: # ここはランダム値
        j = random.randrange(7)
        used_random_num.append(j)
        print(j)
        # 字牌がhai_count_dに含まれていないか含まれていても4個以下の場合
        if JIHAI[j] not in hai_count_d or hai_count_d.get(JIHAI[j]) <= 4:
            for k in range(2):
                insert_dict(JIHAI[j])
                hai.append(JIHAI[j])
        else:
            head()
    else:
        j = random.randrange(9)
        used_random_num.append(j)
        # 数牌がhai_count_dに含まれていないか含まれていても4個以下の場合
        if SUHAI[i][j] not in hai_count_d or hai_count_d.get(SUHAI[i][j]) <= 4:
            for k in range(2):
                insert_dict(SUHAI[i][j])
                hai.append(SUHAI[i][j])
        else:
            head()


# 順子
def shuntsu(i=random.randrange(4)):
    j = random.randrange(7) + 2
    used_random_num.append(j+2)
    for suhai in SUHAI[i][j-1:j+1]:
        if suhai not in hai_count_d or hai_count_d.get(suhai) <= 4:
            pass  # 何もしない
        else:
            shuntsu()

    for suhai in SUHAI[i][j-2:j+1]:
        # SUHAI[i][j-2:j+1]はCofeeScriptでもできるけどPythonと範囲が違うので注意.
        # Python では  [X:Y]のとき Xを含みYを含まない
        # CF では [X...Y] のとき   Xを含みYを含まないようにすることができる(らしい)
        insert_dict(suhai)
        hai.append(suhai)


# 刻子
def kotsu(i=random.randrange(4)):
    if (i == 3):
        j = random.randrange(7)
        used_random_num.append(j)
        if JIHAI[j] not in hai_count_d or hai_count_d.get(JIHAI[j]) < 2:
            for k in range(3):
                insert_dict(JIHAI[j])
                hai.append(JIHAI[j])
        else:
            kotsu()

    else:
        j = random.randrange(9)
        used_random_num.append(j)
        if SUHAI[i][j] not in hai_count_d or hai_count_d.get(SUHAI[i][j]) < 2:
            for k in range(3):
                insert_dict(SUHAI[i][j])
                hai.append(SUHAI[i][j])
        else:
            kotsu()


def check():
    for count in hai_count_d.values():
        if count >= 5:
            print("Error OCCURED")
            print("===== DEBUG =====")
            print(hai_count_d)
            print(hai)
            print(used_random_num)
            print("===== MAKE AGAIN =====")
            import time
            time.sleep(1)
            main()


def make_body():
    choice = random.randrange(2)
    if choice == 0:
        used_random_num.append("shuntsu()")
        shuntsu()
    else:
        used_random_num.append("kotsu()")
        kotsu()


def main():
    global hai
    global hai_count_d
    global used_random_num

    hai = list()
    hai_count_d = dict()
    used_random_num = list()

    head()
    for i in range(4):
        make_body()
    check()
    print(hai)


def tests():
    global hai
    global hai_count_d

    hai = list()
    hai_count_d = dict()

    head(0)  # 字牌以外を選ぶ
    kotsu(1)
    kotsu(1)
    kotsu(1)
    kotsu(1)
    print(hai)
    check()


if __name__ == "__main__":
    for i in range(10000):
        print(str(i) + ": ", end='')
        main()
        # tests()
