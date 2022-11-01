def binary_search(sequence, item):
    begin_index = 0
    end_index = len(sequence)-1
    while begin_index <= end_index:
        mid_point = begin_index + (end_index-begin_index) //2
        mid_point_value = sequence[mid_point]
        if mid_point_value == item:
            return mid_point
        elif item < mid_point_value:
            end_index = mid_point - 1
        else:
            begin_index = mid_point + 1
    return None
sequence_a = [0, 1, 2, 4, 5 ,6 ,7, 8, 9, 11]
item_a = 3

print(binary_search(sequence_a, item_a))

