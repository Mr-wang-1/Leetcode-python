
def coinsRoad(result):
    import numpy as np
    road = a=np.zeros((5,6))
    i = len(f)-1
    j =len(f[0])-1

    while(j>=0 and i>=0):
        if f[i-1][j]==f[i][j-1]:
            road[i-1][j] = 1
            road[i][j-1] = 1
            i = i-1
            j = j-1
        elif f[i-1][j]>f[i][j-1]:
            road[i-1][j] = 1
            i = i-1
        elif f[i-1][j]<f[i][j-1]:
            road[i][j-1] = 1
            j = j-1
    print(road)
f = [[0, 0, 0, 0, 1, 0], [0, 1, 1, 2, 2, 2], [
        0, 1, 1, 3, 3, 4], [0, 1, 2, 3, 3, 5], [1, 1, 2, 3, 4, 5]]
print(coinsRoad(f))
