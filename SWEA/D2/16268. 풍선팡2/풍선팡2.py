for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    final_list = []
    for _ in range(N):
        rand_list = list(map(int, input().split()))
        final_list.append(rand_list)
    
    pung = 0
    max_pung =[]
    for i in range(N):
        for j in range(M):
            if i == 0 and j ==0:
                pung = final_list[i][j] + final_list[i][j+1] + final_list[i+1][j]
            elif i ==N-1 and j ==0:
                pung = final_list[i][j] + final_list[i-1][j] + final_list[i][j+1]
            elif i == 0 and j !=0 and j !=M-1:
                pung = final_list[i][j] + final_list[i][j-1] + final_list[i][j+1] + final_list[i+1][j]
            elif i ==0 and j ==M-1:
                pung = final_list[i][j] + final_list[i][j-1] + final_list[i+1][j]
            elif i !=0 and i !=N-1 and j ==0:
                pung =final_list[i][j] + final_list[i+1][j] + final_list[i-1][j] +final_list[i][j+1]
            elif i == N-1 and j !=0 and j!=M-1 :
                pung = final_list[i][j]+ final_list[i-1][j]+final_list[i][j-1]+final_list[i][j+1]
            elif i ==N-1 and j ==M-1:
                pung = final_list[i][j] + final_list[i-1][j] + final_list[i][j-1]
            elif i !=N-1 and i!=0 and j ==M-1:
                pung = final_list[i][j] + final_list[i-1][j]+final_list[i+1][j] + final_list[i][j-1]
            else:
                pung = final_list[i][j] + final_list[i-1][j]+final_list[i+1][j] + final_list[i][j-1]+final_list[i][j+1]
            max_pung.append(pung)
    answer = max(max_pung)
    print(f'#{tc} {answer}')