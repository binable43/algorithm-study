def josephus_problem(n, k):
    result_arr = []

    next_index = k-1
    people_arr = list(range(1, n+1))

    while people_arr:
        result = people_arr.pop(next_index)
        result_arr.append(result)
        if len(people_arr) != 0:
            next_index = (next_index + (k - 1)) % len(people_arr)

    print(f"<{', '.join(map(str, result_arr))}>")

n, k = map(int, input().split())
answer = josephus_problem(n, k)
