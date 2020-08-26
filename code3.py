import matplotlib.pyplot as plt
from drsr import tt
dtt=tt
from arsr2 import tt
a2tt=tt
from arsr import tt
att=tt

import numpy as np

alg=['DIJKSTRA','A*(Mn)','A*(Eu)']
tt =[dtt, a2tt, att]
ypos = np.arange(len(alg))
plt.xticks(ypos,alg)
plt.ylabel("Time(s)")
plt.xlabel("Dijkstra vs A*")
plt.title("Comparison Results")
l=plt.bar(ypos,tt)
l[0].set_color('r')
l[2].set_color('g')
plt.legend()
plt.show()