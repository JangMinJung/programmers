def solution(n):
    
    if n==1:
        return [[1]]
    
    else:
        A = [[-1 for j in range(n)] for i in range(n)]

        A[0][0]=1
        (i,j)=(0,0)

        for _ in range(n*n):

            for _ in range(n):
                if A[i][j+1]<0:
                    A[i][j+1]=A[i][j]+1
                    j+=1
                    if j > n-2:
                        break


            for _ in range(n):
                if A[i+1][j]<0:
                    A[i+1][j]=A[i][j]+1
                    i+=1
                    if i > n-2:
                        break                

            for _ in range(n):
                if A[i][j-1]<0:
                    A[i][j-1]=A[i][j]+1
                    j-=1
                    if j < 1:
                        break

            for _ in range(n):
                if A[i-1][j]<0:
                    A[i-1][j]=A[i][j]+1
                    i-=1
                    if i < 1:
                        break                 

            if A[i][j]==n**2:
                break    
    return A