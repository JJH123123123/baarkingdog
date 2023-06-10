from sys import stdin
from collections import deque

input = stdin.readline

N, M = map(int,input().split())

field = []
field_numbers = [ [0 for _ in range(N)] for __ in range(N)]

bomb_cnt = [ 0,0,0,0]
mv = [ [0,-1],[1,0], [0,1],[-1,0]]
        # 서 남 동 북 
new_mv = [ [-1,0],[1,0], [0,-1],[0,1]]

for _ in range(N):
    field.append(list(map(int,input().split())))

cur_y, cur_x = N//2, N//2

orders = []
for _ in range(M):
    orders.append(list(map(int,input().split())))
  
ret = 0
def blizzard(dir, speed): # O(speed)
    global N
    ny, nx = N//2, N//2
    while(speed):
        ny, nx = ny + new_mv[dir][0], nx + new_mv[dir][1]
        if(0>ny or 0>nx or ny>=N or nx>=N): break
        field[ny][nx] = 0
        speed-=1
    return


def bomb( ): # 
    
    # move 이후라서 field[y][x]가 0이 나오면 끝내면 됨.
    global N,ret
    ny, nx = N//2, N//2
    length = 1
    flag = False
    next_flag = False
    dir = 0
    cur_value = -1
    cnt = 0 
    st = []
    bmb_cnt = 1
    # print("first")
    while(1):
        for _ in range(length):
            ny, nx = ny + mv[dir][0], nx + mv[dir][1]
            if(field[ny][nx] != cur_value):
                if(bmb_cnt>=4):
                    bomb_cnt[cur_value] += bmb_cnt

                    for _ in range(bmb_cnt):
                        y, x = st.pop()
                        field[y][x] = 0
                        next_flag = True
                bmb_cnt = 1
                cur_value = field[ny][nx]
            else:
                bmb_cnt+=1
            st.append((ny,nx))
            if((ny == 0 and nx == 0)):
                flag = True
                break

        if(flag) : break

        dir = (dir+1)%4
        cnt+=1
        if(cnt==2):
            cnt = 0 
            length += 1

    return next_flag


def move(): # O(2N^2)
    global N
    ny = N//2
    nx = N//2
    exists = deque([])
    length = 1
    flag = False
    
    cnt = 0
    dir = 0
    while(1):
        for _ in range(length):
            ny, nx = ny + mv[dir][0], nx + mv[dir][1]
            if(field[ny][nx] != 0):
                exists.append(field[ny][nx])
                field[ny][nx] = 0
            if ny == 0 and nx == 0:
                flag = True
                break
        
        if(flag): break
        
        cnt +=1
        dir = (dir+1)%4
        if(cnt == 2):
            cnt = 0 
            length += 1

    tmp_y = N//2 
    tmp_x = N//2 
    dir = 0 
    cnt = 0
    length = 1
    while(exists):
        for _ in range(length):
            tmp_y, tmp_x = tmp_y + mv[dir][0], tmp_x + mv[dir][1]
            field[tmp_y][tmp_x] = exists.popleft()
            if(not exists):
                return
        cnt += 1
        dir = (dir+1)%4
        if(cnt == 2 ):
            cnt = 0
            length +=1

    return

def change(): #O(O^2)

    global N
    y, x = N//2, N//2
    change = deque([])
    length = 1
    dir = 0
    cnt = 0 
    cur_value = field[N//2 + mv[dir][0]][N//2 + mv[dir][1]]
    cur_cnt = 0
    flag = False
    res = deque([])
    while(1):
        for _ in range(length):
            y, x = y + mv[dir][0], x + mv[dir][1]
            if(field[y][x] != cur_value):
                res.append(cur_cnt)   
                res.append(cur_value)   
                cur_cnt = 1
                cur_value = field[y][x]
            else:
                cur_cnt +=1
            field[y][x] = 0
            if(y==0 and x ==0):
                flag = True
                break
        if(flag or len(res)>= N**2): break
        
        dir = (dir+1) % 4
        cnt += 1
        if(cnt ==2):
            cnt = 0 
            length+=1
    y, x = N//2, N//2
    dir, cnt = 0, 0
    length = 1 
    flag = False
    while(1):
        for _ in range(length):
            y, x = y + mv[dir][0], x + mv[dir][1]
            if res:
                field[y][x] = res.popleft()
                if(y==0 and x == 0):
                    flag = True
                    return
            else:
                flag = True
                break
        if(flag):break
        cnt+=1
        dir = (dir+1)%4
        if(cnt==2):
            cnt = 0
            length +=1 
    return

# print()
# blizzard(1,2) ok 
# move() good
# bomb()


for i in range(M):
    d, s = orders[i]
    blizzard(d-1,s)
    move()
    while(bomb()):
        move()
    change()

ret = 0
for i in range(1,4):
    ret += i*bomb_cnt[i]
print(ret)



# print(bomb_cnt)
# 0 : first -> numbering 
# 1 : bomb
# 2 : move 
# 3 : 만약 어떤 칸 A의 번호보다 번호가 하나 작은 칸이 빈 칸이면,
# 4 : 
# A에 있는 구슬은 그 빈 칸으로 이동한다. 
# 이 이동은 더 이상 구슬이 이동하지 않을 때까지 반복된다. 
