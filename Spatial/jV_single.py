import matplotlib.pyplot as plt;
import numpy as np;
import sys

file_name = sys.argv[-1]

data = np.loadtxt(file_name, skiprows=1);

V = data[:,0];
J = data[:,1];

# Plot all results
plt.figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k');

# jV steady
plt.axis((-0.1,1.1,-210,150));
plt.plot(V, J, 'k-');

plt.yscale('linear');
plt.title('Fitting');
plt.grid(True);
plt.show(block=True);

