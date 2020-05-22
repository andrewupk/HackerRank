if __name__ == '__main__':

    #students = [['Prashant', 52.22], ['Kush', 52.223], ['Kant', 52.222], ['Kanti', 52.2222], ['Harshit', 52.22222]]
    students = [['Test1', 52], ['Test2', 53], ['Test3', 53]];

    #for _ in range(int(input())):
    #    name = input()
    #    score = float(input())
    #    students.append([name, score])

    def grade(e):
        return e[1]

    def name(e):
        return e


    print(students)
    students.sort(key=grade)
    print(students)

    min_range = 0
    for i in range(1, len(students)):
        if students[i][1] > students[i-1][1]:
            min_range = students[i][1]
            break

    lower_students = []
    for i in range(1, len(students)):
        if students[i][1] == min_range:
            lower_students.append(students[i][0])

    lower_students.sort(key=name)
    print(lower_students)