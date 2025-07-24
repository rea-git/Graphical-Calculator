"""import re
string = "1*x^2+2*x^1+1*x^0"
eqn = string.split('+')
neweqn = []
for i in eqn:
    neweqn.append(re.split(r'[*^]+',i))
print(neweqn)
x = [-5,-4,-3,-2,-1,0,1,2,3,4,5]
y = []
for i in x:
    ssum = 0
    for j in range(len(neweqn)):
        ssum+=int(neweqn[j][0])*(i**int(neweqn[j][2]))
    y.append(ssum)
print(y)"""
m=3
n=4
l1 = [[0 for _ in range(n)]for _ in range(m)]
print(l1)