t = [[0 for x in range(7)] for y in range(7)]
pi = [[[0 for z in range(2)]for x in range(7)] for y in range(7)]
discountfat = 1
MAX_ITERS = 10
epsilon = 0.001
dirs = ["N", "S", "E", "W", "NE", "NW", "SE", "SW", "STAY"]
displacement=[[-1,0],[1,0],[0,1],[0,-1],[-1,1],[-1,-1],[1,1],[1,-1],[0,0]]
windcase = 2
def printmatrix(mm):
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in mm]))

# Reward function, returns 0 if reaches point (3,6) else return -1
def reward(direction):
    if direction[0] == 3 and direction[1] == 6:
        return 0
    else:
        return -1

def wind(direction):
    if direction[1] >=3 and direction[1] <=5:
        direction = [direction[0]-windcase, direction[1]]
    #if direction[0] < 0:
    #    direction = [0, direction[1]]
    return direction

def move(curloc,k):
    curloc = wind(curloc)
    curloc[0]= curloc[0] + displacement[k][0]
    curloc[1]= curloc[1] + displacement[k][1]
    if curloc[0]<0: curloc[0]=0
    if curloc[1]<0: curloc[1]=0
    if curloc[0]>6: curloc[0]=6
    if curloc[1]>6: curloc[1]=6
    return curloc

def val_iter():
    iters = 0
    target = [[-1 for x in range(7)] for y in range(7)]
    target[3][6]=0
    reference = [[0 for x in range(7)] for y in range(7)]
    while iters < MAX_ITERS:
        iters += 1
        delta = 0
        direction = "STAY"
       
        for i in range(7):
            for j in range(7):
                reference[i][j]=target[i][j]
        for i in range(7):
            for j in range(7):
                rewards = -100000000
                for k in range(9):
                    next_step = move([i,j],k)
                    re_sum = reference[next_step[0]][next_step[1]]
                    if re_sum > rewards:
                        rewards = re_sum
                        pi[i][j][0] = k
                        pi[i][j][1] = -1
                    else:
                        if re_sum == rewards:
                            pi[i][j][1] =k
                     
                target[i][j] = reward([i,j]) + rewards
                if abs(target[i][j] - reference[i][j]) > delta:
                    delta = abs(target[i][j] - reference[i][j])
        if delta < epsilon:
            break
    return target
            
#printmatrix(t)
printmatrix(val_iter())
t1 = [[0 for x in range(7)] for y in range(7)]
for i in range(7):
    for j in range(7):
        t1[i][j]=pi[i][j][0]
printmatrix(t1)
for i in range(7):
    for j in range(7):
        t1[i][j]=pi[i][j][1]
printmatrix(t1)




