#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# создайте словарь, где ключами являются числа, а значениями – строки.
#Примените к нему метод items(), c с помощью полученного объекта dict_items
# создайте новый словарь, "обратный" исходному, т. е. ключами являются строки,
# а значениями – числа.

if __name__ == '__main__':
    dict = {1: 'aaa', 2: 'bbb', 3: 'ccc'}
    print("Словарь:", dict)
    dict_new = {v: k for k, v in dict.items()}
    print("Измененный словарь:",dict_new)