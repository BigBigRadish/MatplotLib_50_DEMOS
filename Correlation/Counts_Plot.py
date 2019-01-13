# -*- coding: utf-8 -*-
'''
Created on 2019年1月13日 下午8:08:00
Zhukun Luo
Jiangxi University of Finance and Economics
'''
'''
渐近增大散点的形状防止重叠
'''
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Import Data
df = pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/mpg_ggplot2.csv")
df_counts = df.groupby(['hwy', 'cty']).size().reset_index(name='counts')#先分组聚合给每一组数据一个独立的大小

# Draw Stripplot
fig, ax = plt.subplots(figsize=(16,10), dpi= 80)    
sns.stripplot(df_counts.cty, df_counts.hwy, size=df_counts.counts*2, ax=ax)

# Decorations
plt.title('Counts Plot - Size of circle is bigger as more points overlap', fontsize=22)
plt.show()