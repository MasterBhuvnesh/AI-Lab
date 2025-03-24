#CODE

# Dictionary to store the assigned colors for each node (region).
assigned = {
    'WA': None,  # Western Australia
    'NT': None,  # Northern Territory
    'Q': None,   # Queensland
    'SA': None,  # South Australia
    'NSW': None, # New South Wales
    'V': None,   # Victoria
    'T': None    # Tasmania
}

# Dictionary to define the neighbors of each node (region).
neighbors = {
    'WA': ['NT', 'SA'],          
    'NT': ['WA', 'Q', 'SA'],     
    'Q': ['NT', 'SA', 'NSW'],    
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],  
    'NSW': ['Q', 'SA', 'V'],     
    'V': ['SA', 'NSW'],          
    'T': []                      
}

# Function to assign colors to nodes (regions) while ensuring no adjacent regions have the same color.
def assignCol():
    for key in assigned.keys():
        i, flag = 0, 0  
        current = key    

        if assigned[key] is None:
            while i <= (len(domain) - 1):
                assigned[current] = domain[i]
                print('The assigned colour for', current, 'is:', assigned[current])

                flag = checkConst(current)

                if flag == 1:
                    i = i + 1
                else:
                    break  

# Function to check constraints (e.g., no adjacent regions have the same color)
def checkConst(current):
    for neighbor in neighbors[current]:
        if assigned[neighbor] == assigned[current]:
            return 1
    return 0  

# Example domain of colors (e.g., Red, Green, Blue)
domain = ['Red', 'Green', 'Blue']

# Call the function to assign colors
assignCol()

# OUTPUT

"""
The assigned colour for WA is: Red
The assigned colour for NT is: Red
The assigned colour for NT is: Green
The assigned colour for Q is: Red
The assigned colour for SA is: Red
The assigned colour for SA is: Green
The assigned colour for SA is: Blue
The assigned colour for NSW is: Red
The assigned colour for NSW is: Green
The assigned colour for V is: Red
The assigned colour for T is: Red
"""