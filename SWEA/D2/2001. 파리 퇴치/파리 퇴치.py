for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    final_list = []
    for _ in range(N):
        rand_list = list(map(int, input().split()))
        final_list.append(rand_list)

    pari_list = []
    for k in range(N - M + 1):
        for l in range(N - M + 1):
            pari_ = 0
            for i in range(k, k + M):
                for j in range(l, l + M):
                    pari_ += final_list[i][j]
            pari_list.append(pari_)
    answer = max(pari_list)
    print(f'#{tc} {answer}')