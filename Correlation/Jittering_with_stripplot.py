# -*- coding: utf-8 -*-
'''
Created on 2019年1月13日 下午7:39:28
Zhukun Luo
Jiangxi University of Finance and Economics
'''
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#使用stripplot防止数据重叠，进行抖动操作
# 导入数据
df = pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/mpg_ggplot2.csv")

# Draw Stripplot
fig, ax = plt.subplots(figsize=(16,10), dpi= 80)    
sns.stripplot(df.cty, df.hwy, jitter=0.25, size=8, ax=ax, linewidth=.5)

# 进行装饰
plt.title('Use jittered plots to avoid overlapping of points', fontsize=22)
plt.show()