import matplotlib.pyplot as plt;
import numpy as np;


data = np.loadtxt('jV_steady.dat', skiprows=1);
ref = np.loadtxt('G0610_cell3/1suns.dat', skiprows=3);

V_steady = data[:,0];
J_steady = data[:,1];
V_ref = ref[:,0];
J_ref = ref[:,1]*(-10);

V_steady += 0.0;
J_steady += 0;

# Plot all results
plt.figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k');

# jV steady
plt.axis((-0.1,1.4,-210,0));
plt.plot(V_steady, J_steady, 'k-');
plt.scatter(V_ref, J_ref, s=50, color='orange');

plt.yscale('linear');
plt.title('Fitting');
plt.grid(True);

