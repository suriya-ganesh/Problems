if __name__ == "__main__":

    test_cases = int(input())
    for _ in range(test_cases):
        student_no = int(input())
        split_value = input().split("A")

        if len(split_value)<2:
            print(0)
        else:
            print(len(max(split_value[1:])))