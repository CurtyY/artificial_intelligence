# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


data4 = pd.read_csv('avila-tr.csv')
data4.info()

correlacao=data4.corr().abs().unstack().sort_values(kind='quicksort')
sns.heatmap(data4.corr())
print(correlacao)