import sys

N = int(sys.stdin.readline())
words = set()

for _ in range(N):
    word = sys.stdin.readline().strip()
    words.add(word)

sorted_words = sorted(words, key=lambda x: (len(x), x))

for word in sorted_words:
    print(word)
