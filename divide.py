def divide_and_conquer(list):
    if len(list) <= 1:
        print("Base case:", list)
        return
    mid = len(list) // 2
    left = list[:mid]
    right = list[:mid]
    print("Divide:", list)
    divide_and_conquer(left)
    divide_and_conquer(right)

numbers = list(range(1,6))
divide_and_conquer(numbers)