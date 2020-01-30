def a_minute(student_state):
    possible = False
    new_state = student_state

    for student in range(len(student_state)):

        if student_state[student] == "A":
            new_state[student_state+1] = student_state[student+1]
            possible = True
        else:
            new_state[student_state+1]=student_state[student]

    return possible,new_state



test_cases = int(input())

for _ in range(test_cases):

    student_no = int(input())



