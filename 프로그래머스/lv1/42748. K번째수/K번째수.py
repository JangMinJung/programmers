def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        A=sorted(array[commands[i][0]-1:commands[i][1]])
        answer.append(A[commands[i][2]-1])
    return answer