#Problema de juez patito 1386
sw=True
num=[]
while sw:
    v=[str(i) for i in input().split()]
    if v[0]=='S':
        num.append(int(v.pop(1)))
        v.pop(0)
    elif v[0]=='A':
        if len(num)==0:
            print('Error')
        else:
            print(max(num))
        v.pop(0)
        
    elif v[0] == 'R':
        if len(num)==0:
            print('Error')
        else:
            i=num.index(max(num))
            num.pop(i)
        v.pop(0)
    elif v[0] == 'I':
        if len(num)==0:
            print('Error')
        else:
            i=num.index(max(num))
            s=max(num)+int(v.pop(1))
            num[i]=s
        v.pop(0)
    elif v[0] == 'D':
        if len(num)==0:
            print('Error')
        else:
            i=num.index(max(num))
            s=max(num)-int(v.pop(1))
            num[i]=s
        v.pop(0)
    elif v[0] == 'T':
        sw=False
