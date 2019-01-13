# -*- coding: utf-8 -*-
'''
Created on 2019年1月13日 下午8:28:28
Zhukun Luo
Jiangxi University of Finance and Economics
'''
'''
在探索性分析中(EDA)，为了理解所有可能的数值变量对之间的关系，成对图是一种常用的方法。它是双变量分析的必备工具。
'''
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#加载数据集
df = sns.load_dataset('iris')

# 绘制成对图
plt.figure(figsize=(10,8), dpi= 80)
sns.pairplot(df, kind="scatter", hue="species", plot_kws=dict(s=80, edgecolor="white", linewidth=2.5))
plt.show()
