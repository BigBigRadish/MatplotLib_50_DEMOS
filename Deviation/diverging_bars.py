# -*- coding: utf-8 -*-
'''
Created on 2019年1月14日 下午12:15:32
Zhukun Luo
Jiangxi University of Finance and Economics
'''
'''
发散型条形图
如果想根据单个指标查看项目的变化情况，并可视化此差异的顺序和数量，那么发散型条形图 （Diverging Bars）是一个很好的工具。
它有助于快速区分数据中组的性能，并且非常直观，并且可以立即传达这一点。
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# 数据预处理
df = pd.read_csv("https://github.com/selva86/datasets/raw/master/mtcars.csv")
x = df.loc[:, ['mpg']]
df['mpg_z'] = (x - x.mean())/x.std()#z-score
df['colors'] = ['red' if x < 0 else 'green' for x in df['mpg_z']]
df.sort_values('mpg_z', inplace=True)
df.reset_index(inplace=True)

# 绘制主图
plt.figure(figsize=(14,10), dpi= 80)
plt.hlines(y=df.index, xmin=0, xmax=df.mpg_z, color=df.colors, alpha=0.4, linewidth=5)

# 装饰
plt.gca().set(ylabel='$Model$', xlabel='$Mileage$')
plt.yticks(df.index, df.cars, fontsize=12)
plt.title('Diverging Bars of Car Mileage', fontdict={'size':20})
plt.grid(linestyle='--', alpha=0.5)
plt.show()