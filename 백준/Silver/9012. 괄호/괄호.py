import sys

T = int(input())

candidates = []

for _ in range(T):
    candidate = sys.stdin.readline().strip()
    candidates.append(candidate)

for letter in candidates:
    left = 0
    right = 0

    for l in letter:

        if right > left:
            break

        if l == "(":
            left += 1
        elif l == ")":
            right += 1

    if right == left:
        print("YES")
    else:
        print("NO")