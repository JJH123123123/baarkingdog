from sys import stdin
from collections import deque
input = stdin.readline

N,M = map(int,input().split())

mv = [[0,-1],[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1]]

smells = [[0 for _ in range(4)] for __ in range(4)]


field = [[[0 for ____ in range(8)] for _ in range(4)] for __ in range(4)]
# fishs = deque([])
prev_field = [[[0 for ____ in range(8)] for _ in range(4)] for __ in range(4)]
# 죽은 걸 표현을 못해
for _ in range(N):
    y,x,d = map(int,input().split())
    field[y-1][x-1][d-1]+=1

 
# 두 번 전 연습에서 생긴 물고기의 냄새가 격자에서 사라진다.
new_mv = [[0,0],[-1,0],[0,-1],[1,0],[0,1]] # 상, 좌, 하, 우
Sy, Sx = map(int,input().split())
Sy-=1
Sx-=1

            


vis = [ [False for _ in range(4)] for __ in range(4)]
tmp = 555
total_cnt = 0 

def sharkMove(Sy, Sx, step, cnt, fishcnt):
    global total_cnt, tmp

    if(step==3):
        # print(total_cnt, cnt,fishcnt,tmp,"fsihsifehfifh")
        if(cnt>=100):
            if(fishcnt > total_cnt):
                tmp = cnt

                total_cnt = fishcnt
            else:
                if total_cnt == fishcnt:
                    tmp = min(cnt,tmp)

        return
    for dir in range(1,1+4):
        ny, nx = Sy+new_mv[dir][0], Sx + new_mv[dir][1]
        if(0>ny or 0>nx or ny>=4 or nx>=4): continue
        tmp_cnt = 0

        if(not vis[ny][nx]):
            for fishdir in range(8):
                tmp_cnt += field[ny][nx][fishdir]
            vis[ny][nx] = True
            sharkMove(ny,nx, step+1,  cnt *10 + dir, fishcnt + tmp_cnt)
            vis[ny][nx] = False
        else:
            sharkMove(ny,nx, step+1,  cnt *10 + dir, fishcnt )

    return

from copy import deepcopy

def Move(Sy, Sx):
    global field, prev_field
    prev_field =  deepcopy(field)

    for i in range(4):
        for j in range(4):
            for dir in range(8):
                cur_cnt = prev_field[i][j][dir]
                
                if(cur_cnt==0):
                    continue
                d = dir
                # flag = False
                for _ in range(8):
                    ny, nx = i + mv[d][0], j + mv[d][1]
                    if(ny<0 or nx<0 or ny>=4 or nx>=4): 
                        d = (d-1)%8
                        continue
                    if(ny==Sy and nx == Sx):
                        d = (d-1) %8
                        continue
                    if(smells[ny][nx]>0):
                        d = (d-1)%8
                        continue
                    field[ny][nx][d] += cur_cnt
                    field[i][j][dir] -= cur_cnt
                    break

    return

def smell_delete():
    global smells
    for i in range(4):
        for j in range(4):
            if(smells[i][j]>0):
                smells[i][j]-=1
    return

def sharkMoveSmell(order:int):
    # print(order)
    global Sy, Sx # , field, new_mv
    first, second, third = order//100, (order//10)%10, order%10
    moves = [first, second, third]
    # new moves
    for dir in moves:
        Sy, Sx = Sy + new_mv[dir][0], Sx + new_mv[dir][1]
        if(Sy<0 or Sx<0 or Sy>=4 or Sx>=4):
            Sy, Sx = Sy - new_mv[dir][0], Sx - new_mv[dir][1]
            return
        for i in range(8):
            if(field[Sy][Sx][i]):
                smells[Sy][Sx] = 3
            field[Sy][Sx][i] = 0 
    return

def duplicate():
    global field, prev_field
    for i in range(4):
        for j in range(4):
            for dir in range(8):
                field[i][j][dir] += prev_field[i][j][dir]
                prev_field[i][j][dir] = 0
    return

def solve(M):
    global Sy, Sx, tmp, total_cnt
    for _ in range(M):
        Move(Sy, Sx)
        sharkMove(Sy,Sx,0,0,0)
        sharkMoveSmell(tmp)
        smell_delete()
        tmp = 555
        total_cnt = 0
        duplicate()
    ret = 0 
    for i in range(4):
        for j in range(4):
            for dir in range(8):
                ret += field[i][j][dir]
    print(ret)
    return 

solve(M)



# 상어가 연속해서 3칸 이동한다. 상어는 현재 칸에서 상하좌우로 인접한 칸으로 이동할 수 있다. 
# 연속해서 이동하는 칸 중에 격자의 범위를 벗어나는 칸이 있으면, 그 방법은 불가능한 이동 방법이다.
# 연속해서 이동하는 중에 상어가 물고기가 있는 같은 칸으로 이동하게 된다면, 
# 그 칸에 있는 모든 물고기는 격자에서 제외되며, 제외되는 모든 물고기는 물고기 냄새를 남긴다.
# 가능한 이동 방법 중에서 제외되는 물고기의 수가 가장 많은 방법으로 이동하며, 
# 그러한 방법이 여러가지인 경우 사전 순으로 가장 앞서는 방법을 이용한다. 사전 순에 대한 문제의 하단 노트에 있다.
# for _ in range(M):
#     #fish move
#     #
#     continue

 

# 냄새 제거 O(16)

# 1  2  3  4  5  6  7 8 
# ←, ↖, ↑, ↗, →, ↘, ↓, ↙ 



# 상어의 이동 방법 중 사전 순으로 가장 앞서는 방법을 찾으려면 
# 먼저, 방향을 정수로 변환해야 한다. 상은 1, 좌는 2, 하는 3, 우는 4로 변환한다.
# 변환을 모두 마쳤으면, 수를 이어 붙여 정수로 하나 만든다. 
# 두 방법 A와 B가 있고, 각각을 정수로 변환한 값을 a와 b라고 하자. a < b를 만족하면 A가 B보다 사전 순으로 앞선 것이다.

# 예를 들어, [상, 하, 좌]를 정수로 변환하면 132가 되고, 
# [하, 우, 하]를 변환하면 343이 된다. 132 < 343이기 때문에, [상, 하, 좌]가 [하, 우, 하]보다 사전 순으로 앞선다.

# 총 43 = 64가지 방법을 사전 순으로 나열해보면 
# [상, 상, 상], [상, 상, 좌], [상, 상, 하], [상, 상, 우], [상, 좌, 상], [상, 좌, 좌], [상, 좌, 하], [상, 좌, 우], [상, 하, 상],
# ..., [우, 하, 하], [우, 하, 우], [우, 우, 상], [우, 우, 좌], [우, 우, 하], [우, 우, 우] 이다.