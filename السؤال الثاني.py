def binary(a):
    l=[]
    while True:
        l.append(a%2)
        a//=2
        if a==0:
            break
    l.reverse()
    return l

num=int(input('enter a number'))
x=binary(num)
for i in x:
    print(i,end="")
