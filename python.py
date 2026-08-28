def calcu_Sum(n):
    if(n==0):
        return 0
    return calcu_Sum(n-1) +n
sum=calcu_Sum(5)
print(sum)
    