from sys import stdin
from collections import deque
input = stdin.readline

# 첫째 줄에 보드의 크기 N이 주어진다. (2 ≤ N ≤ 100) 다음 줄에 사과의 개수 K가 주어진다. (0 ≤ K ≤ 100)
N = int(input())

MAP = [ [0 for _ in range(N+1)] for i in range(N+1)]



# 동 남 서 북 
# 1 2 3 4  
rotate_dir = {'L':1, 'D':2}
dir = 1
moves = [[0,0], [0,1],[1,0],[0,-1],[-1,0]]

def rotate(order):
    global dir
    dir = (4 + dir + (-1) ** rotate_dir[order])%4
    if(dir == 0):
        dir = 4
    # 오른쪽 1을 보고 있을 떄 왼쪽으로 회전하는 게 북쪽이므로 4 - 1 + 1 = 0 = 4 
    # 오른쪽 1을 보고 있을 떄 오른쪽으로 회전하는 게 남쪽이므로  1 + 1 = 2 (mod 4) 
    return



snake = deque([[0, 0]])


apple = int(input())
for i in range(apple):
    apple_y, apple_x = map(int, input().split())
    MAP[apple_y-1][apple_x-1] = 1

change  = int(input())

rotates = []

for _ in range(change):
    time, direction = input().split()
    time = int(time)
    rotates.append([time,direction])

rotates.sort()
rotates = deque(rotates)

cur_time = 1
while(1):

    snake_ny, snake_nx = snake[-1][0] + moves[dir][0], snake[-1][1] + moves[dir][1]
    if(len(rotates)>0 and rotates[0][0]==cur_time):
        # print(rotates[0][1])
        rotate(rotates[0][1])
        rotates.popleft()
    
    # 벽 out of bound
    if(0 > snake_ny or 0 > snake_nx or snake_ny >= N or snake_nx >= N):
        break

    if(MAP[snake_ny][snake_nx]) == 0:
        MAP[snake_ny][snake_nx] = 2
        snake.append([snake_ny,snake_nx])
        # print(snake[0][0], type(snake[0][1]))
        y, x = snake[0]
        MAP[y][x] = 0
        # [snake[0][1]
        snake.popleft()
    elif MAP[snake_ny][snake_nx] == 1:
        snake.append([snake_ny,snake_nx])
        MAP[snake_ny][snake_nx] = 2
    else: # 이미 남아있는 
        break
    # for row in MAP:
    #     print(*row)
    # print()
    cur_time += 1
print(cur_time)        



# 다음 K개의 줄에는 사과의 위치가 주어지는데, 첫 번째 정수는 행, 두 번째 정수는 열 위치를 의미한다. 사과의 위치는 모두 다르며, 맨 위 맨 좌측 (1행 1열) 에는 사과가 없다.



