from sys import stdin, setrecursionlimit
setrecursionlimit(int(1e5))

N = int(input())


MAP = []


def isValid(ny:int, nx:int, N):
    if ny < 0  or nx < 0 or ny >= N or nx >= N:
        return False
    
    if MAP[ny][nx]==1:
        return False

    return True

def dfs(y,x, direction, N):
    if x == N-1 and y == N-1:
        return 1


    res = 0

    # 가로로 이동하기 0 : 가로 0, 대각선 2로부터
    if direction == 0 or direction == 2:
        new_y, new_x = y, x+1
        if isValid(new_y, new_x, N):
            res += dfs(new_y, new_x, 0, N)

    # 세로로 이동하기 1 : 세로 1, 대각선 2로부터 
    if direction == 1 or direction == 2:
        new_y, new_x = y+1, x
        if isValid(new_y, new_x, N):
            res += dfs(new_y, new_x, 1, N)

    new_y, new_x = y+1, x+1
    if isValid(new_y, new_x, N) and isValid(y+1,x,N) and isValid(y,x+1,N):
        res += dfs(new_y, new_x, 2, N)
    # 대각선으로 이동하기 2 : 모든 방향에서 가능
    # 대각선 : direction 상관없이 전부

    return res

MAP = [list(map(int,input().split())) for _ in range(N)]
res = dfs(0,1,0,N)
print(res)
