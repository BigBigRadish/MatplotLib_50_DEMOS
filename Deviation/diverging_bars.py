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
df.reset_index(inplace=True)#重新规整索引

# 绘制主图
plt.figure(figsize=(14,10), dpi= 80)
plt.hlines(y=df.index, xmin=0, xmax=df.mpg_z, color=df.colors, alpha=0.4, linewidth=5)#行水平线

# 装饰
plt.gca().set(ylabel='$Model$', xlabel='$Mileage$')
plt.yticks(df.index, df.cars, fontsize=12)
plt.title('Diverging Bars of Car Mileage', fontdict={'size':20})
plt.grid(linestyle='--', alpha=0.5)
'''
matplotlin.pyplot.grid(b, which, axis, color, linestyle, linewidth， **kwargs)
b : 布尔值。就是是否显示网格线的意思。官网说如果b设置为None， 且kwargs长度为0，则切换网格状态。但是没弄明白什么意思。如果b设置为None，但是又给了其它参数，则默认None值失效。

    which : 取值为'major', 'minor'， 'both'。 默认为'major'。看别人说是显示的我的是Windows7下，用Sublime跑的，minor只是一个白画板，没有网格，major和both也没看出什么效果，不知道为什么。

    axis : 取值为‘both’， ‘x’，‘y’。就是想绘制哪个方向的网格线。不过我在输入参数的时候发现如果输入x或y的时候,输入的是哪条轴，则会隐藏哪条轴

    color : 这就不用多说了，就是设置网格线的颜色。或者直接用c来代替color也可以。

    linestyle :也可以用ls来代替linestyle， 设置网格线的风格，是连续实线，虚线或者其它不同的线条。 | '-' | '--'                        | '-.' | ':' | 'None' | ' ' | '']

    linewidth : 设置网格线的宽度
'''
plt.show()