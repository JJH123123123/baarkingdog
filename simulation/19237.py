
from sys import stdin
input = stdin.readline

N, M, k = map(int,input().split())
# 냄새는 상어가 k번 이동하고 나면 사라진다.
field =  []
mv = [[0,0],[-1,0,],[1,0],[0,-1],[0,1]]

#  N×N 크기의 격자 중 M개의 칸에 상어가 한 마리씩 들어 있다. 맨 처음에는 모든 상어가 자신의 위치에 자신의 냄새를 뿌린다. 
#  그 후 1초마다 모든 상어가 동시에 상하좌우로 인접한 칸 중 하나로 이동하고, 자신의 냄새를 그 칸에 뿌린다. 냄새는 상어가 k번 이동하고 나면 사라진다.

# 각 상어가 이동 방향을 결정할 때는, 먼저 인접한 칸 중 아무 냄새가 없는 칸의 방향으로 잡는다.
# 그런 칸이 없으면 자신의 냄새가 있는 칸의 방향으로 잡는다. 이때 가능한 칸이 여러 개일 수 있는데,
# 그 경우에는 특정한 우선순위를 따른다. 우선순위는 상어마다 다를 수 있고, 같은 상어라도 현재 상어가 보고 있는 방향에 따라 또 다를 수 있다. 
# 상어가 맨 처음에 보고 있는 방향은 입력으로 주어지고, 그 후에는 방금 이동한 방향이 보고 있는 방향이 된다.

# output 
# 1번 상어만 격자에 남게 되기까지 걸리는 시간을 출력한다. 단, 1,000초가 넘어도 다른 상어가 격자에 남아 있으면 -1을 출력한다.


smells = [[[0,0] for i in range(N)] for _ in range(N)]

for i in range(N):
    field.append(list(map(int,input().split())))

for i in range(N):
    for j in range(N):
        if(field[i][j]==0):
            field[i][j] = 411

shark_cnt = 0
sharks_dir = [ [[0 for i in range(4)] for j in range(5) ] for _ in range(M+1)]

cur_shark = [0] + list(map(int,input().split()))

for i in range(1,1+M):
    for dir in range(1,1+4):
        sharks_dir[i][dir] = [0] + list(map(int,input().split()))

def smallCntDown():
    for i in range(N):
        for j in range(N):
            if(smells[i][j][0]>0):
                smells[i][j][0]-=1
                if(smells[i][j][0]==0):
                    smells[i][j] = [0,0]
    return

# how to implement remove and follow its priority rules ?

def findNew(cur_shark_y, cur_shark_x, shark_type,shark_dir):
    empty_possible = [] 
    not_empty_possible = [] 
    find = None
    for dir in sharks_dir[shark_type][shark_dir][1:]:
        ny, nx = cur_shark_y + mv[dir][0], cur_shark_x +  mv[dir][1]
        if(0>ny or 0>nx or ny>=N or nx>=N): continue

        if(smells[ny][nx][0]==0):
            return [ny,nx,dir]
            # 0은 지금 냄새 X
        else:   
            if(smells[ny][nx][1]==shark_type):
                not_empty_possible.append([ny,nx,dir])
            else:
                continue

    return not_empty_possible[0]

    
def smell():
    for i in range(N):
        for j in range(N):
            if(field[i][j]!=411):
                if(smells[i][j][0]==0):
                    smells[i][j] = [k, field[i][j]]
                else:
                    smells[i][j] = [k, field[i][j]]
    return

def MovewithDelete(prev_y, prev_x, cur_shark_y, cur_shark_x, shark_type, changed_dir):
    # global M
    ny, nx = cur_shark_y, cur_shark_x # + mv[changed_dir][1]
    if(field[ny][nx]==411):
        field[prev_y][prev_x] = 411
        field[ny][nx] =  shark_type
    else:
        if(field[ny][nx] > shark_type):
            field[ny][nx] = shark_type
            field[prev_y][prev_x] = 411
        else:
            # delete 
            field[prev_y][prev_x]=411
            pass    
    return

def countExist():
    cnt = 0
    for i in range(N):
        for j in range(N):
            if (field[i][j]!=411):
                cnt+=1
            
    return cnt

def main():
    # global M
    t = 0
    while(t<=1000 and countExist()>1):
        smell()
        mvs = []
        for i in range(N):
            for j in range(N):      
                if(field[i][j]!=411):
                    # print(i,j,field[i][j])  
                    ny,nx, next_dir = (findNew(i,j, field[i][j],cur_shark[field[i][j]]))
                    cur_shark[field[i][j]] = next_dir
                    mvs.append([i,j,next_dir])
        for i,j, next_dir in mvs:
            ny, nx = i + mv[next_dir][0], j + mv[next_dir][1]
            MovewithDelete(i,j,ny, nx, field[i][j], cur_shark[field[i][j]])
        smallCntDown()
        # print("t : ", t)
        # for i in range(N):
        #     for j in range(N):
        #         print(field[i][j],end= " ")
        #     print()
        t += 1 


    if(t>1000 or shark_cnt>1):
        print(-1)
    else:
        print(t)

    return
main()

