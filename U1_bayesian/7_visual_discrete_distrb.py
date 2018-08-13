def bar_heights(intervals, relative_probabilities, total_probability):

    heights = []
    
    #TODO: sum the relative probabilities
    total_relative_prob = sum(relative_probabilities)
    
    for i in range(0, len(relative_probabilities)):
        
        #TODO: Looping through the relative_probabilities list, 
        #      take one probability at a time and 
        #      calculate the area of each bar. Think about how you can 
        #      calculate the area of a bar knowing the total_probability,
        #      relative probability, and the sum of the relative probabilities.
        
        #HINT: It's possible to do this in one line of code
        bar_area = total_probability*(relative_probabilities[i]/total_relative_prob)
        
        # TODO: Calculate the height of the bar and append the value to the
        # heights list. Remember that the area of each bar 
        # is the width of the bar times the height of the bar
        
        #HINT: It's possible to do this in one line of code
        heights.append(bar_area/(intervals[i+1]-intervals[i]))
        
    return heights
