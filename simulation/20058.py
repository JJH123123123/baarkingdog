from collections import deque
from sys import stdin
input = stdin.readline

N, Q = map(int,input().split())

field = [ list(map(int,input().split())) for _ in range(pow(2,N)) ]
L = list(map(int,input().split())) # 2^L x 2^L 만큼의 sub array if L = 0 => 1 x 1 

outBound = pow(2,N)
mv = [[0,1],[1,0],[0,-1],[-1,0]]

def rotateSubarray( cur_y:int, cur_x:int, step:int):
    global outBound, field


    Length = pow(2, step)
    new_field = [[0 for _ in range(outBound)] for __ in range(outBound)]

    for y in range(cur_y, outBound, Length):
        for x in range(cur_x, outBound, Length):
            for l in range(Length):
                for q in range(Length):
                    new_field[y + q][x + Length - l -1] = field[y+l][x+q]

    field = new_field
    melting = deque([])
    for row in range(outBound):
        for col in range(outBound):
            cnt = 0
            for dir in range(4):
                ny, nx = row + mv[dir][0], col + mv[dir][1]
                if(ny<0 or nx<0 or nx>=outBound or ny>=outBound): continue

                if(field[ny][nx]!=0):
                    cnt+=1
            if(cnt<3 and field[row][col]!=0):
                melting.append((row,col))
 
    while(len(melting)):
        y, x = melting.popleft()
        field[y][x]-=1

    return

vis = [ [False for _ in range(outBound)] for __ in range(outBound)]

def bfs(cur_y:int, cur_x:int):
    global outBound
    place = deque([(cur_y,cur_x)])
    cnt = 1
    S = field[cur_y][cur_x]
    vis[cur_y][cur_x] = True

    while(place):
        cur_y, cur_x = place.popleft()
        
        for dir in range(4):
            ny, nx = cur_y + mv[dir][0], cur_x + mv[dir][1]
            if(0>ny or 0>nx or ny>=outBound or nx>=outBound):
                continue
            if(not vis[ny][nx] and field[ny][nx]):
                vis[ny][nx]=True
                S += field[ny][nx]
                cnt += 1
                place.append((ny,nx))

    return cnt, S


for i in range(Q):
    rotateSubarray(0,0,L[i])
    # another = rotate_and_melting(another,outBound,0)

# 파이어스톰을 시전하려면 시전할 때마다 단계 L을 결정해야 한다.
# 파이어스톰은 먼저 격자를 2^L × 2^L 크기의 부분 격자로 나눈다. 
# 후, 모든 부분 격자를 시계 방향으로 90도 회전시킨다.
# 이후 얼음이 있는 칸 3개 또는 그 이상과 인접해있지 않은 칸은 얼음의 양이 1 줄어든다.


res = 0
M = -1
flag = False
for i in range(outBound):
    for j in range(outBound):
        if(field[i][j] >0 and not vis[i][j]):
            flag = True
            tmp, S = bfs(i,j)
            res += S
            M = max(tmp,M)

if(not flag):
    print(0)
    print(0)

else:
    print(res)
    print(M)

