testcases= int(input())
for i in range(testcases):
    days=int(input())
    sday=[0]
    sprob=[0]

    for j in range(days):
        schedule=input().split()
        sday.append(int(schedule[0]))
        sprob.append(sprob[-1]+int(schedule[1]))
        #schedule.append(list(map(int,input().split())))
    print(sday,sprob)
    queries=int(input())
    impd=0
    ans=0
    for k in range(queries):
        q=list(map(int,input().split()))
        for i in sday:
            if i <= q[0]:
                impd=i
            else:
                break
        ans=sprob[sday.index(impd)]
        if ans >= q[1]:
            print("Go Camp")
        else :
            print("Go Sleep")
        
        