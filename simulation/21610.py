from sys import stdin
from collections import deque
input  = stdin.readline

# input 
N, M = map(int,input().split())
field = [list(map(int,input().split())) for _ in range(N)]
orders = [list(map(int,input().split())) for _ in range(M)]

# 상수들, 처음 구름은 아래와 같은 4가지 구름을 갖고 있다. N>=2이라서 가능하다.
cloud = deque([ [N-1,0], [N-1,1], [N-2,0], [N-2,1]]) # [ [cur_y, cur_x], ... ]
vis = [[False for _ in range(N)] for __ in range(N)]
mv = [[0,0], [0,-1], [-1,-1],
    [-1,0], [-1,1], [0,1],
      [1,1],[1,0],[1,-1]] # index from 1 to 8

# 예를 들어, (N, 2)에서 인접한 대각선 칸은 (N-1, 1), (N-1, 3)이고, (N, N)에서 인접한 대각선 칸은 (N-1, N-1)뿐이다.

def genMove(dir:int, time:int): 

    # 0 vis : initialize 
    for i in range(N):
        for j in range(N):
            vis[i][j] = False

    # 1, 2 move add
    dy, dx = mv[dir][0], mv[dir][1]
    for _ in range(len(cloud)):
        y, x =  cloud.popleft()
        ny, nx = (y+time*dy)%N, (x+time*dx)%N
        if(not vis[ny][nx]):
            field[ny][nx] += 1
            vis[ny][nx] = True
            cloud.append((ny,nx))


    while(cloud):
        y, x = cloud.popleft() # 3 
        # 4 
        for diag in range(2,9,2):
            ny, nx = y + mv[diag][0], x + mv[diag][1]
            if(0>ny or 0>nx or ny>=N or nx>=N): continue

            if(field[ny][nx]>0):
                field[y][x]+=1
        
    # 5 
    for i in range(N):
        for j in range(N):
            if(field[i][j]>=2 and not vis[i][j]):
                cloud.append((i,j))
                field[i][j]-=2
    return

for d, s in orders:
    genMove(d,s)

ret = 0
for i in range(N):
    ret += sum(field[i])

print(ret)


