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
s = data[:,6];
E_c =data[:,7] / q; # in eV
E_v =data[:,8] / q;
E_fn =data[:,9] / q;
E_fp =data[:,10] / q;
Jn = data[:,11];
Jp = data[:,12];
J_disp = data[:,13];
li_float = data[:,14];
li = []
for i in li_float:
    li.append(int(i))


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

# Exciton concentration
plt.subplot(324)
plt.title('Excitons')
color_graph();
ax1 = plt.gca()
ax1.set_xlim([xmin,xmax])
ax1.plot(x, s, 'k-', mfc='none')
ax1.set_yscale('linear')
ax1.set_ylabel('s $[m^{-3}]$')
ax1.set_xlabel('Position [nm]')

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