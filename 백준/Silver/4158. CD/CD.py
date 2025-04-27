import sys

while True:
    N, M = map(int, sys.stdin.readline().strip().split())
    if N == 0 and M == 0:
        break

    sg_cd_set = set()
    for _ in range(N):
        sg_cd = sys.stdin.readline().strip()
        sg_cd_set.add(sg_cd)

    common_cd = 0
    for _ in range(M):
        sy_cd = sys.stdin.readline().strip()
        if sy_cd in sg_cd_set:
            common_cd += 1

    print(common_cd)