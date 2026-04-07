def student_averages(students):
    result = {}

    for student, grades in students.items():
        avg = sum(grades.values()) / len(grades)
        result[student] = round(avg)

    return result


def assignment_averages(students):
    result = {}
    counts = {}

    for grades in students.values():
        for assignment, score in grades.items():
            result[assignment] = result.get(assignment, 0) + score
            counts[assignment] = counts.get(assignment, 0) + 1

    for assignment in result:
        result[assignment] = round(result[assignment] / counts[assignment])

    return result