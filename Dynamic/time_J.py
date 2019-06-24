import numpy as np 
import sys

#file_name = "space_pulse_illumination_0.000000V.dat";
file_name = sys.argv[-1]
fname = open(file_name);
column_number = 5;
tmp_title = [];
tmp_value = [];
tmp_data = 0;
tmp_time = 0;
tmp_data_number = 0;
J = [];
time = [];
value = [];
value_space_pos = [];
i = 0;
position_number = 1;

for rows in fname:
    parts = rows.split('\t') # split line into parts
    if len(parts) > 1:   # if at least 2 parts/columns
        try:
            tmp_data = float(parts[column_number]);
        except:
            pass;
        else:
            tmp_value.append(tmp_data);
    if len(parts) <= 1:
        tmp_title.append(parts);
    if len(rows.strip()) == 0 :
        tmp_data_number += 1;
        # TIME
        time_string = str(tmp_title[0]).split(' ');
        tmp_time = float(time_string[1]);
        time.append(tmp_time);
                
        #CURRENT
        current_string = str(tmp_title[2]).split(' ');
        J.append(float(current_string[3]));      
        
        #VALUE
        value.append(tmp_value);
        value_space_pos.append(value[i][position_number]);
        
        tmp_title = [];
        tmp_value = [];
        i += 1;

fname.close();

#SAVE RESULTS
save_results = open('test.txt', 'w')
for i in range(len(time)):
  save_results.write(str(time[i]) + "\t" + str(value_space_pos[i]) + "\t" + str(J[i]) + "\n");
  
save_results.close();