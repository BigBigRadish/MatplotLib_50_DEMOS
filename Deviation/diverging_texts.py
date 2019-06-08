# -*- coding: utf-8 -*-
'''
Created on 2019年1月14日 下午12:45:47
Zhukun Luo
Jiangxi University of Finance and Economics
'''
'''
发散型文本（Diverging Texts)与发散型条形图（Diverging Bars）相似，
如果你想以一种漂亮和可呈现的方式显示图表中每个项目的价值，就可以使用这种方法。
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# 数据预处理
df = pd.read_csv("https://github.com/selva86/datasets/raw/master/mtcars.csv")
x = df.loc[:, ['mpg']]
df['mpg_z'] = (x - x.mean())/x.std()
df['colors'] = ['red' if x < 0 else 'green' for x in df['mpg_z']]
df.sort_values('mpg_z', inplace=True)
df.reset_index(inplace=True)

# 绘制图例
plt.figure(figsize=(14,14), dpi= 80)
plt.hlines(y=df.index, xmin=0, xmax=df.mpg_z)#辅助线
for x, y, tex in zip(df.mpg_z, df.index, df.mpg_z):
    t = plt.text(x, y, round(tex, 2), horizontalalignment='right' if x < 0 else 'left', 
                 verticalalignment='center', fontdict={'color':'red' if x < 0 else 'green', 'size':14})

# 装饰   
plt.yticks(df.index, df.cars, fontsize=12)
plt.title('Diverging Text Bars of Car Mileage', fontdict={'size':20})
plt.grid(linestyle='--', alpha=0.5)#网格半透明
plt.xlim(-2.5, 2.5)#横坐标范围
plt.show()