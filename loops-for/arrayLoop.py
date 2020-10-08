def insert_squares(arr, num):
    # add square of numbers from 1 to num to the list named arr and return list
    for n in range(1, num + 1):
        arr.append(n*n)
    return arr