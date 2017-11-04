target = [[0 for x in range(7)] for y in range(7)]
discountfat = 1
MAX_ITERS = 1000
epsilon = 0.001
dirs = ["N", "S", "E", "W", "NE", "NW", "SE", "SW", "STAY"]
windcase = 0
def printmatrix():
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in target]))

# Reward function, returns 0 if reaches point (3,6) else return -1
def reward(direction):
    if direction[0] == 3 and direction[1] == 6:
        return 0
    else:
        return -1

def wind(direction):
    if direction[1] >=3 and direction[1] <=5:
        direction = (direction[0]-windcase, direction[1])
    if direction[0] < 0:
        direction = (0, direction[1])
    return direction

def move(curloc,dir):
    curloc = wind(curloc)
    if dir == "N":
        if curloc[0]-1 >= 0:
            curloc = (curloc[0]-1, curloc[1])
    elif dir == "S":
        if curloc[0]+1 <= 6:
            curloc = (curloc[0]+1, curloc[1])
    elif dir == "E":
        if curloc[1]-1 >= 0:
            curloc = (curloc[0], curloc[1]-1)
    elif dir == "S":
        if curloc[1]+1 <= 6:
            curloc = (curloc[0], curloc[1]+1)
    elif dir == "NE":
        if curloc[0]-1 <= 0 and curloc[1]-1 <= 0:
            return curloc
        elif curloc[0]-1 <= 0:
            curloc = (curloc[0], curloc[1]-1)
        elif curloc[1]-1 <= 0:
            curloc = (curloc[0]-1, curloc[1])
        else:
            curloc = (curloc[0]-1, curloc[1]-1)
    elif dir == "NW":
        if curloc[0]-1 <= 0 and curloc[1]+1 >= 6:
            return curloc
        elif curloc[0]-1 <= 0:
            curloc = (curloc[0], curloc[1]+1)
        elif curloc[1]+1 >= 6:
            curloc = (curloc[0]-1, curloc[1])
        else:
            curloc = (curloc[0]-1, curloc[1]+1)
    elif dir == "SE":
        if curloc[0]+1 >= 6 and curloc[1]-1 <= 0:
            return curloc
        elif curloc[0]+1 <= 6:
            curloc = (curloc[0], curloc[1]-1)
        elif curloc[1]-1 <= 0:
            curloc = (curloc[0]+1, curloc[1])
        else:
            curloc = (curloc[0]+1, curloc[1]-1)
    elif dir == "SW":
        if curloc[0]+1 >= 6 and curloc[1]+1 >= 6:
            return curloc
        elif curloc[0]+1 >= 6:
            curloc = (curloc[0], curloc[1]+1)
        elif curloc[1]+1 >= 6:
            curloc = (curloc[0]+1, curloc[1])
        else:
            curloc = (curloc[0]+1, curloc[1]+1)
    elif dir == "STAY":
        curloc = curloc
    return curloc

def val_iter(target):
    iters = 0
    reference = target
    while iters < MAX_ITERS:
        iters += 1
        delta = 0
        direction = "STAY"
        rewards = -100000000
        for i in range(7):
            for j in range(7):
                pos = (i,j)
                for k in dirs:
                    next_step = move(pos,k)
                    re_sum = reference[next_step[0]][next_step[1]]
                    if re_sum > rewards:
                        reward = re_sum
                        direction = k
                target[i][j] = reward(pos) + epsilon*reward
                if target[i][j] - reference[i][j] > delta:
                    delta = target[i][j] - reference[i][j]
        if delta < epsilon:
            break
    return reference
            
printmatrix()
