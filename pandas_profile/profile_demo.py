# -*- coding: utf-8 -*-
'''
Created on 2019年5月7日

@author: Zhukun Luo
Jiangxi university of finance and economics
'''
#pandas拓展库
import pandas_profiling
import pandas as pd
if __name__=='__main__':
    df=pd.read_csv('./train.csv')
    pfr=pandas_profiling.ProfileReport(df)
    pfr.to_file('report.html')