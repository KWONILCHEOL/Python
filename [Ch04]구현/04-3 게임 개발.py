n, m = map(int, input().split())

d = [[False] * m for _ in range(n)]
x, y, direction = map(int, input().split())
d[x][y] = True

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction = (direction + 3) % 4

count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if d[nx][ny] == False and array[nx][ny] == 0:
        d[nx][ny] = True
        x,y = nx,ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if array[nx][ny] == 0:
            x,y = nx,ny
        else:
            break
        turn_time = 0

print(count)