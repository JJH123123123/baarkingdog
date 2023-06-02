
# from functools import itemgetter
from sys import stdin
input = stdin.readline
n = int(input())

likes = dict()
school = [[0 for i in range(n)] for j in range(n)]
student = [i for i in range(1,n*n+1)]

for number in range(1,1+n*n):
    tmp = list(map(int,input().split()))
    likes[tmp[0]] = tmp[1:]


mv = [[0,1],[0,-1],[1,0],[-1,0]]


def findLikeMost(to_student):
    # 4 * n^2 
    place = None
    max_cnt = 0
    possbile_place = []
    
    # 1 
    for i in range(n):
        for j in range(n):
            if(school[i][j]!=0): continue
            cnt_target = 0
            for l in range(4):
                ny, nx = i + mv[l][0], j + mv[l][1]
                if(0>ny or 0>nx or ny>=n or nx>=n): continue
                
                if(school[ny][nx] in likes[to_student]):
                    cnt_target +=1
                
            if(max_cnt<cnt_target):
                possbile_place = [(i,j)]
                max_cnt = cnt_target
            elif max_cnt == cnt_target:
                possbile_place.append((i,j))
    
    if len(possbile_place)==1:
        return possbile_place[0]
    
    # 2 
    empty_place = dict()
    for i in range(4+1):
        empty_place[i] = []

    for possible in possbile_place:
        y, x = possible
        cnt = 0
        for dir in range(4):
            ny, nx = possible[0] + mv[dir][0], possible[1] + mv[dir][1]
            if(0>ny or 0>nx or ny>=n or nx>=n): continue
            if(school[ny][nx]==0):
                cnt+=1

        empty_place[cnt].append(possible)

    current = []
    for i in range(4,-1,-1):
        if(empty_place.get(i,0)):
            current = empty_place[i]
            break
    
    if(len(current)==1):
        return current[0]
    

    # 3 

    current.sort()
    return current[0]


# 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
# 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
# 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.
# 한 칸에는 학생 한 명의 자리만 있을 수 있고, |r1 - r2| + |c1 - c2| = 1을 만족하는 두 칸이 (r1, c1)과 (r2, c2)를 인접하다고 한다.

# print(likes)

for item in likes.keys():
    # print()
    # print(item,'\n')

    i, j = findLikeMost(item)
    school[i][j] = item
    # for row in school:
    #     print(*row)
    # print(i,j)


total = 0

for i in range(n):
    for j in range(n):

        Like_list = likes[school[i][j]]
        cnt = 0
        for dir in range(4):
            ny, nx = mv[dir][0] + i , mv[dir][1] + j 
            if(0>ny or 0>nx or ny>=n or nx>=n): continue
            
            if school[ny][nx] in Like_list:
                cnt+=1
        
        if(cnt==0):
            continue
        total+= pow(10, cnt-1)
print(total)
