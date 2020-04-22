# problema de hackerRank
n=int(input())
if n%2!=0:
    print('Weird')
elif n in range(2,5):
    print('Not Weird')
elif n in range(6,21):
    print('Weind')
else:
    print('Not Weird')