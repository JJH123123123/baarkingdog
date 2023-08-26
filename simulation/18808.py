from sys import stdin
input = stdin.readline

n, m, k  = map(int,input().split())


MAP = [[0 for _ in range(m)] for _ in range(n)]
Stickers = []
sticker = []

for __ in range(k):
    row, col = map(int,input().split())
    sticker = [] 
    for _ in range(row):
        cur_row = list(map(int,input().split()))
        sticker.append(cur_row)

    Stickers.append(sticker)
            
# for sticker in Stickers:
#     print(sticker)

# 회전 구현 
from copy import deepcopy as dcpy

def rotate(row,col, arr):
    copy_MAP = [[0 for _ in range(row)] for __ in range(col)]

    for i in range(row):
        for j in range(col):
            copy_MAP[j][row-1-i] = arr[i][j]

    return copy_MAP
    

# 매칭 구현 

def matching(sticker):
    sticker_height = len(sticker)
    sticker_breath = len(sticker[0])
    row, col = -1, -1

    for i in range(n - sticker_height + 1):
        for j in range(m - sticker_breath + 1):
            flag = False
            for hh in range(sticker_height):
                for bb in range(sticker_breath):
                    if(MAP[i+hh][j+bb] and sticker[hh][bb]): # MAP exists and sticker_exist
                        flag = True
                if(flag): break
            
            if(not flag):
                row, col = i,j
                return row,col
    return row,col


def draw(i,j, sticker):
    sticker_height = len(sticker)
    sticker_breath = len(sticker[0])

    for row in range(sticker_height):
        for col in range(sticker_breath):
            if(sticker[row][col]==0):
                continue
            MAP[i + row][j + col] = sticker[row][col]


for idx in range(k):
    cnt = 0
    cur_sticker = dcpy(Stickers[idx])
    while(cnt<4):
        row, col = matching(cur_sticker)
        if( (row,col) != (-1,-1)):
            # print(cnt,row,col)
            draw(row,col,cur_sticker)
            # for R in MAP:
            #     print(*R)
            # print()
            break
        else:
            cur_sticker = rotate(len(cur_sticker), len(cur_sticker[0]), cur_sticker)
            cnt+=1

res = 0
for i in range(n):
    for j in range(m):
        if(MAP[i][j]):
            res+=1
print(res)





