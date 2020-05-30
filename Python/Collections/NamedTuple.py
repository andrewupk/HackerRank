from collections import namedtuple

if __name__ == '__main__':
    N = int(input())
    columns = list(input().split())
    Student = namedtuple('Student', columns)
    students = []
    for i in range(N):
        students.append(Student(*list(input().split())))

    sum = 0
    for student in students:
        sum += int(student.MARKS)

    print('{:.2f}'.format(sum / len(students)))