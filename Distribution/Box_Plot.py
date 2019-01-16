# -*- coding: utf-8 -*-
'''
Created on 2019年1月16日 下午4:43:35
Zhukun Luo
Jiangxi University of Finance and Economics
'''
'''
箱形图
箱形图是一种可视化分布的好方法，记住中位数、第25个第45个四分位数和异常值。 
但是，您需要注意解释可能会扭曲该组中包含的点数的框的大小。
因此，手动提供每个框中的观察数量可以帮助克服这个缺点
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# 导入数据
df = pd.read_csv("https://github.com/selva86/datasets/raw/master/mpg_ggplot2.csv")

# 画图
plt.figure(figsize=(13,10), dpi= 80)
sns.boxplot(x='class', y='hwy', data=df, notch=False)

# 将n个对象添加到箱盒图里面
def add_n_obs(df,group_col,y):
    medians_dict = {grp[0]:grp[1][y].median() for grp in df.groupby(group_col)}
    xticklabels = [x.get_text() for x in plt.gca().get_xticklabels()]
    n_obs = df.groupby(group_col)[y].size().values
    for (x, xticklabel), n_ob in zip(enumerate(xticklabels), n_obs):
        plt.text(x, medians_dict[xticklabel]*1.01, "#obs : "+str(n_ob), horizontalalignment='center', fontdict={'size':14}, color='white')

add_n_obs(df,group_col='class',y='hwy')    

# 装饰
plt.title('Box Plot of Highway Mileage by Vehicle Class', fontsize=22)
plt.ylim(10, 40)
plt.show()
