import matplotlib.pyplot as plt

population_ages=[22,55,62,21,22,34,42,43,99,102,12,120,122,130,111,115,80,45,56,32]

#ids=[x for x in range(len(population_ages))]
bins=[0,10,20,30,40,50,60,70,80,90,100,110,120,130]
plt.hist(population_ages,bins,histtype='bar',rwidth=0.8)


plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()
