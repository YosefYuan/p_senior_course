def find_largest_element(l):
    if not isinstance(l, list):
        print('input is not a list')
        return
    if len(l) == 0:
        print('empty list')
        return
    largest_element = l[0]
    for item in l:
        if item > largest_element:
            largest_element = item

    print('largest element is: {}'.format(largest_element))

find_largest_element([1, 2, 3, 4, 5])
