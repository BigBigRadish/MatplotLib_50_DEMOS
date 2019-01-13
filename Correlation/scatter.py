# -*- coding: utf-8 -*-
'''
Created on 2019年1月13日
@author: agnostic

'''
import numpy as np
import pandas as pd
import matplotlib as mlp
import matplotlib.pyplot as plt
import seaborn as sns
import warnings; warnings.filterwarnings(action='once')
from scipy.interpolate.interpolate import spltopp
'''
散点图是用于研究两个变量之间关系的经典的和基本的图表。
如果数据中有多个组，则可能需要以不同颜色可视化每个组。
在 matplotlib 中，可以使用plt.scatterplot（）方便地执行此操作。
'''
large = 22; med = 16; small = 12
params = {'axes.titlesize': large,
          'legend.fontsize': med,
          'figure.figsize': (16, 10),
          'axes.labelsize': med,
          'axes.titlesize': med,
          'xtick.labelsize': med,
          'ytick.labelsize': med,
          'figure.titlesize': large}
plt.rcParams.update(params)
plt.style.use('seaborn-whitegrid')
sns.set_style("white")
# 导入数据集
midwest = pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/midwest_filter.csv")

# 准备数据
# 创建和预测类别一样多的颜色
categories = np.unique(midwest['category'])
colors = [plt.cm.tab10(i/float(len(categories)-1)) for i in range(len(categories))]#


plt.figure(figsize=(16, 10), dpi= 80, facecolor='w', edgecolor='k')# 绘制整个图表
# plt.show()
for i, category in enumerate(categories):
    plt.scatter('area', 'poptotal', 
                data=midwest.loc[midwest.category==category, :], 
                s=20, c=colors[i], label=str(category))
# plt.show()
# 装饰，设置图例
plt.gca().set(xlim=(0.0, 0.1), ylim=(0, 90000),
              xlabel='Area', ylabel='Population')#通过plt.gca()获得当前的Axes对象ax
# plt.show()
plt.xticks(fontsize=12); plt.yticks(fontsize=12)
plt.title("Scatterplot of Midwest Area vs Population", fontsize=22)
plt.legend(fontsize=12)    
plt.show()    