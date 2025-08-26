def entry(testify):
    number = 5
    return f"{testify} is the name of this function"

gate_pass = None
def gate_fee(gate_pass):
    if gate_pass > 18:
        return "You are allowed to enter"
    else:
        return "You are not allowed to enter"

numbers = []

def mean(numbers):
    total_mean = 0
    for num in numbers:
        total_mean += num
    return (total_mean/len(numbers))


def calculate_grade(score):
    if score >= 90:
        return "Grade is A"
    elif score >= 80:
        return "Grade is B"
    elif score >= 70:
        return "Grade is C"
    elif score >= 60:
        return "Grade is D"
    else:
        return "Grade is Failure"



print("hello")
