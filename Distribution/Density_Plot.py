# -*- coding: utf-8 -*-
'''
Created on 2019年1月16日 下午2:15:44
Zhukun Luo
Jiangxi University of Finance and Economics
'''
'''
密度图
密度图是一种常用工具，用于可视化连续变量的分布。 
通过“响应”变量对它们进行分组，您可以检查 X 和 Y 之间的关系。
以下情况用于表示目的，以描述城市里程的分布如何随着汽缸数的变化而变化。
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# 导入数据
df = pd.read_csv("https://github.com/selva86/datasets/raw/master/mpg_ggplot2.csv")

# 画图
plt.figure(figsize=(16,10), dpi= 80)
sns.kdeplot(df.loc[df['cyl'] == 4, "cty"], shade=True, color="g", label="Cyl=4", alpha=.7)
'''
kdeplot(核密度估计图)
核密度估计(kernel density estimation)是在概率论中用来估计未知的密度函数，属于非参数检验方法之一。
通过核密度估计图可以比较直观的看出数据样本本身的分布特征。具体用法如下：
绘制简单的一维kde图像:x=np.random.randn(100)  #随机生成100个符合正态分布的数sns.kdeplot(x)
cut：参数表示绘制的时候，切除带宽往数轴极限数值的多少(默认为3):sns.kdeplot(x,cut=0)
cumulative ：是否绘制累积分布
shade：若为True，则在kde曲线下面的区域中进行阴影处理，color控制曲线及阴影的颜色
vertical：表示以X轴进行绘制还是以Y轴进行绘制
cbar：参数若为True，则会添加一个颜色棒(颜色帮在二元kde图像中才有)


'''
sns.kdeplot(df.loc[df['cyl'] == 5, "cty"], shade=True, color="deeppink", label="Cyl=5", alpha=.7)
sns.kdeplot(df.loc[df['cyl'] == 6, "cty"], shade=True, color="dodgerblue", label="Cyl=6", alpha=.7)
sns.kdeplot(df.loc[df['cyl'] == 8, "cty"], shade=True, color="orange", label="Cyl=8", alpha=.7)

# 装饰坐标轴及标题
plt.title('Density Plot of City Mileage by n_Cylinders', fontsize=22)
plt.legend()
plt.show()