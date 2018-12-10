

def calculateManhattan(initial_state):
    initial_config = initial_state
    manDict = 0
    for i,item in enumerate(initial_config):
        prev_row,prev_col = int(i/ 3) , i % 3
        goal_row,goal_col = int(item /3),item % 3
        manDict += abs(prev_row-goal_row) + abs(prev_col - goal_col)
    return manDict


with open('test.txt', 'r') as fh:
    line = fh.read().split("\n")

    print(calculateManhattan([1,1]))
    
    for i in line:
        split = i.split(",")
        c = [int(split[0]), int(split[1])]
        print(calculateManhattan(c))
