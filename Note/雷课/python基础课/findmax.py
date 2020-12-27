def find_max(list1):
    max = list1[0]
    for num in list1:
        if num > max:
            max = num
    return max
