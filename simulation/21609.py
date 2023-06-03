from sys import stdin
from collections import deque 
input = stdin.readline





# 1. 크기가 가장 큰 블록 그룹을 찾는다.
# 2. 그러한 블록 그룹이 여러 개라면 포함된 무지개 블록의 수가 가장 많은 블록 그룹, 
# 3. 그러한 블록도 여러개라면 기준 블록의 행이 가장 큰 것을, 그 것도 여러개이면 열이 가장 큰 것을 찾는다.
# 그룹의 기준 블록은 무지개 블록이 아닌 블록 중에서 행의 번호가 가장 작은 블록, 그러한 블록이 여러개면 열의 번호가 가장 작은 블록이다.
# 그룹에 속한 블록의 개수는 2보다 크거나 같아야 하며
# bfs

mv = [[0,0], [0,1],[1,0],[0,-1],[-1,0]]

#행, 열 정보를 어떻게 기록해야 하지?
    
N, M = map(int,input().split())
school = [[ ] for j in range(N)]
tmp_school = [[0 for i in range(N)] for j in range(N)]


for i in range(N):
    school[i] = list(map(int,input().split()))
    # for j in range(N):
        # school[i][j] = 
 

def dfs(ny, nx, target):

    if(school[ny][nx] ==6):
        return
    
    school[ny][nx] = 6
    if(0>ny or 0>nx or ny>=N or nx>=N):
        return

    for dir in range(1,1+4):
        nny, nnx = ny + mv[dir][0], nx + mv[dir][1]
        if(0>nny or 0>nnx or nny>=N or nnx>=N): continue
        if(school[nny][nnx] == target or school[nny][nnx] == 0):
            dfs(nny,nnx,target)

    

def main():

    vis = [[0 for i in range(N)] for j in range(N)]
    total = []
    # 1 단계 
    for i in range(N):
        for j in range(N):
            if(school[i][j] == -1 or school[i][j]==0) or school[i][j]==6: continue
            target = []
            target_y = i
            target_x = j
            rainbow_cnt = 0
            # since 0은 기준이 될 수가 없어서
            if(vis[i][j] == True): continue
            # 방문했던 경우는 이미 다른 곳에서 체크를 한 것이기에 
            deq = deque([(i,j)])
            vis_cnt = 1
            vis[i][j] = True
            while(deq):
                cur_y, cur_x =  deq.popleft()

                for dir in range(1,4+1):
                    ny, nx = cur_y + mv[dir][0], cur_x + mv[dir][1]
                    if(0>ny or 0>nx or ny>=N or nx>=N or vis[ny][nx]): continue

                    if(school[ny][nx]==0):
                        deq.append((ny,nx))
                        target.append((ny,nx))
                        vis[ny][nx]=True
                        vis_cnt+=1
                        rainbow_cnt +=1
                    elif school[i][j] == school[ny][nx]:
                        deq.append((ny,nx))
                        vis[ny][nx]=True
                        vis_cnt+=1
                        if(target_y==i):
                            if(target_x < j):
                                target_y, target_x = i,j

                        else: # target_y <= i
                            if(target_y < i):
                                target_y, target_x = i,j
            
            for y,x in target:
                vis[y][x] = False
            if(vis_cnt>=2):
                total.append((vis_cnt,rainbow_cnt, target_y, target_x, school[i][j]))

    if len(total)==0:
        return 0

    # total sort()
    total.sort(key=lambda x: (-x[0],-x[1],-x[2],-x[3]))
    d, rainbow, tar_y, tar_x, v = total[0]
    dfs(tar_y, tar_x, school[tar_y][tar_x])
    return d
    # 이중에서 



def gravity():
    # 아래의 6을 위로 뺴내는 구현 추가
    for j in range(N): # 왼쪽 열부터 오른쪽 열까지 아래 행에서부터 하나씩 중력을 적용해주기
        for i in range(N-1,-1,-1): # N-1 ~ 1 왜? 계속 내려야 하니까 
            # 벽이랑 이미 지워진 건 pass
            if( school[i][j]==-1):
                continue
            cur_y = i
            while(1):
                if(cur_y == N-1):
                    break
                if(school[cur_y+1][j]==-1):
                    break

                if(school[cur_y+1][j]==6):
                    # swap if there exists vacant
                    school[cur_y+1][j], school[cur_y][j] = school[cur_y][j], school[cur_y+1][j]

                cur_y +=1

    return


def rotation():
    for i in range(N):
        for j in range(N):
            tmp_school[i][j] = school[j][N-i-1]
    
    for i in range(N):
        for j in range(N):
            school[i][j] = tmp_school[i][j]

    return



output = 0
while(1):
    ret = main()
 
    if(ret==0):
        break
    output += ret**2

    gravity()
    rotation()
    gravity()
print(output)



