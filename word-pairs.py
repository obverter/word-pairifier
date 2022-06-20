#!/usr/bin/env python
# coding: utf-8

from funny_words import build_n_gram
import pandas as pd

groups = []


def genpairs(x, y):
    for _ in range(y):
        for _ in range(x):
            pair = [build_n_gram(1) for _ in range(2)]
            groups.append(pair)
    return list(groups)


x = input("How many words per pair?\n  >")
y = input("How many pairs?\n  >")

genpairs(2, 1000)

df = pd.DataFrame(groups)

name = input("Name the csv:\n  >")

df.to_csv(f"{name}.csv")
