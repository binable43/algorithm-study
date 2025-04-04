def factorial(n):
    # 이 부분을 채워보세요!
    if n == 1:
        return 1
    elif n == 0:
        return 1

    return n * factorial(n-1)

n = int(input())
print(factorial(n))