import matplotlib.pyplot as plt

x=[1,2,3,4,5,6,7,8,9]
y=[19,17,16,15,14,13,12,11,10]

plt.scatter(x,y,label='skitscat',color='k', marker='*', s=100)


plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()
