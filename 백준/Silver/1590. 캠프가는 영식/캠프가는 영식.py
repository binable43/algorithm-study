import sys

N, T = map(int, sys.stdin.readline().split())

bus_info = []

for _ in range(N):
    S, I, C = map(int, sys.stdin.readline().split())
    bus_info.append([S, I, C])

min_waiting_time_list = []

for S, I, C in bus_info:
    bus_arrival = []
    time = S

    for i in range(C):

        if time == T:
            min_waiting_time_list.append(0)
            break
        elif time > T:

            min_waiting_time = time - T
            min_waiting_time_list.append(min_waiting_time)
            break

        time += I


min_waiting_time_list = sorted(min_waiting_time_list)

if not min_waiting_time_list:
    print(-1)
else:
    print(min_waiting_time_list[0])