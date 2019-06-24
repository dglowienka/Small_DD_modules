import matplotlib.pyplot as plt;
import numpy as np;
import math

data = np.loadtxt('spatial.txt', skiprows=1);

x = data[:,0];
V = data[:,1];
E = data[:,2];
n = data[:,3];
p = data[:,4];
s = data[:,5];
NA = data[:,6];
NC = data[:,7];
Jn = data[:,8];
Jp = data[:,9];
J_NA = data[:,10];
J_NC = data[:,11];
J_disp = data[:,12];

q = 1.602E-19;
k_B = 1.38E-23;
T = 293;
C_n = 1E-14;
C_p = 1E-14;
N_t = 1E21;
N_c = 1E27;
N_v = 1E27;
E_c = 3.9*q;
E_v = -5.4*q;
E_t = 0.15*q;
n1 = N_c*math.exp((E_t-E_c) / (k_B*T));
p1 = N_v*math.exp((E_v - E_t) / (k_B*T));
k1 = ((C_n*C_p*N_t) / (C_n*(n+n1) + C_p*(p+p1))) * n*p;
test = n*p/(n+p);

plt.figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k');
# k1
plt.plot(x, k1)
plt.yscale('log')
plt.title('k1')
plt.grid(True)