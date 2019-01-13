# -*- coding: utf-8 -*-
'''
Created on 2018年12月11日 下午4:55:41
Zhukun Luo
Jiangxi University of Finance and Economics
'''
'''
相关性热点图
'''
import numpy as np
import pandas as pd
import matplotlib as mlp
import matplotlib.pyplot as plt
import seaborn as sns
import warnings; warnings.filterwarnings(action='once')

# 导入数据集
df = pd.read_csv("https://github.com/selva86/datasets/raw/master/mtcars.csv")

# 绘制热点图
plt.figure(figsize=(12,10), dpi= 80)
sns.heatmap(df.corr(), xticklabels=df.corr().columns, yticklabels=df.corr().columns, cmap='RdYlGn', center=0, annot=True)
#组装
plt.title('Correlogram of mtcars', fontsize=22)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()