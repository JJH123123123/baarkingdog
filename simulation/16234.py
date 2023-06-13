

from sys import stdin, setrecursionlimit
from collections import deque
from copy import deepcopy
setrecursionlimit(100000)
input = stdin.readline

N, L, R = map(int,input().split())


field =[list(map(int,input().split())) for _ in range(N)]
next_field = deepcopy(field)
T = 0
flag = False

mv = [[-1,0],[1,0],[0,-1],[0,1]]

vis = [[False for _ in range(N)] for ___ in range(N)]
places = deque([]) # [sum, [(y1,x1)]]

tmp_sum = 0 
def dfs(y:int, x:int):
    global N, L, R, mv, tmp_sum
    cur = field[y][x]
    tmp_sum += cur
    places.append((y,x))
    for dir in range(4):
        ny, nx = y + mv[dir][0], x + mv[dir][1]
        if(0>ny or 0>nx or ny>=N or nx>=N): continue
        
        if((L<= abs(cur - field[ny][nx])<= R) and not vis[ny][nx]):
            vis[ny][nx] = True
            dfs(ny,nx)
    return


# do : field -> prev_field
# store : field <- prev_field
# 
while(1):
    flag = False
    # vis 배열 초기화
    for i in range(N):
        for j in range(N):
            vis[i][j] = False

    for i in range(N):
        for j in range(N):
            # L<= 차이 <= R 면 발동
            for dir in range(4):
                ny, nx = i + mv[dir][0], j + mv[dir][1]
                if(0>ny or 0>nx or nx>=N or ny>=N): continue
                if(L<=abs(field[i][j]-field[ny][nx])<=R):
                    # do 
                    if(not vis[i][j]):
                        vis[i][j] = True
                        vis[ny][nx] = True
                        dfs(ny,nx)
                        # places에 저장된 배열의 함을 구하기

            cnt = len(places)
            if(cnt):
                tmp_sum//= cnt
                while places:
                    y, x = places.popleft()
                    next_field[y][x] = tmp_sum
                    tmp_sum = 0
                    flag = True
    # 다음 기록으로 넘겨주기
    if(not flag):
        break
    field = deepcopy(next_field)
    T+=1
print(T)
