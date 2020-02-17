def max_Num(number):
    largest = number[0]
    for item in number:
        if item > largest:
            largest = item
    return largest