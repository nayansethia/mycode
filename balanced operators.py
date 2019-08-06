from stack import stack
s=stack()
l=input()
#hi
t=1
for i in range(len(l)):
    if l[i] =="{" or l[i]=="[" or l[i]=="(":
        s.push(l[i])
    elif s.isempty():
        print("Not balanced")
        t=0
        break
    elif l[i]=="}":
        k=s.pop()
        if k!="{":
            print("Not balanced")
            t=0
            break
    elif l[i]=="]":
        k=s.pop()
        #print(k)
        if k!="[":
            print("Not balanced")
            t=0
            break
    elif l[i]==")":
        k=s.pop()
        if k!="(":
            print("Not balanced")
            t=0
            break
    #s.printstack()
if t==1:
    print("Balanced")
    
