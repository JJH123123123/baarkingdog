

# 첫째 줄부터 4개의 줄에 각 칸의 들어있는 물고기의 정보가 1번 행부터 순서대로 주어진다. 
# 물고기의 정보는 두 정수 ai, bi로 이루어져 있고, ai는 물고기의 번호, bi는 방향을 의미한다.
# 방향 bi는 8보다 작거나 같은 자연수를 의미하고, 1부터 순서대로 ↑, ↖, ←, ↙, ↓, ↘, →, ↗ 를 의미한다.
from sys import setrecursionlimit
setrecursionlimit(100000)

           #   북     북서    서       남서    남    남동    동    북동  
mv = [[0,0],[-1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1]]

tmp_field = []
for i in range(4):
    tmp_field.append(list(map(int,input().split())))

field = [ [0 for i in range(4)] for _ in range(4)]

for i in range(4):
    for j in range(0,8,2):
        field[i][j//2] = [tmp_field[i][j], tmp_field[i][j+1]]

# 처음 값에 대해서는 따로 빼서 계산 
first = field[0][0][0]

import copy

def rotationAll(k_field, shark_y, shark_x):
    new_field = copy.deepcopy(k_field)
    st = dict()
    for i in range(4):
        for j in range(4):
            if(new_field[i][j][0]==0 or new_field[i][j][0]==-1): continue
            st[new_field[i][j][0]] = [i,j, new_field[i][j][1]]

    for key in range(1,17):
        if(st.get(key,0)==0): continue
        cur_y, cur_x, cur_dir = st[key]

        for _ in range(1,1+8):
            ny, nx = cur_y + mv[cur_dir][0], cur_x + mv[cur_dir][1]

            if(0>ny or 0>nx or ny>=4 or nx>=4):
                cur_dir = (cur_dir+1)%9
                if(cur_dir==0):
                    cur_dir = 1
                continue
            if(new_field[ny][nx][0]==0):
                cur_dir = (cur_dir+1)%9
                if(cur_dir==0):
                    cur_dir = 1
                continue              
 
            # 빈 공간 + 다른 물고기만 등장
            # 자리 변경 
            # print(key,cur_dir)
            new_field[cur_y][cur_x][1] = cur_dir
            next_num,next_dir = new_field[ny][nx]
            new_field[ny][nx], new_field[cur_y][cur_x] = new_field[cur_y][cur_x], new_field[ny][nx]
            st[next_num] = [cur_y,cur_x,next_dir]
            st[key] = [ny,nx,cur_dir]
   
            break
    # 상어 자리 
    s_dir = new_field[shark_y][shark_x][1]
    possible = []
    s_y = shark_y
    s_x = shark_x

    while(1):
        s_y, s_x= s_y + mv[s_dir][0], s_x + mv[s_dir][1]
        if(s_y<0 or s_x<0 or s_y>=4 or s_x>=4):
            break
        # 빈 경우 
        if(new_field[s_y][s_x][0]==-1 or new_field[s_y][s_x]==0): continue
        possible.append([s_y,s_x])
    
    return possible, new_field

res = 0
field[0][0][0] = 0

def main(tmp_field, shark_y, shark_x, ret):
    global res, first
    possible, next_field = rotationAll(tmp_field,shark_y,shark_x)
 
    if len(possible)==0:
        res = max(res,ret)
        return

    for y,x  in possible:
        
        tmp = next_field[y][x][0]
        if(tmp==-1 or tmp == 0): continue
        ret += tmp

        next_field[shark_y][shark_x][0] = -1
        next_field[y][x][0] = 0
        
        main(next_field,y,x,ret)
        ret -= tmp

        next_field[y][x][0] = tmp
        next_field[shark_y][shark_x][0] = 0

main(field, 0,0,0)
print(res+first)

