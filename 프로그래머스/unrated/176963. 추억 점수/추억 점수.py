def solution(name, yearning, photo):
    answer = [0 for k in range(len(photo))]
    yearning_dict={}
    for i in range(len(name)):
        yearning_dict[name[i]]=yearning[i]
    print(yearning_dict)
    for j in range(len(photo)):
        for k in range(len(photo[j])):
        
            if photo[j][k] not in yearning_dict:
                answer[j]+=0
                print(photo[j][k])
            else:
                answer[j]+=yearning_dict[photo[j][k]]
                
                        
    return answer