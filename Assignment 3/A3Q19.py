def list_diff():
    list1 = [1, 2, 3, 5]
    list2 = [2, 4]
    diff = set(list1) - set(list2)
    print("Only in list1:", diff)

list_diff()
