import sys;
import numpy as np;


script = sys.argv[0]
filename = sys.argv[1]

#filename = 'DG180714_G061_1cell_at1_fast_2LS_01.dat'
fileoutput = filename.replace(".", "_PV.")
#data = np.loadtxt(filename, skiprows=0);
data = np.genfromtxt(filename, skip_footer=3)
P_in = 1000;
cell_scale = [1, 1.03167068593155, 1.11362635968994, 1.0985241970956]

f=open(fileoutput,'a')
NAMES  = np.array(['Eff', 'Voc', 'Jsc', 'FF']);
cell_no = 0
while cell_no < 4:
    f.write("Filename %s\r\n" % (filename))
    # Get data for specific cell
    V_cell = data[:,cell_no*2];
    V_cell = np.asarray(np.split(V_cell, 2)).transpose()
    J_cell = cell_scale[cell_no]*data[:,cell_no*2+1]*-10;
    J_cell = np.asarray(np.split(J_cell, 2)).transpose()
    
    #REVERSED scan
    V_rev = V_cell[:,0]
    J_rev = J_cell[:,0]
    P_rev = J_rev*V_rev
    Vm_rev = V_rev[np.argmin(P_rev)];
    Jm_rev = J_rev[np.argmin(P_rev)];
    Jsc_rev = np.interp(0, V_rev[::-1], J_rev[::-1]); #Inverted for interpolation only
    Voc_rev = np.interp(0, J_rev[::-1], V_rev[::-1]); #Inverted for interpolation only
    FF_rev = (Vm_rev*Jm_rev) / (Voc_rev*Jsc_rev);
    Eff_rev = np.absolute(Jsc_rev*Voc_rev*FF_rev) / (P_in);
    FLOATS_rev = np.array([ Eff_rev ,  Voc_rev ,  Jsc_rev ,  FF_rev ]);
    DAT_rev =  np.vstack((NAMES, FLOATS_rev));
    f.write("Cell no %d for REVERSED scan \r\n" % (cell_no+1))
    np.savetxt(f, DAT_rev, delimiter=" ", fmt="%s");
    f.write("\r\n")
    
    #FORWARD scan
    V_frw = V_cell[:,1]
    J_frw = J_cell[:,1]
    P_frw = J_frw*V_frw
    Vm_frw = V_frw[np.argmin(P_frw)];
    Jm_frw = J_frw[np.argmin(P_frw)];
    Jsc_frw = np.interp(0, V_frw, J_frw);
    Voc_frw = np.interp(0, J_frw, V_frw);
    FF_frw = (Vm_frw*Jm_frw) / (Voc_frw*Jsc_frw);
    Eff_frw = np.absolute(Jsc_frw*Voc_frw*FF_frw) / (P_in);
    FLOATS_frw = np.array([ Eff_frw ,  Voc_frw ,  Jsc_frw ,  FF_frw ]);
    DAT_frw =  np.vstack((NAMES, FLOATS_frw));  
    f.write("Cell no %d for FORWARD scan \r\n" % (cell_no+1))
    np.savetxt(f, DAT_frw, delimiter=" ", fmt="%s");
    f.write("\r\n")
    
    cell_no += 1;
    
f.close()
