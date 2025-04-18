import sys

n = sys.stdin.readline()

names = sys.stdin.readline().split()

# set student dict
student = {}
for name in names:
    student.setdefault(name, 0)

# vote popularity of each student
for _ in range(int(n)):
    popular_students = sys.stdin.readline().split()
    for p_s in popular_students:
        if p_s in student.keys():
            student[p_s] += 1

# sort student dict
sorted_student = dict(sorted(student.items(), key=lambda item: item[1], reverse=True))

# print the result
for s, count in sorted_student.items():
    print(s, count)