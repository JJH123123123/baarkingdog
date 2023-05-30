N, M, y, x, K = map(int, input().split())
MAP = []
for _ in range(N):
    MAP.append(list(map(int, input().split())))
COM = list(map(int, input().split()))

dice = [0]*6
# 처음: 위 아래  왼 오  앞 뒤  
# 처음: 0  1   2  3  4 5
# 오 : 왼  앞    위   아래 뒤 오(o)
# 왼 : 오  앞    아래  위  뒤 왼
# 위 : 뒤  위    오   왼  아래 앞
# 뒤 : 앞  아래  오   왼  위  뒤


flip_data = [[4, 5, 2, 3, 1, 0],
             [5, 4, 2, 3, 0, 1],
             [3, 2, 0, 1, 4, 5],
             [2, 3, 1, 0, 4, 5]]
dx = [1, -1 , 0, 0]
dy = [0, 0, -1, 1]
for i in COM:
    i-=1
    x+=dx[i]
    y+=dy[i]
    # print(x,y, N,M)
    if not 0<=x<M or not 0<=y<N:
        x-=dx[i]
        y-=dy[i]
        continue

    temp = [0]*6
    for j in range(6):
        temp[j] = dice[flip_data[i][j]]
    dice = temp
    print(dice)
    if MAP[y][x] == 0:
        MAP[y][x] == dice[1]
    else:
        dice[1] = MAP[y][x]
        MAP[y][x] = 0