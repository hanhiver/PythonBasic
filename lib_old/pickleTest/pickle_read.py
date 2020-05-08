#!/usr/bin/python3
import pprint, pickle

#使用pickle模块从文件中重构python对象
with open('data.pkl', 'rb') as pkl_file:
    data1 = pickle.load(pkl_file)
    pprint.pprint(data1)

    data2 = pickle.load(pkl_file)
    pprint.pprint(data2)

#pkl_file.close()
