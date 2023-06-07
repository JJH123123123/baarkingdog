
from sys import stdin
input = stdin.readline

N = int(input())
field = [list(map(int,input().split())) for _ in range(N)]

tornado_y, tornado_x = N//2, N//2
ret = 0
# move, check !=0, scatter, if it is out, scattered or not ret+= 

# 1  1 2  2  3  3  4  4  5  5 6  6  7  7 8 8 9  9  10 ...
# 서 남 동 북  서 남 동 북 서 남 동 북  서 남 동 북 서 남 동 북   ...

cur_dir = 0
length = 1 
cnt = 2 
mv = [ [0,-1],[1,0],[0,1], [-1,0]]
ret = 0
def blow(cur_y, cur_x, dir):
    global ret


    five_cor_y, five_cor_x = cur_y + 2*mv[dir][0], cur_x + 2* mv[dir][1]
    sand = field[cur_y][cur_x]
    one = (sand) // 100
    two =  (2 *  sand) // 100
    five = (5 * sand) // 100
    ten =  (10* sand) // 100
    seven =(7 *sand) // 100
    left = sand - 2*(one+seven+ten+two) - five

    if(five_cor_y < 0 or five_cor_x < 0 or five_cor_x >= N or five_cor_y >= N):
        ret += five
    else:
        field[five_cor_y][five_cor_x] += five

    ortho = (dir+1)%4
    ortho_y, ortho_x = mv[ortho][0], mv[ortho][1]
    # plus, 1%, 7%, 10% with 2%
    # cnt 
    coeff = [one,seven,ten]
    cnt = 0
    for y,x in [[cur_y-mv[dir][0], cur_x-mv[dir][1]], [cur_y, cur_x],[cur_y+mv[dir][0], cur_x+mv[dir][1]]]:
        ny, nx, = y - ortho_y, x - ortho_x
        if(cnt==1):
            nny,nnx = ny - ortho_y, nx - ortho_x
            if(nny < 0 or nnx < 0 or nny>= N or nnx >= N):      
                ret += two
            else:
                field[nny][nnx] += two

        if(ny < 0 or nx < 0 or ny>= N or nx >= N): 
            ret += coeff[cnt]
        else:
            field[ny][nx] += coeff[cnt]
        cnt+=1

    cnt = 0
    # minus 1%, 7%, 10% with 2%
    for y,x in [[cur_y-mv[dir][0], cur_x-mv[dir][1]], [cur_y, cur_x],[cur_y+mv[dir][0], cur_x+mv[dir][1]]]:
        ny, nx, = y + ortho_y, x + ortho_x
        if(cnt==1):
            nny,nnx = ny + ortho_y, nx + ortho_x
            if(nny < 0 or nnx < 0 or nny>= N or nnx >= N):     
                ret += two
            else:
                field[nny][nnx] += two

        if(ny < 0 or nx < 0 or ny>= N or nx >= N): 
            ret += (coeff[cnt])
        else:
            field[ny][nx] += (coeff[cnt])
        cnt+=1
    
    ny, nx = cur_y+mv[dir][0], cur_x+mv[dir][1] 
    if(0>ny or 0>nx or ny>=N or nx>=N):
        ret += left
    else:
        field[ny][nx] += left
    field[cur_y][cur_x] = 0
    return

    # %2 


flag = False
while tornado_x!=0 or tornado_y!=0:
    for _ in range(length):
        tornado_y += mv[cur_dir][0]
        tornado_x += mv[cur_dir][1]
        if(tornado_y<0 or tornado_x<0 or tornado_y>=N or tornado_x>=N): break

        if(field[tornado_y][tornado_x]!=0):
            blow(tornado_y,tornado_x,cur_dir)

        if(tornado_y == 0 and tornado_x == 0):
            flag = True
            break
    cnt-=1
    cur_dir = (cur_dir + 1) % 4
    if(cnt==0):
        cnt = 2
        length+=1

print(ret)
