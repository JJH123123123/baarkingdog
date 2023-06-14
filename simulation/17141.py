from itertools import combinations as combi
from sys import stdin, setrecursionlimit
from collections import deque

setrecursionlimit(100000)

input = stdin.readline


# 첫째 줄에 연구소의 크기 N(5 ≤ N ≤ 50), 놓을 수 있는 바이러스의 개수 M(1 ≤ M ≤ 10)이 주어진다.
# backtracking 
N, M = map(int,input().split())

mv = [ [0,-1],[0,1], [-1,0], [1,0] ]
field = []


virus_places = deque([])
for i in range(N):
    field.append(list(map(int,input().split())))
    for j in range(N):
        if (field[i][j] == 2):
            virus_places.append((i,j))




def outbound(y,x):
    return (0>y or 0>x or y>=N or x>=N)

cur_cnt = 0
vis = [[False for _ in range(N)] for __ in range(N)]

ret = 130130130103030
def check():
    for i in range(N):
        for j in range(N):
            if field[i][j] != 1 and not vis[i][j]:
                return False
            
    return True


def bfs(places):
    global ret
    places = deque(places)
    for idx in range(len(places)):
        vis[places[idx][0]][places[idx][1]] = True
    T = 0
    if(check()):
        ret = min(T,ret)
        return

    while(places):

        for _ in range(len(places)):
            y, x = places.popleft()
            for dir in range(4):
                ny, nx = y + mv[dir][0], x + mv[dir][1]
                if outbound(ny,nx): continue
                if(field[ny][nx]==1): continue
                if(not vis[ny][nx]):
                    vis[ny][nx] = True
                    places.append((ny,nx))
        T+=1
        if(check()):
            ret = min(ret,T)
            return
    return
    


for possible in combi(virus_places,M):
    for i in range(N):
        for j in range(N):
            vis[i][j] = False
    bfs(possible)

if (ret==130130130103030):
    print(-1)
else:
    print(ret)


