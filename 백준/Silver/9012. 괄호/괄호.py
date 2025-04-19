import sys

T = int(input())

for _ in range(T):
    string = sys.stdin.readline().strip()
    stack = []
    is_vps = True

    for s in string:
        if s == "(":
            stack.append(s)
        elif s == ")":
            if not stack:
                is_vps = False
                break
            stack.pop()

    if stack:
        is_vps = False

    if is_vps:
        print("YES")
    else:
        print("NO")