from sys import stdin
from itertools import combinations as combi
from collections import deque
input = stdin.readline

N, M = map(int,input().split())
field = []
possible = []
empty_cnt = 0
for i in range(N):
    field.append(list(map(int,input().split())))
    for j, val in enumerate(field[-1]):
        if(val==2):
            possible.append((i,j))
        if(field[i][j]==0):
            empty_cnt+=1

mv = [[0,1],[1,0],[0,-1],[-1,0]]

ret = 130103130031 
def bfs(comb):
    global N, empty_cnt

    vis_time = [[False for _ in range(N)] for __ in range(N)]
    
    deq = deque(comb)

    for i in range(len(deq)):
        y,x = deq[i]
        vis_time[y][x] = True # 방문한 세균
    T = 0
    total_cnt = 0
    tmp = 130103130031 
    while len(deq)>0 and (total_cnt!=empty_cnt):
        for _ in range(len(deq)):
            y, x  = deq.popleft()
            for dir in range(4):
                ny, nx = y + mv[dir][0], x + mv[dir][1]
                if(0>ny or 0>nx or ny>=N or nx>=N): continue
                if(field[ny][nx]==1 or vis_time[ny][nx]): continue # 벽이므로
                vis_time[ny][nx] = True
                if(field[ny][nx]==0):
                    total_cnt+=1
                deq.append((ny,nx))
        T+=1
        if(T>=ret):
            return T
        
    if(total_cnt==empty_cnt):
        tmp = min(tmp,T)

    return tmp

for cur_combi in combi(possible,M):
    T = bfs(cur_combi)
    ret = min(T,ret)
    if(ret==0):
        break
if(ret==130103130031):  ret = -1

print(ret)