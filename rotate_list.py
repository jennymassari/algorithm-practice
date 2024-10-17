# Add your clarifying questions here

def rotate_list(list, shift_by):
    if shift_by > len(list):
        shift_by = shift_by%len(list) # 5, 10 -> 0
    
    for _ in range(shift_by):
        last_number = list.pop()
        list.insert(0, last_number)
        print(list)
    return list
    # if shift_by number is > list length: # 7, 4
    #     subtract list length form the shift_by number # new shift by is 3
    #     return remainer of shift_by numer divided by length # lenght of list is 5, shift number is 11, 11%5 = 1
    # a for loop with the shift_by number
    #     pop on the list
    #     insert at [0] the popped number

    
assert rotate_list([1, 2, 3, 4, 5], 3) ==[3, 4, 5, 1, 2]
# assert rotate_list([1, 2, 3, 4, 5], 0) ==[1, 2, 3, 4, 5]
# assert rotate_list([1, 2, 3, 4, 5], 5) ==[1, 2, 3, 4, 5]
# assert rotate_list([1, 2, 3, 4, 5], 35) ==[1, 2, 3, 4, 5]
