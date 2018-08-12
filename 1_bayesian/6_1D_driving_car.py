
import matplotlib.pyplot as plt
%matplotlib inline

import numpy as np

def output_map(grid):
    
    x = [i for i in range(len(grid))]
    y = [0.2 for i in range(len(grid))]
    plt.bar(x, y)
    plt.xlabel("Grid Space")
    plt.ylabel("Probability")
    plt.title("Probability of the robot being at each space on the grid")
    plt.show()


def update_probabilities(grid, updates):
        
    for i in range(len(updates)):
        pos = updates[i][0]
        new_prob = updates[i][1]
        if(pos < len(grid) and pos >= 0):
            grid[pos] = new_prob 
    
    return grid
