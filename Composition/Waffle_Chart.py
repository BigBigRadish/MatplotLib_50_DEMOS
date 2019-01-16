# -*- coding: utf-8 -*-
'''
Created on 2019年1月16日 下午5:20:03
Zhukun Luo
Jiangxi University of Finance and Economics
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from pywaffle import Waffle

# Import
df_raw = pd.read_csv("./mpg_ggplot2.csv")

# Prepare Data
df = df_raw.groupby('class').size().reset_index(name='counts')
n_categories = df.shape[0]
colors = [plt.cm.inferno_r(i/float(n_categories)) for i in range(n_categories)]

# Draw Plot and Decorate
fig = plt.figure(
    FigureClass=Waffle,
    plots={
        '111': {
            'values': df['counts'],
            'labels': ["{0} ({1})".format(n[0], n[1]) for n in df[['class', 'counts']].itertuples()],
            'legend': {'loc': 'upper left', 'bbox_to_anchor': (1.05, 1), 'fontsize': 12},
            'title': {'label': '# Vehicles by Class', 'loc': 'center', 'fontsize':18}
        },
    },
    rows=7,
    colors=colors,
    figsize=(16, 9)
)
plt.show()