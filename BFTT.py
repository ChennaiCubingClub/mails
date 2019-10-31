testcases = int(input())
for i in range(testcases):
    number=input()
    cnt= number.count('3')
    if cnt>=3:
        print (int(number))
    else :
        j=1
        while j==1:
            number=int(number)
            number +=1
            if str(number).count('3') >2:
                j=0
                print (int(number))
            
                
            
        
    