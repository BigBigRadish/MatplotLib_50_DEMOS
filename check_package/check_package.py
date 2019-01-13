# -*- coding: utf-8 -*-
'''
Created on 2019年1月13日
@author: agnostic
Jiangxi University of Finance and Economics
'''
#图表可以重新设置显示要素
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import warnings; warnings.filterwarnings(action='once')

large = 22; med = 16; small = 12
params = {'axes.titlesize': large,
          'legend.fontsize': med,
          'figure.figsize': (16, 10),
          'axes.labelsize': med,
          'axes.titlesize': med,
          'xtick.labelsize': med,
          'ytick.labelsize': med,
          'figure.titlesize': large}
plt.rcParams.update(params)
plt.style.use('seaborn-whitegrid')
sns.set_style("white")

# Version
print(mpl.__version__)#2.2.3
print(sns.__version__)#0.9.0 