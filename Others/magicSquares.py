import numpy as np

n = int(input("n = "))

arr = np.zeros((n,n))

point = [0, n//2]

def fix(point):
    while (point[0] < 0 or point[1] >= n or point[0] >=n or point[1] < 0):
        if point[0] < 0:
            point[0] = n-1

        if point[0] >= n:
            point[0] = 0
        
        if point[1] >= n:
            point[1] = 0

        if point[1] < 0:
            point[1] = n-1

    return point

for i in range(1, n**2+1):
    arr[tuple(point)] = i

    point[0] -= 1
    point[1] += 1

    point = fix(point)
    
    while arr[tuple(point)] != 0 and i != n**2:
        point[0] += 1
        point[1] -= 1

        point = fix(point)

        point[0] += 1

        point = fix(point)

print(arr)
