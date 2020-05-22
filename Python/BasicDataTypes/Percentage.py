if __name__ == '__main__':
    """
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    """

    student_marks = {'Krishna': [67.0, 68.0, 69.0], 'Arjun': [70.0, 98.0, 63.0], 'Malika': [52.0, 56.0, 60.0]}
    query_name = 'Malika'
    marks = student_marks[query_name]
    sum = 0
    for i in range(len(marks)):
        sum += marks[i]

    print("{:.2f}".format(sum / len(marks)))