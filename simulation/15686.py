from itertools import combinations as combi
from sys import stdin
input = stdin.readline

N, M = map(int,input().split())
field = []
chi = [] # y,x for fried chicken store 
home = []
for i in range(N):
    field.append(list(map(int,input().split())))

    for j in range(N):
        if(field[i][j] == 2):
            chi.append((i,j))
        elif (field[i][j]== 1):
            home.append((i,j))

ret = 1301030130101031
for possible in combi(chi,M): # O(13C6) : max
    tmp_ret = 0
    for target in home: # O(100)
        tmp = 3013013031031010
        home_y, home_x = target
        for chicken in possible:
            chicken_y, chicken_x = chicken

            # calculating of Manhattan distance
            tmp = min(tmp, abs(chicken_y-home_y)+abs(chicken_x-home_x))
        tmp_ret += tmp
    # updating min_sum of distance 
    ret = min(ret, tmp_ret)
print(ret)


    # update min
