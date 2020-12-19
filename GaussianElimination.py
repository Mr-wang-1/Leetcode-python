'''
高斯消去法
通过消元过程把一般方程组化成三角方程组
再通过回代过程求出方程组的解
'''
def GaussianElimination(A,B):
    N = len(A)
    for i in range(1,N):
        for j in range(i,N):
            # 计算消元因子delta
            delta = A[j][i-1]/A[i-1][i-1]
            # 从第i-1行开始消元
            for k in range(i-1,N):
                # 对A进行消元
                A[j][k] = A[j][k] - A[i-1][k]*delta
            # 对B进行消元
            B[j] = B[j]-B[i-1]*delta
    # 进行回代，直接将方程的解保留在B中
    B[N-1] = B[N-1]/A[N-1][N-1]
    for i in range(N-2,-1,-1):
        for j in range(N-1,i,-1):
            B[i] = B[i]- A[i][j]*B[j]
        B[i] = B[i]/A[i][i]
    # 返回所有解的列表
    return B

matrixA = [[2,-1,1],[4,1,-1],[1,1,1]]
matrixB = [1,5,0]
print('方程的解为',GaussianElimination(matrixA, matrixB))
