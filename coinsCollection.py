def coinsCollection(board):
    result = board
    m = len(board)  # hang
    n = len(board[0])  # lie
    for i in range(1, m):
        for j in range(0, n):
            result[i][j] = max(result[i-1][j], result[i][j-1])+board[i][j]
    return max(result[-1])      

# def coinsRoad(selfroad):
#     road = board
#     while(m>=0 and n>=0):
#         if road[m-1][n] ==road[m][n-1]:
#             road[i-1][j] = 1
#             road[i][j-1] = 0
#             i = i-1
#             j= j-1
#         elif road[i-1][j]>road[i][j-1]:
#             road[i-1][j] = 0
#         elif road[i-1][j]<road[i][j-1]:
#             road[i][j-1] = 1
#             j = j-1
#     return road

board = [[0, 0, 0, 0, 1, 0 ], [0,1,0,1,0,0], [
    0,0,0,1,0,1], [0,0,1,0,0,1], [1,0,0,0,1,0]]
print(coinsCollection(board))


