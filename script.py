#open the file with initail mails
with open('mails.txt') as f:
    original = f.read().splitlines()
    
print(len(original))
with open('temp.txt') as f:
    temp = f.read().splitlines()
print(len(temp))
    
final=set(original+temp)
fin_list=list(final)
print(len(fin_list))

with open('mails.txt', 'w') as f:
    for item in fin_list:
        f.write("%s\n" % item)
        
