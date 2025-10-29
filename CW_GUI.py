#===================================================
import matplotlib.pyplot as plt #this package works with plots, graph, pie charts
import numpy as np #this package also works with the matplotlib framework
#===================================================

x = np.array(["c1", "c2", "c3", "c4"])
y = np.array([100, 75, 1, 50])

print(np.mean(y))
print(np.median(y))
print(np.std(y))

plt.xlabel("Courses")
plt.ylabel("grades")

#line chart
plt.plot(x,y)
plt.show() #plt.show() basically prints out the graph/type of graph being given

#pie chart
mylabels = ["a1", "a2", "a3", "a4"]
plt.pie(y, labels=mylabels)
plt.show()

x = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]

plt.plot(x,y)
plt.show()

plt.pie(x, labels=x)
plt.show()

plt.pie(y, labels=y)
plt.show()

plt.scatter(x,y)
plt.show()