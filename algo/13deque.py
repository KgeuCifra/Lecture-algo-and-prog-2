from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
print(queue.popleft())  # Вывод: 1
