import sys

n = int(sys.stdin.readline())
students = []

for _ in range(n):
    students.append(sys.stdin.readline().rstrip().split())

students.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for student in students:
  print(student[0])
