import sys;
import re


script = sys.argv[0]
filename = sys.argv[1]

#filename = 'DG180626_D061_fast_2LS.IV'
fileoutput = filename.replace(".IV", ".dat")
with open(filename, 'r') as myfile:
    data=myfile.read().replace('\r\n', '')
    
elements = re.split('\t+', data) 

    
JV_all = elements[143::]
J_all = JV_all[:len(JV_all)/2:]
V_all = JV_all[len(JV_all)/2::]

V1 = V_all[:len(V_all)/4:]
V2 = V_all[len(V1):len(V1)+len(V_all)/4:]
V3 = V_all[len(V1)+len(V2):len(V1)+len(V2)+len(V_all)/4:]
V4 = V_all[len(V1)+len(V2)+len(V3):len(V1)+len(V2)+len(V3)+len(V_all)/4:]

J1 = J_all[:len(J_all)/4:]
J2 = J_all[len(J1):len(J1)+len(J_all)/4:]
J3 = J_all[len(J1)+len(J2):len(J1)+len(J2)+len(J_all)/4:]
J4 = J_all[len(J1)+len(J2)+len(J3):len(J1)+len(J2)+len(J3)+len(J_all)/4:]

JV_string_out = zip(V1,J1,V2,J2,V3,J3,V4,J4);
footer = elements[1:5:]
with open(fileoutput, 'w') as fp:
    fp.write('\r\n'.join('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % x for x in JV_string_out))
    fp.write('\r\n')
    fp.write(''.join('%s \n' % footer))
    fp.write('setup=minisunsim; speed=0(0=fast,1=slow,2=max,3=min); measurement mode=perovskite abcd hysteresis; light;lamp voltage=\r\n\r\n')
    fp.write('---------------------------------------------------------------------------')
    fp.write('\r\n\r\n')
    