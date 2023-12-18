T = int(input())
for tc in range(1, T+1):
    location, string = input().split()
    string = list(string)
    location = int(location)-1
    # print(string, location)
    del string[location]

    answer = ''
    for i in string:
        answer +=i
    print(answer)