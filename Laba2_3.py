n,m = [int(i) for i in input().split()]

t = ['.'],['*']
t1 = ['*'],['.']
a = [ t*(m//2) if i % 2 == 0 else t1*(m//2) for i in range(n)]

for i in range(n):
    for j in range(m):
        print(a[i][j],end = ' ')
    print()