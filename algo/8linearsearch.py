def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1
data = [5, 3, 7, 2, 9]
index = linear_search(data, 7)
print("Элемент найден на позиции:", index)

