# -*- coding: utf-8 -*-
'''
Created on 2019年1月16日 下午3:30:53
Zhukun Luo
Jiangxi University of Finance and Economics
'''
'''
Joy Plot允许不同组的密度曲线重叠，这是一种可视化大量分组数据的彼此关系分布的好方法。 
它看起来很悦目，并清楚地传达了正确的信息。
它可以使用基于 matplotlib 的 joypy 包轻松构建。
'''
import joypy.joyplot as jlt
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

# 导入数据
mpg = pd.read_csv("https://github.com/selva86/datasets/raw/master/mpg_ggplot2.csv")

# 画图
plt.figure(figsize=(16,10), dpi= 80)
fig, axes = jlt(mpg, column=['hwy', 'cty'], by="class", ylim='own', figsize=(14,10))

# 装饰
plt.title('Joy Plot of City and Highway Mileage by Class', fontsize=22)
plt.show()