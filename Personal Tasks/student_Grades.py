# define a function that takes a dictionary of student names mapped to a list of test scores.
# Return a new dictionary showing each student's average score

def mean(numbers):
    total_mean = 0
    for num in numbers:
        total_mean += num
    return (total_mean/len(numbers))


scores = {"Tommy":[30, 40, 50, 60, 70], "Jacob":[35, 55, 40, 70, 100], "Pascal":[90, 100, 80, 70, 65]}
 
def student_grader(grades):
    final = {}
    for student, grade in grades.items():
        avg = (sum(grade)/len(grade))
        final[student] = avg
    return final

print(student_grader(scores))

    