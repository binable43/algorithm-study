import sys

def solution(people, game):
    if game == "Y":
        return len(people)
    elif game == "F":
        return len(people) // 2
    elif game == "O":
        return len(people) // 3

N, game = sys.stdin.readline().split()
people = set()

for _ in range(int(N)):
    name = sys.stdin.readline().strip()
    people.add(name)

print(solution(people, game))