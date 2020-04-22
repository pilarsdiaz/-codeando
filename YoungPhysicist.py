#Problema de Code Forces 69AYoungPhysicist
n= int(input())
lis=[]*n
for i in range(n):
    cor=[int(j) for j in input().split()]
    lis.append(cor)
x,y,z=0,0,0
for i in range(n):
    x=x+lis[i][0]
    y=y+lis[i][1]
    z=z+lis[i][2]
if x==0 and y==0 and z==0:
    print('YES')
else:
    print('NO')