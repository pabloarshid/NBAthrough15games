import numpy as np
import pandas as pd
import glob
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

l = [pd.read_csv(filename, header = 0,parse_dates=['Date']) for filename in glob.glob("/mnt/c/Users/umar_/Documents/Projects/Data/NBA/Through 15 games/*.csv")]
means = [ ]

for df in l:
    df['Year'] = df.Date.dt.year
    temp = df[df["G"] < 16]
    year = temp.Date.dt.year.unique()
    temp2 = temp[["PTS", "AST", "TRB", "STL", "BLK", "TOV", "Year"]].mean(axis=0)
    means.append(temp2)
    
meansdf = pd.DataFrame(means)
meansdf["Year"] = meansdf.Year.astype(int)
meansdf = meansdf.set_index('Year')
