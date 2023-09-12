def initial_state():
    return (8, 0, 0)  # Change initial state to (8, 0, 0)

def is_goal(s):
    return s == (4, 4, 0)  # Change the goal check

def successors(s):
    x, y, z = s
    actions = []
    
    # Define valid pouring actions and their corresponding costs
    if x > 0 and y < 5:
        amount_to_pour = min(x, 5 - y)
        actions.append(((x - amount_to_pour, y + amount_to_pour, z), amount_to_pour))
    if x > 0 and z < 3:
        amount_to_pour = min(x, 3 - z)
        actions.append(((x - amount_to_pour, y, z + amount_to_pour), amount_to_pour))
    if y > 0 and x < 8:
        amount_to_pour = min(y, 8 - x)
        actions.append(((x + amount_to_pour, y - amount_to_pour, z), amount_to_pour))
    if y > 0 and z < 3:
        amount_to_pour = min(y, 3 - z)
        actions.append(((x, y - amount_to_pour, z + amount_to_pour), amount_to_pour))
    if z > 0 and x < 8:
        amount_to_pour = min(z, 8 - x)
        actions.append(((x + amount_to_pour, y, z - amount_to_pour), amount_to_pour))
    if z > 0 and y < 5:
        amount_to_pour = min(z, 5 - y)
        actions.append(((x, y + amount_to_pour, z - amount_to_pour), amount_to_pour))
    
    return actions
