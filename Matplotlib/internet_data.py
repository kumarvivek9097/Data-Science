import matplotlib.pyplot as plt
import numpy as np
import urllib
import matplotlib.dates as mdates
from datetime import datetime

def bytespdate2num(fmt,encoding='utf-8'):
    strconverter=mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s=b.decode(encoding)
        return strconverter
    return bytesconverter

def graph_data(stock):
    fig=plt.figure()
    ax1=plt.subplot2grid((1,1),(0,0))



    
    stock_price_url='https://pythonprogramming.net/yahoo_finance_replacement'
    source_code=urllib.urlopen(stock_price_url).read().decode()
    stock_data=[]
    split_source=source_code.split('\n')

    for line in split_source[1:]:
        split_line=line.split(',')
        if len(split_line)==7:
            if 'values' not in line:
                stock_data.append(line)
    date,openp,highp,lowp,closep,adjusted_closep,volume=np.loadtxt(stock_data,
                                                    delimiter=',',
                                                    unpack=True,dtype=object,
                                                    converters={0: lambda x: datetime.strptime(x,'%Y-%m-%d')})




    
    ax1.plot_date(date,closep,'-',label='Price')
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
    plt.xlabel('date')
    plt.ylabel('price')
    plt.title('Interesting Graph\nCheck it out')
    plt.legend()
    plt.subplots_adjust(left=0.09,bottom=0.18,right=0.94,wspace=0.2,hspace=0)
    plt.show()

graph_data('TSLA')
