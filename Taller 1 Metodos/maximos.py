import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.signal import argrelextrema

def crear_df():
    df=pd.read_csv('EstrellaEspectro.txt',sep='  ',names=['x','y'],engine='python')
    return df

def main():
    df=crear_df()
    n=1
    df['max'] = df.iloc[argrelextrema(df.y.values, np.greater_equal,order=n)[0]]['y']

    plt.scatter(df['x'], df['max'], c='r',s=7)
    plt.plot(df['x'], df['y'])
    plt.show()
    
main()