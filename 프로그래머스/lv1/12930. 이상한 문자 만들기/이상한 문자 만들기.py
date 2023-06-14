def solution(s):
    answer =''
    s_list=s.split(" ")

    for i in range(len(s_list)):
        for j in range(len(s_list[i])):
            if j%2==0:
                element=s_list[i][j].upper()
                answer+=element

            else:
                element=s_list[i][j].lower()
                answer+=element
        if i == len(s_list)-1 :
            break
        answer+=" "         

    return answer