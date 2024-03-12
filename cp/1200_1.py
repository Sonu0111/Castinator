
#Optimisation pending
def get_max_of_activities(n,a,b,c):
    result=0
    for x in range(0,n):
        check_sum=0
        for y in range(0,n):
            if(x!=y):
                for z in range(0,n):
                    if(y!=z and x!=z):
                        check_sum=a[x]+b[y]+c[z]
                        result=max(result,check_sum)

    return result

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    print(get_max_of_activities(n,a,b,c))

