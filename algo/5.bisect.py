import bisect

arr = [1, 2, 4, 6, 8]
position = bisect.bisect_left(arr, 4)
print(position)  # Вывод: 2


