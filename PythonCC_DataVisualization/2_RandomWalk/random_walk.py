import time
from random import choice
import numpy as np
import matplotlib.pyplot as plt

class RandomWalk():
    def __init__(self, num_steps=5000, max_step_length=5):
        self.num_steps = num_steps
        self.max_step_length = max_step_length
        self.curr_step = 0 
        self.x_steps = [0]
        self.y_steps = [0]

    def take_a_walk(self):
        while self.curr_step < self.num_steps:  

            x_dir = choice([-1, 1])
            x_mag = choice(list(range(self.max_step_length+1)))
            x_step = x_dir * x_mag

            y_dir = choice([-1, 1])
            y_mag = choice(list(range(self.max_step_length+1)))
            y_step = y_dir * y_mag

            # print("x_step is", x_step)
            # print("y_step is", y_step)
            
            if x_step == 0 and y_step == 0:
                continue
            
            next_x = self.x_steps[-1] + x_step
            next_y = self.y_steps[-1] + y_step

            self.x_steps.append(next_x)
            self.y_steps.append(next_y)

            ### caption section out if you don't want to animate
            """
            time.sleep(0.05)
            f = open("inputstream", "a")
            ln = str(next_x) + "," + str(next_y) + "\n"
            f.write(ln)
            """
            ###
            
            self.curr_step += 1

        # print("x and y steps are", self.x_steps, self.y_steps)

    def map_walk(self):
        
        np_x_steps = np.array(self.x_steps)
        np_y_steps = np.array(self.y_steps)
        z_steps = np_x_steps * np_x_steps
        
        plt.figure(figsize=(10, 6), dpi=256)
        plt.scatter(self.x_steps, self.y_steps, c=z_steps, cmap=plt.cm.Greens_r, edgecolor='none', s=40)
        plt.scatter(0, 0, c='blue', s=1000, marker='x')
        
        plt.title("Random Walk", fontsize=30)
        plt.xlabel("Lateral", fontsize=22)
        plt.ylabel("Longitudinal", fontsize=22)

        plt.tick_params(axis="both", which='major', \
            labelsize=12, length=6, width=2, colors=(0, 0, 0), direction='out')

        x_range = max(self.x_steps) - min(self.x_steps)
        y_range = max(self.y_steps) - min(self.y_steps)
        plt.xticks(np.arange(min(self.x_steps), max(self.x_steps)+1, x_range/10)) 
        plt.yticks(np.arange(min(self.y_steps), max(self.y_steps)+1, y_range/10))
        plt.grid()

        plt.savefig('map.png')
        plt.show()
