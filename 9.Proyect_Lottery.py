#We are going to build out a weighted lottery function. you are tasked with making sure that the house win.
#If I have a dictionary like this:
#  weights = {
#      'winning': 1,
#      'losing': 1000
#  }
#
#  print(weighted_lottery(weights))


import numpy as np

def weighted_lottery(weights):
    container_list = [] #we need somtehing to keep a list

    for (name, weight) in weights.items(): #the key-value pairs
        #loop 1 time --- loop 1000 times
        for _ in range(weight):
            container_list.append(name)

    return np.random.choice(container_list)

other_weights = {
    'green': 1,
    'yellow': 2,
    'red': 3
}

print(weighted_lottery(other_weights))