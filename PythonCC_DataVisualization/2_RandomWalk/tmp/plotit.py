import matplotlib.pyplot as plt
from random_walk import RandomWalk

###
rw = RandomWalk()
rw.take_a_walk()
plt.scatter(rw.x_steps, rw.y_steps, edgecolor='none', s=15)
plt.show()
###
 
while True:
    rw = RandomWalk()
    rw.take_a_walk()
    
    # plt.figure(dpi=128, figsize=(10, 6))
    
    point_numbers = list(range(rw.num_steps))
    plt.scatter(rw.x_steps, rw.y_steps, edgecolor='none', s=15)
        
    # plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    # plt.scatter(rw.x_steps[-1], rw.y_steps[-1], c='red', edgecolors='none', s=100)
        
    # plt.axes().get_xaxis().set_visible(False)
    # plt.axes().get_yaxis().set_visible(False)
        
    plt.show()
    
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break

