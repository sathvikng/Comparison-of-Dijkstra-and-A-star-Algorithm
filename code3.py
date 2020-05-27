import matplotlib.pyplot as plt
from dijkstr import tt
dtt=tt
from astr import tt
att=tt
import numpy as np

alg=['DIJKSTRA','A*']
tt =[dtt, att]
ypos = np.arange(len(alg))
plt.xticks(ypos,alg)
plt.ylabel("Time(s)")
plt.xlabel("Dijkstra vs A*")
plt.title("DAA TEAM 5")
l=plt.bar(ypos,tt)
l[0].set_color('r')
plt.legend()
plt.show()



