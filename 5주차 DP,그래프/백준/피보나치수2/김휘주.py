# https://www.acmicpc.net/problem/2748
# 답은 나오는데,,, 틀렸습니다,,??

n = int(input())

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(n))