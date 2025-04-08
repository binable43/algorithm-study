def solution(array):
    good_word_num = 0

    for i in range(len(array)):
        stack = []

        for j in range(len(array[i])):
            if stack and stack[-1] == array[i][j]:
                stack.pop()
            else:
                stack.append(array[i][j])

        if not stack:
            good_word_num += 1

    print(good_word_num)

N = int(input())
words = [input() for _ in range(N)]

solution(words)