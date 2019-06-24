import matplotlib.pyplot as plt;
import numpy as np;

colors = ['orange', 'brown', '#2ca02c', 'darkblue', 'y']

def color_graph():
    val_old=-1;
    for val in li[:]:
        if (val==val_old):
            continue;
        x_min_li = li.index(val);
        x_max_li = len(li) - 1 - li[::-1].index(val);
        plt.axvspan(x[x_min_li], x[x_max_li], facecolor=colors[val], alpha=0.4, lw=0)
        plt.grid(False, which='both', color='k', linestyle='-',alpha=0.4)
        val_old = val;

data = np.loadtxt('spatial.txt', skiprows=1);
q = 1.602E-19;

x = data[:,0]/1E-9; #in nm
xmin = min(x);
xmax = max(x);
G = data[:,1];
V = data[:,2];
E = data[:,3];
n = data[:,4];
p = data[:,5];
nt = data[:,6];
pt = data[:,7];
a = data[:,8];
#c = data[:,8];
E_c =data[:,9] / q; # in eV
E_v =data[:,10] / q;
E_fn =data[:,11] / q;
E_fp =data[:,12] / q;
Jn = data[:,13];
Jp = data[:,14];
J_disp = data[:,16];
li_float = data[:,17];
li = []
for i in li_float:
    li.append(int(i))
    
#SRH parameters
kB = 1.38E-23;
T = 300;
q = 1.602E-19;
Nc_layer = [2.5E25, 8E24, 2.5E25];
Nv_layer = [2.5E25, 8E24, 2.5E25];
Ec_layer = [-4, -3.9, -3.3];
Ev_layer = [-6, -5.4, -5.3];
Et_layer = [-5, -4.65, -4.3];
tau_n_layer = [1E-8, 1.8E-8, 1E-8];
tau_p_layer = [1E-8, 1.8E-8, 1E-8];
Nt_layer= [1E22, 1E21, 1E22];
tau_n = [];
tau_p = [];
Nt = [];
Cn = [];
Cp = [];
n1 = [];
p1 = [];
Nc = [];
Nv = [];
Ec = [];
Ev = [];
Et = [];

#for i in li:
#    tau_n = np.append(tau_n, tau_n_layer[i]);
#    tau_p = np.append(tau_p, tau_p_layer[i]);
#    Nt = np.append(Nt, Nt_layer[i]);
#    Nc = np.append(Nc, Nc_layer[i]);
#    Nv = np.append(Nv, Nv_layer[i]);
#    Ec = np.append(Ec, Ec_layer[i]);
#    Ev = np.append(Ev, Ev_layer[i]);
#    Et = np.append(Et, Et_layer[i]);
#
#Cn = 1/(tau_n*Nt);
#Cp = 1/(tau_p*Nt);
#n1 = Nc*np.exp(-q*(Ec-Et)/(kB*T));
#p1 = Nv*np.exp(-q*(Et-Ev)/(kB*T));
#
#SRH_steady = ( (Cn*Cp*Nt) / (Cn*(n+n1) + Cp*(p+p1)) ) * ((n * p)-(n1*p1));
#SRH_n = (1 / (tau_n*Nt))*(n*Nt - nt*(n + n1));
#SRH_p = (1 / (tau_p*Nt))*(nt*(p + p1) - p1*Nt);

# Plot all results
plt.figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k');

# Generation
plt.subplot(321)
axes = plt.gca()
axes.set_xlim([xmin,xmax])
plt.plot(x, G, 'k-', mfc='none')
plt.yscale('linear')
plt.title('Generation profile')
plt.xlabel('Position [nm]')
plt.ylabel('G $[m^{-3}]$')
color_graph();

# Electric field
plt.subplot(322)
axes = plt.gca()
axes.set_xlim([xmin,xmax])
plt.plot(x, E, 'k-', mfc='none')
plt.yscale('linear')
plt.title('Electric field')
plt.xlabel('Position [nm]')
plt.ylabel('F $[V m^{-1}]$')
plt.ticklabel_format(axis='y',style='sci',scilimits=(1,4))
color_graph();

# Charge concentration
plt.subplot(323)
plt.title('Charge concentration')
color_graph();
ax1 = plt.gca()
ax1.set_xlim([xmin,xmax])
ax1.plot(x, n, 'k-', mfc='none')
ax1.set_yscale('log')
ax1.set_ylabel('n $[m^{-3}]$')
ax1.set_xlabel('Position [nm]')
ax2 = ax1.twinx()
ax2.plot(x, p, 'r-', mfc='none')
ax2.set_ylabel('p $[m^{-3}]$', color='r')
for label in ax2.get_yticklabels():
    label.set_color("r")
ax2.set_yscale('log')

# Trapped charge concentration
plt.subplot(324)
plt.title('Traps')
color_graph();
ax1 = plt.gca()
ax1.set_xlim([xmin,xmax])
ax1.plot(x, nt, 'k-', x, pt, 'r-', mfc='none')
ax1.set_yscale('log')
ax1.set_ylabel('n$_t$ $[m^{-3}]$')
ax1.set_xlabel('Position [nm]')
ax2 = ax1.twinx()
#ax2.plot(x, SRH_steady, 'r-', x, SRH_n, 'w--', x, SRH_p, 'g--', mfc='none')
ax2.set_ylabel('R $m^3 s^{-1}$', color='r')
for label in ax2.get_yticklabels():
    label.set_color("r")
ax2.set_yscale('log')

# Current density
plt.subplot(325)
plt.title('Current density')
color_graph();
ax1 = plt.gca()
ax1.set_xlim([xmin,xmax])
ax1.plot(x, Jn, 'k-', mfc='none')
ax1.set_yscale('linear')
ax1.set_ylabel('J$_n$ $[A m^{-2}]$')
ax1.set_xlabel('Position [nm]')
ax2 = ax1.twinx()
ax2.plot(x, Jp, 'r-', mfc='none')
ax2.set_ylabel('J$_p$ $[A m^{-2}]$', color='r')
for label in ax2.get_yticklabels():
    label.set_color("r")
ax2.set_yscale('linear')

# Energy
plt.subplot(326)
axes = plt.gca()
axes.set_xlim([xmin,xmax])
plt.plot(x, E_c, 'k-', x, E_v, 'r-', x, E_fn, 'k--', x, E_fp, 'r--', mfc='none')
plt.yscale('linear')
plt.title('Energy')
plt.xlabel('Position [nm]')
plt.ylabel('E $[eV]$')
color_graph();

# SRH recombinatio
#plt.subplot(326)
#axes = plt.gca()
#axes.set_xlim([xmin,xmax])
#plt.plot(x, Rmn, 'k-s', x, Rmp, 'r-o', x, R_SRH, 'w--', mfc='none')
#plt.yscale('log')
#plt.title('SRH recombination')
#plt.grid(True)
#color_graph();
# Charge concentration
#plt.subplot(326)
#plt.plot(x, a, 'k-o', x, c, 'r-o', mfc='none')
#plt.yscale('log')
#plt.title('Charge concentration')
#plt.grid(True)

plt.tight_layout();
plt.show();