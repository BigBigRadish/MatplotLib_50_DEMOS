# -*- coding: utf-8 -*-
'''
Created on 2019年1月17日 下午9:47:13
Zhukun Luo
Jiangxi University of Finance and Economics
'''
'''
饼图
饼图是显示组成的经典方式。 然而，现在通常不建议使用它，因为馅饼部分的面积有时会变得误导
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 导入数据
df_raw = pd.read_csv("./mpg_ggplot2.csv")

# 分组
df = df_raw.groupby('class').size()

# 用pandas进行绘制
df.plot(kind='pie', subplots=True, figsize=(8, 8))
plt.title("Pie Chart of Vehicle Class - Bad")
plt.ylabel("")
plt.show()