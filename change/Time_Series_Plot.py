# -*- coding: utf-8 -*-
'''
Created on 2019年1月19日 下午9:29:24
Zhukun Luo
Jiangxi University of Finance and Economics
'''
'''
时间序列图
时间序列图用于显示给定度量随时间变化的方式。 
下图表示1949年至1969年间航空客运量的变化情况。
'''
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
# 导入数据
df = pd.read_csv('https://github.com/selva86/datasets/raw/master/AirPassengers.csv')

# 画图
plt.figure(figsize=(16,10), dpi= 80)
plt.plot('date', 'traffic', data=df, color='tab:red')

# 坐标轴装饰
plt.ylim(50, 750)
xtick_location = df.index.tolist()[::12]
xtick_labels = [x[-4:] for x in df.date.tolist()[::12]]
plt.xticks(xtick_location, xtick_labels)
plt.yticks(fontsize=12, alpha=.7)
plt.title("Air Passengers Traffic (1949 - 1969)", fontsize=22)
plt.grid(axis='both', alpha=.3)

# Remove borders
plt.gca().spines["top"].set_alpha(0.0)    
plt.gca().spines["bottom"].set_alpha(0.3)
plt.gca().spines["right"].set_alpha(0.0)    
plt.gca().spines["left"].set_alpha(0.3)   
plt.show()