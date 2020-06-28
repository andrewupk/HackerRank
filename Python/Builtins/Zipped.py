if __name__ == '__main__':
    [N, X] = map(int, input().split())
    subject_marks = []
    for i in range(X):
        subject_marks.append(input().split())

    zipped = list(zip(*subject_marks))
    for student in zipped:
        average = 0
        for mark in student:
            average += float(mark)
        print(average / X)

