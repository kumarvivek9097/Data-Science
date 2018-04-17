import matplotlib.pyplot as plt
import numpy as np
import urllib
import matplotlib.dates as mdates

def graph_data(stock):
    stock_price_url='https://pythonprogramming.net/yahoo_finance_replacement'
    source_code=urllib.urlopen(stock_price_url).read().decode()
    stock_data=[]
    split_source=source_code.split('\n')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Interesting Graph\nCheck it out')
    plt.legend()
    plt.show()

graph_data('TSLA')
