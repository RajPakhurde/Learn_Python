def find_max_num(num_list):
    max = num_list[0]
    for num in num_list:
        if num > max:
            max = num

    return max
