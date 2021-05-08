f = open('input.txt','r')
n = int(f.readline())
ls = list(map(int,f.readline().split()))
ans = max(ls)
k = 0
for i in ls:
    temp = set()
    for j in ls:
        temp.add(j%i)
    if(len(temp)>k):
        k = len(temp)
        ans = i
    elif len(temp)==k:
        ans = min(ans,i)
    # print(temp)
print(ans)

f.close()

f = open('output.txt','w')
f.write(str(ans))
f.close()