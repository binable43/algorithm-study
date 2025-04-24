import sys
input = sys.stdin.readline

n, m = list(map(int, input().rstrip().split()))
nums = sorted([int(input().rstrip()) for _ in range(n)])

def lower_bound(target):
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] < target:
            start = mid + 1
        elif nums[mid] > target:
            end = mid - 1
        elif nums[mid] == target:
            if end == mid: break
            end = mid
    if nums[end] == target:
        return end
    else:
        return -1

for _ in range(m):
    print(lower_bound(int(input().rstrip())))