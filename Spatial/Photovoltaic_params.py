import sys;
import numpy as np;

script = sys.argv[0]
filename = sys.argv[1]

data = np.loadtxt(filename, skiprows=1);
P_in = 1000;
V = data[:,0];
J = data[:,1];
P = J*V;

V_m = V[np.argmin(P)];
J_m = J[np.argmin(P)];
P_m = V_m*J_m;

J_sc = np.interp(0, V, J);
V_oc = np.interp(0, J, V);

FF = (V_m*J_m) / (V_oc*J_sc);
Eff = np.absolute(P_m) / (1000);

NAMES  = np.array(['Jsc \t', 'Voc \t', 'FF \t', 'Efficiency']);
FLOATS = np.array([ J_sc ,  V_oc ,  FF ,  Eff ]);

DAT =  np.vstack((NAMES, FLOATS));
np.savetxt('PV_steady.dat', DAT, delimiter=" ", fmt="%s");
