import sys

N, M, K = map(int, sys.stdin.readline().split())

subjects = []

for _ in range(N):
    s, p = sys.stdin.readline().split()
    subjects.append([s, int(p)])

t_list = []
for _ in range(K):
    t = sys.stdin.readline().strip()
    t_list.append(t)

base_score = 0
non_recommended = []

for s, p in subjects:
    if s in t_list:
        base_score += p
    else:
        non_recommended.append([s, p])

sorted_list_desc = sorted(non_recommended, key=lambda x: x[1], reverse=True)
max_score = base_score + sum([subject[1] for subject in sorted_list_desc[:M - K]])

sorted_list_asc = sorted(non_recommended, key=lambda x: x[1])
min_score = base_score + sum([subject[1] for subject in sorted_list_asc[:M - K]])

print(min_score, max_score)