import sys

while True:
    line = sys.stdin.readline().rstrip()
    if line == ".":
        break

    stack = []
    is_balance = True

    for l in line:

        if l == "(" or l == "[":
            stack.append(l)
        elif l == ")":
            if not stack or stack[-1] != "(":
                is_balance = False
                break
            stack.pop()
        elif l == "]":
            if not stack or stack[-1] != "[":
                is_balance = False
                break
            stack.pop()


    if is_balance and not stack:
        print("yes")
    else:
        print("no")
