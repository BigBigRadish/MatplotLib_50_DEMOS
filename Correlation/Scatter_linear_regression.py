# -*- coding: utf-8 -*-
'''
Created on 2019年1月13日 下午6:15:50
Zhukun Luo
Jiangxi University of Finance and Economics
'''
'''
两个变量如何相互改变，那么最佳拟合线就是常用的方法。
下图显示了数据中各组之间最佳拟合线的差异。
要禁用分组并仅为整个数据集绘制一条最佳拟合线，
下面的sns.lmplot（）调用中删除hue='cyl'参数
'''
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Import Data
df = pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/mpg_ggplot2.csv")
df_select = df.loc[df.cyl.isin([4,8]), :]

# Plot
sns.set_style("white")
gridobj = sns.lmplot(x="displ", y="hwy", hue="cyl", data=df_select, 
                     height=7, aspect=1.6, robust=True, palette='tab10', 
                     scatter_kws=dict(s=60, linewidths=.7, edgecolors='black'))

# Decorations
gridobj.set(xlim=(0.5, 7.5), ylim=(0, 50))
plt.title("Scatterplot with line of best fit grouped by number of cylinders", fontsize=20)
plt.show()