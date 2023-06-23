from sys import stdin
input = stdin.readline

N = int(input())

# 드래곤 
# 0 : ->, 1 : up, 2 : left, 3 : down
mv = [[0,1],[-1,0],[0,-1],[1,0]]
# 1 ++ -> 반시계
def find_dir(d,g):
    moves = [d]
    for i in range(g):
        tmp = []

        for j in range(len(moves)):
            tmp.append((moves[-j-1]+1)%4)
        moves.extend(tmp)
        print(moves)
    return moves
check = [[0 for _ in range(101)] for __ in range(101)]


for _ in range(N):
    x,y,d,g = map(int,input().split())
    dic_list = find_dir(d,g)

    check[y][x] = 1
    ny, nx = y, x
    for dir in dic_list:
        ny, nx = ny + mv[dir][0], nx + mv[dir][1]
        check[ny][nx] = 1
    # print(dic_list,g)
    
cnt = 0
for i in range(100):
    for j in range(100):
        if check[i][j] and check[i][j+1] and check[i+1][j] and check[i+1][j+1]:
            cnt+=1
print(cnt)