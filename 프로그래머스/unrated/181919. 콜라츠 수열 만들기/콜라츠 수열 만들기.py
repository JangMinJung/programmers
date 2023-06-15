def solution(n):
    answer = [n]
    while True:
        if n%2==0:
            n=n/2
            answer.append(n)
        else: 
            n=3*n+1
            answer.append(n)
        if n==1:
            break
    return answer