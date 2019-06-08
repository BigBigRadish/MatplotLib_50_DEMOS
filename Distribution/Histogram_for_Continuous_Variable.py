# -*- coding: utf-8 -*-
'''
Created on 2019年1月15日 下午12:12:41
Zhukun Luo
Jiangxi University of Finance and Economics
'''
'''
连续变量的直方图 
直方图显示给定变量的频率分布。下面的图表示基于类型变量对频率条进行分组，从而更好地了解连续变量和类型变量
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Import Data
df = pd.read_csv("https://github.com/selva86/datasets/raw/master/mpg_ggplot2.csv")

# Prepare data
x_var = 'displ'
groupby_var = 'class'
df_agg = df.loc[:, [x_var, groupby_var]].groupby(groupby_var)
vals = [df[x_var].values.tolist() for i, df in df_agg]
print(vals)
# Draw
plt.figure(figsize=(16,9), dpi= 80)
colors = [plt.cm.Spectral(i/float(len(vals)-1)) for i in range(len(vals))]
n, bins, patches = plt.hist(vals, 30, stacked=True, density=False, color=colors[:len(vals)])
print(bins)
'''
hist的参数非常多，但常用的就这六个，只有第一个是必须的，后面四个可选
arr: 需要计算直方图的一维数组
bins: 直方图的柱数，可选项，默认为10
normed: 是否将得到的直方图向量归一化。默认为0
facecolor: 直方图颜色
edgecolor: 直方图边框颜色
alpha: 透明度
histtype: 直方图类型，‘bar’, ‘barstacked’, ‘step’, ‘stepfilled’
返回值 ：
n: 直方图向量，是否归一化由参数normed设定
bins: 返回各个bin的区间范围
patches: 返回每个bin里面包含的数据，是一个list
'''

# 装饰
plt.legend({group:col for group, col in zip(np.unique(df[groupby_var]).tolist(), colors[:len(vals)])})
# plt.show()
plt.title("Stacked Histogram of ${x_var}$ colored by ${groupby_var}$", fontsize=22)
plt.xlabel(x_var)
plt.ylabel("Frequency")
plt.ylim(0, 25)
# plt.xticks(locs=bins[::3],labels=[round(b,1) for b in bins[::3]])
'''
plt.xticks()
第一个参数接受坐标，第二个参数接受，各坐标显示的文本，关键字参数，如 rotation，表示文本显示时旋转的角度，为了达到一种美观的效果。
'''
plt.show()