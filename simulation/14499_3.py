
from sys import stdin
input = stdin.readline

N, M, x, y, order = map(int,input().split())

# N, M: 지도의 세로, 가로 
# x, y: 행, 열

field = [] 

for i in range(N):
    field.append(list(map(int,input().split())))


# 처음: 위 아래  왼 오  앞 뒤  
# 처음: 0  1   2  3  4  5 
# 오 : 왼 오  아래 위  4  5 
# 왼 : 오 왼  위 아래     
# 북(위) : 뒤 앞   왼 오 위 아래
# 남(뒤): 앞 뒤 왼오 아래 위


dice = [0] * 6 
dice_moves = [
           [2,3,1,0,4,5],
           [3,2,0,1,4,5],
           [5,4,2,3,0,1],
           [4,5,2,3,1,0]
        ]



orders = list(map(int,input().split()))

#     동, 서, 북, 남
dx = [0,0,-1,1]
dy = [1,-1,0,0] 

for cmd in orders:
    # print(dice[1]) # 위 출력
    nx, ny = x + dx[cmd-1], y + dy[cmd-1]
    if( (0>ny) or (0>nx) or  (M<=ny) or (N<=nx) ): continue

    tmp = [0] * 6
    for index, idx in enumerate(dice_moves[cmd-1]):
        tmp[index] = dice[idx]
    dice = tmp 
    
    if dice[1] == 0:
        field[nx][ny], dice[1] = 0, field[nx][ny]
    else:
        dice[1], field[nx][ny] = field[nx][ny],0
    # print(tmp)
    print(dice[0])
    y, x = ny, nx


# 주사위는 지도의 바깥으로 이동시킬 수 없다. 만약 바깥으로 이동시키려고 하는 경우에는 해당 명령을 무시해야 하며, 출력도 하면 안 된다.
# => 예외처리

# 가장 처음에 주사위에는 모든 면에 0이 적혀져 있다.
# 지도의 각 칸에는 정수가 하나씩 쓰여져 있다. 주사위를 굴렸을 때, 이동한 칸에 쓰여 있는 수가 0이면, 
# 주사위의 바닥면에 쓰여 있는 수가 칸에 복사된다. 0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며, 칸에 쓰여 있는 수는 0이 된다.
# => 작동원리 

# 마지막 줄에는 이동하는 명령이 순서대로 주어진다. 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4로 주어진다.
# => 각 1, 2, 3, 4에 대한 rotation
