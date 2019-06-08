# -*- coding: utf-8 -*-
'''
Created on 2019年1月18日 下午8:24:36
Zhukun Luo
Jiangxi University of Finance and Economics
'''
'''
树形图类似于饼图，它可以更好地完成工作而不会误导每个组的贡献
'''
# pip install squarify
import squarify 
import pandas as pd
import matplotlib.pyplot as plt

# 导入数据
df_raw = pd.read_csv("./mpg_ggplot2.csv")

# 处理数据
df = df_raw.groupby('class').size().reset_index(name='counts')
labels = df.apply(lambda x: str(x[0]) + "\n (" + str(x[1]) + ")", axis=1)
sizes = df['counts'].values.tolist()
colors = [plt.cm.Spectral(i/float(len(labels))) for i in range(len(labels))]

# 绘图
plt.figure(figsize=(12,8), dpi= 80)
squarify.plot(sizes=sizes, label=labels, color=colors, alpha=.8)

# 装饰
plt.title('Treemap of Vechile Class')
plt.axis('off')#隐藏坐标轴
plt.show()
