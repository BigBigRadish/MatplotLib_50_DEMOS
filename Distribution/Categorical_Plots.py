# -*- coding: utf-8 -*-
'''
Created on 2019年1月16日 下午5:01:54
Zhukun Luo
Jiangxi University of Finance and Economics
'''
'''
分类图
由 seaborn库 提供的分类图可用于可视化彼此相关的2个或更多分类变量的计数分布
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 加载本地titanic数据
titanic = sns.load_dataset("titanic")

# 画图
g = sns.catplot("alive", col="deck", col_wrap=4,
                data=titanic[titanic.deck.notnull()],
                kind="count", height=3.5, aspect=.8, 
                palette='tab20')

plt.Figure().suptitle('sf')
plt.show()