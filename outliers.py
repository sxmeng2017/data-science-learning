import statsmodels.api as sm
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def filter_outliers(a):
    b = a.copy()
    std = np.std(b)
    mean = np.mean(b)
    level = 3
    bmax, bmin = std + level * mean, std - level * mean
    b[bmin > b] = np.nan
    b[bmax < b] = np.nan
    return b

def winsorize(a ,p):
    b = a.copy()
    bmin, bmax = np.percentile(b, p) , np.percentile(b, 100 - p)
    b[b < bmin], b[b > bmax] = bmin, bmax
    return b


def trunc(a ,p):
    b = a.copy()
    bmin, bmax = np.percentile(b, p) , np.percentile(b, 100 - p)
    b[b < bmin], b[b > bmax] = np.nan, np.nan
    return b.dropna()



