import matplotlib.pyplot as plt
import numpy as np

#part 1
'''
import csv
x=[]
y=[]

with open('test.txt','r') as csvfile:
    plots=csv.reader(csvfile,delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.plot(x,y,label='Label from file')
'''
x,y=np.loadtxt('test.txt',delimiter=',',unpack=True)
plt.plot(x,y,label='Label from file')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()
