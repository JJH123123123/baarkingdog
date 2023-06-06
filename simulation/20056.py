from collections import deque
from math import floor
from sys import stdin
input = stdin.readline


mv = [[-1,0],[-1,1],[0,1],[1,1],[1,0], [1,-1],[0,-1],[-1,-1]]
N, M, K = map(int,input().split())
field = [[ deque([]) for _ in range(N)] for j in range(N)]
fireball = deque([])
for _ in range(M):
    r,c,m1,s1,d1 = map(int,input().split())
    r-=1
    c-=1
    field[r][c].append([m1,s1,d1])
    fireball.append([r,c])
# print(fireball)
# for row in field:
#     print(*row)

# 둘째 줄부터 M개의 줄에 파이어볼의 정보가 한 줄에 하나씩 주어진다. 파이어볼의 정보는 다섯 정수 ri, ci, mi, si, di로 이루어져 있다.
# 마법사 상어가 크기가 N×N인 격자에 파이어볼 M개를 발사했다.
# 가장 처음에 파이어볼은 각자 위치에서 이동을 대기하고 있다. i번 파이어볼의 위치는 (ri, ci), 질량은 mi이고, 방향은 di, 속력은 si이다. 위치 (r, c)는 r행 c열을 의미한다.

# 관건은 
# 파이어볼은 4개의 파이어볼로 나누어진다.
# 나누어진 파이어볼의 질량, 속력, 방향은 다음과 같다.
# 질량은 ⌊(합쳐진 파이어볼 질량의 합)/5⌋이다.
# 속력은 ⌊(합쳐진 파이어볼 속력의 합)/(합쳐진 파이어볼의 개수)⌋이다.
# 합쳐지는 파이어볼의 방향이 모두 홀수이거나 모두 짝수이면, 방향은 0, 2, 4, 6이 되고, 그렇지 않으면 1, 3, 5, 7이 된다.
# 질량이 0인 파이어볼은 소멸되어 없어진다.

# 움직인다. 움직이면서 겹치면 합친다. 
# 겹치면 4개를 나눠서 넣는다. 
# 움직임, 충돌을 배열로 어떻게 구현하면 깔끔할까
 


def Move():
    # move 
    while fireball:
        y, x = fireball.popleft()
        m, s, d = field[y][x].popleft()

        ny, nx = (y + s*mv[d][0])%N, (x + s*mv[d][1]) % N
        field[ny][nx].append([m,s,d])

    # print(new_fireball)
    for i in range(N):
        for j in range(N):
            if(len(field[i][j])>=2):
                sum_mass = 0
                sum_speed = 0
                odd = 0
                even = 0
                fireball_cnt = len(field[i][j])
                # print(fireball_cnt)
                while(field[i][j]):
                    m,s,d = field[i][j].popleft()
                    sum_mass +=   m 
                    sum_speed +=  s
                    if(d%2!=0):        
                        odd += 1
                    else:
                        even += 1

                sum_mass = sum_mass//5
                # print(even, odd, fireball_cnt)
                if(sum_mass<=0): continue
                sum_speed = sum_speed//fireball_cnt
                # field[i][j] = deque([]) # delete 
                if((even == fireball_cnt or odd == fireball_cnt)): # 1 3 5 7
                    for dir in range(0,8,2):
                        field[i][j].append([sum_mass,sum_speed, dir])
                        fireball.append([i,j])
                else:
                    for dir in range(1,8,2):
                        field[i][j].append([sum_mass,sum_speed, dir])
                        fireball.append([i,j])
            elif len(field[i][j])==1:
                fireball.append([i,j])
    return

def check():
    ret = 0    
    for i in range(N):
        for j in range(N):
            if(field[i][j]):
                for fireball in field[i][j]:
                    ret += fireball[0]
    print(ret)
    return

cnt = 0
while(K>0):
    Move()
    K-=1
check()