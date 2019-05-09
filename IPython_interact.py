import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from IPython.html.widgets import interact
%matplotlib inline
df = sns.load_dataset('planets')
def plot_data(method='Imaging',x='orbital_period',y='mass',z='year',size=10,cmap='Blues'):
    global df 
    df = df[df['method'] == method]
    dfx, dfy, dfz= df[x], df[y], df[z]
    
    bubbles = (dfx - dfx.min()) / (dfx.max() - dfx.min())
    sc = plt.scatter(dfx, dfy, s=size * bubbles + 9, cmap=cmap)
    plt.title('statistic')

    
var = df.columns.tolist()
cmaps = [cmap for cmap in plt.cm.datad if  not cmap.endswith("_r")]
cmaps.sort()
interact(plot_data,x=var,y=var,size=(100,700),cmap=cmaps)
