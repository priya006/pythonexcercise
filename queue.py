from collections import deque
#list as queue [First in last out]
queue = deque(['Eric', 'John', 'Michael'])
print(queue)
queue.append('Au')
print(queue)

queue.popleft()
print(queue)




if __name__ == "__main__":
    pass

