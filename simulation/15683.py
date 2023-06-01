from itertools import product as permu_repeat # 중복순열
from sys import stdin
input = stdin.readline

N, M = map(int,input().split()) # 사무실의 가로, 세로
MAP = [ [] for i in range(N)]
# VIS = [ [False for] for i in range(N)]

for i in range(N):
    MAP[i] = list(map(int,input().split()))

# 1 : one side, two : two side, three : front and right, 4번 : 뒤 빼고 다. 5번 전부 
# 6 : 벽 
AREA = N*M 

CCTV = [] 
# 벽 지워주기 

for i in range(N):
    for j in range(M):
        if(1<=MAP[i][j]<=6):
            AREA-=1

        if(0<MAP[i][j]<6):
            CCTV.append([i,j,MAP[i][j]]) # row, col, type of CCTV

def check():
    global AREA
    cnt = 0
    for i in range(N):
        for j in range(M):
            if MAP[i][j]==7:
                MAP[i][j] = 0
                cnt+=1
    return cnt

# main function 1,2,3,4,5
# 1 2 3 4 
# 동 남 서 북 시계방향
# index : 1부터 만드려고 0,0 넣어줌
dx = [0,1,0,-1,0]
dy = [0,0,1,0,-1]

def move_forward(dir, cctv_y, cctv_x):
    ny_cctv, nx_cctv = cctv_y, cctv_x
    while(1):
        ny_cctv, nx_cctv = ny_cctv + dy[dir], nx_cctv + dx[dir]
        if(ny_cctv<0 or nx_cctv < 0 or ny_cctv >= N or nx_cctv >= M or MAP[ny_cctv][nx_cctv]==6):
            return
        if(1<=MAP[ny_cctv][nx_cctv]<=5): continue
        MAP[ny_cctv][nx_cctv] = 7
    return 

def clockwise_rotate(dir,count):
    for i in range(count):
        dir = (dir+1)%4
        if(dir==0) : dir = 4
    return dir


def main(dir, cctv_y, cctv_x, cctv_type):
    if cctv_type == 1:
        move_forward(dir,cctv_y, cctv_x)
    if cctv_type == 2:
        move_forward(dir,cctv_y, cctv_x)
        move_forward(clockwise_rotate(dir,2),cctv_y, cctv_x)
    if cctv_type == 3:
        move_forward(dir,cctv_y, cctv_x)
        move_forward(clockwise_rotate(dir,1),cctv_y, cctv_x)

    if cctv_type == 4:
        move_forward(dir,cctv_y, cctv_x)
        move_forward(clockwise_rotate(dir,1),cctv_y, cctv_x)
        move_forward(clockwise_rotate(dir,3),cctv_y, cctv_x)
    
    if cctv_type == 5:
        move_forward(1,cctv_y, cctv_x)
        move_forward(2,cctv_y, cctv_x)
        move_forward(3,cctv_y, cctv_x)
        move_forward(4,cctv_y, cctv_x)

    return

ret = AREA

for rotations in permu_repeat([1,2,3,4],repeat= len(CCTV)): # 각 경우에 대해서 
    # 회전을 시켜주고, CCTV를 작동해주고 
    # print(rotations)
    for idx, cctv in enumerate(CCTV):
        # print(cctv)
        cctv_y, cctv_x, cctv_type = cctv
        main(rotations[idx], cctv_y, cctv_x, cctv_type)
    # AREA의 최솟값 찾아주기 
    # 다시 MAP == 7 부분은 0으로 초기화 => check 한번에 구현 
    # for row in MAP:
    #     print(*row)
    # print()
    tmp = AREA - check()
    ret = min(ret,tmp)
print(ret)

# print(check()) # ok 



# CCTV의 방향 및 탐색 범위


