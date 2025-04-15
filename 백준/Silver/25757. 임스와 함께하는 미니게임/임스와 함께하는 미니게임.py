def solution(people, game):
    play_time = 0

    if game == "Y":
        play_time = len(people)
    elif game == "F":
        play_time = len(people) // 2
    elif game == "O":
        play_time = len(people) // 3

    return print(play_time)

N, game = input().split()
people = set()

for _ in range(int(N)):
    name = input()
    people.add(name)

solution(people, game)