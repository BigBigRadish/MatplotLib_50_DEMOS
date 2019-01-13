# -*- coding: utf-8 -*-
'''
Created on 2019年1月13日 下午7:11:40
Zhukun Luo
Jiangxi University of Finance and Economics
'''
'''
每列中显示每个组的最佳拟合线。可以通过在sns.lmplot()中设置col=groupingcolumn参数来实现
'''
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# 导入数据
df = pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/mpg_ggplot2.csv")
df_select = df.loc[df.cyl.isin([4,8]), :]

# Each line in its own column
sns.set_style("white")
gridobj = sns.lmplot(x="displ", y="hwy", 
                     data=df_select, 
                     height=7, 
                     robust=True, 
                     palette='Set1', 
                     col="cyl",
                     scatter_kws=dict(s=60, linewidths=.7, edgecolors='black'))

# Decorations
gridobj.set(xlim=(0.5, 7.5), ylim=(0, 50))
plt.show()