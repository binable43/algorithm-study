def solution(array):
    n = len(array)
    set_x = dict()
    set_y = dict()

    for i in range(n):
        set_x.setdefault(array[i][0], 0)
        set_y.setdefault(array[i][1], 0)

    for coord in array:
        if coord[0] in set_x:
            set_x[coord[0]] += 1
        if coord[1] in set_y:
            set_y[coord[1]] += 1

    count_parallel_x = sum(1 for value in set_x.values() if value >= 2)
    count_parallel_y = sum(1 for value in set_y.values() if value >= 2)

    print(count_parallel_x + count_parallel_y)


n = int(input())
coordinate_list = []

for _ in range(n):
    x, y = map(int, input().split())
    coordinate_list.append([x, y])

solution(coordinate_list)