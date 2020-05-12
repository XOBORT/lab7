# -*- coding: utf-8 -*-
import pylab
import numpy as np
import matplotlib.pyplot as plt
pylab.minorticks_on()
pylab.grid(color="black", which="major", linewidth=1)
pylab.grid(color="k", which="minor", linestyle=":", linewidth=0.5)
data=np.loadtxt ("ans1.dat")
plt.plot(data[:,1], data[:,2],color= 'b')
plt.title(" y'(y) ")
plt.ylabel("y(x)")
plt.xlabel("x")

pylab.show()
