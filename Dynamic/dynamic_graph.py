import matplotlib.pyplot as plt
import matplotlib.animation as animation

ColumnNumber = 9;
inputfile = '6E-8';
outputfile = 'Jp_6E-8.mp4';
ymin = -220;
ymax = 0;
frames = 1000;

class FileClass:
    fname = [];
    column_number= 0;
    current_position = 0;
    current_time = 0;
    current_J = 0;
    title = [];
    grid = [];
    value = [];
        
    def __init__(self, column_number, file_name):
        self.column_number = column_number;
        self.fname = open(file_name);
        self.read_grid();
        
    def read_grid(self):
        tmp_data = 0;
        tmp_grid_column_number = 0;
        tmp_grid = [];
        self.fname.seek(0);
        for rows in self.fname:
            parts = rows.split('\t') # split line into parts
            if len(parts) > 1:   # if at least 2 parts/columns
                try:
                    tmp_data = float(parts[tmp_grid_column_number]);
                except:
                    pass;
                else:
                    tmp_grid.append(tmp_data);
            if len(parts) <= 1:
                if len(tmp_grid):
                    break;
        self.grid = tmp_grid;
        self.current_position = 0;
        self.fname.seek(0); # get back to initial position of file
    
    def read_next(self):
        tmp_title = [];
        tmp_value = [];
        tmp_data = 0;
        tmp_position = self.current_position;
        tmp_time = 0;
        tmp_J = 0;
        
        self.fname.seek(self.current_position);
        for rows in self.fname:
                tmp_position += len(rows); # add length of row to current position
                parts = rows.split('\t') # split line into parts
                if len(parts) > 1:   # if at least 2 parts/columns
                    try:
                        tmp_data = float(parts[self.column_number]);
                    except:
                        pass;
                    else:
                        tmp_value.append(tmp_data);
                if len(parts) <= 1:
                    tmp_title.append(parts);
                    if len(tmp_value):
                        tmp_position -= len(rows); # do not count last row
                        break;
        # TIME
        time_string = str(tmp_title[0]).split(' ');
        tmp_time = float(time_string[1]);
        self.current_time = tmp_time;
        
        #CURRENT
        current_string = str(tmp_title[2]).split(' ');
        tmp_J = float(current_string[3]);
        self.current_J = tmp_J;        
        
        # VALUE
        self.value = tmp_value;
        self.current_position = tmp_position;
    
    def get_grid(self):
        return self.grid;
    
    def get_value(self):
        return self.value;
    
    def get_time(self):
        return self.current_time;
        
    def get_current(self):
        return self.current_J;
        
    def __exit__(self):
        self.fname.close();

# Init file class
global ObjectClass;
ObjectClass = FileClass(ColumnNumber, (inputfile));

# Set up figure and animation
fig, ax = plt.subplots(1,1);
#plt.yscale('log');

time_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)
current_text = ax.text(0.02, 0.90, '', transform=ax.transAxes)
line, = ax.plot([],[],'o-');

def init():
    time_text.set_text('');
    current_text.set_text('')
    line.set_data([], []);
    return line;
    
def animate(i):
    ObjectClass.read_next();
    t = ObjectClass.get_time();
    j = ObjectClass.get_current();
    x = ObjectClass.get_grid();
    y = ObjectClass.get_value();
    
    ax.set_xlim([min(x), max(x)]);
    ax.set_ylim(ymin, ymax);
    
    time_text.set_text('Time = %.3e' %t)
    current_text.set_text('Photocurrent = %.3f A m-2' %j)
    line.set_data(x, y);            # update the data
    return line;

ani = animation.FuncAnimation(fig, animate, frames=frames,
                              interval=1, blit=False, init_func=init)
ani.save(outputfile, fps=30, extra_args=['-vcodec', 'libx264'])
