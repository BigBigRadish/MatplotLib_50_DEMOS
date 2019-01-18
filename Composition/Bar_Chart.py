# -*- coding: utf-8 -*-
'''
Created on 2019年1月18日 下午8:33:22
Zhukun Luo
Jiangxi University of Finance and Economics
'''
'''
条形图
条形图是基于计数或任何给定指标可视化项目的经典方式
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import random

# 导入数据
df_raw = pd.read_csv("./mpg_ggplot2.csv")

# 处理数据
df = df_raw.groupby('manufacturer').size().reset_index(name='counts')
n = df['manufacturer'].unique().__len__()+1
all_colors = list(plt.cm.colors.cnames.keys())
random.seed(100)
c = random.choice(all_colors)#choice() 方法返回一个列表，元组或字符串的随机项。

# 条形绘制
plt.figure(figsize=(16,10), dpi= 80)
plt.bar(df['manufacturer'], df['counts'], color=c, width=.5)
for i, val in enumerate(df['counts'].values):
    plt.text(i, val, float(val), horizontalalignment='center', verticalalignment='bottom', fontdict={'fontweight':500, 'size':12})

# 装饰坐标区域
plt.gca().set_xticklabels(df['manufacturer'], rotation=60, horizontalalignment= 'right')
plt.title("Number of Vehicles by Manaufacturers", fontsize=22)
plt.ylabel('# Vehicles')
plt.ylim(0, 45)
plt.show()