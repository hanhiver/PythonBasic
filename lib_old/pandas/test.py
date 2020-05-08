#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 16:52:09 2019

@author: dhan
"""

import pandas as pd 

df = pd.read_excel('test.xlsx')
#print(df['项目'])
"""
print(df.iloc[2, 2])

print(df.iloc[2:4, 2:4])

# 找到所有参加人员（独一无二）
print(df['参加人员'].unique())

# 找到总费用大于10的所有条目。
d = df[df['总费用 （KRMB）']>10]
print(d)

d.to_excel('res.xlsx')
"""
print(df.head())