
from sys import stdin
from collections import deque 
input = stdin.readline


N = int(input())
graph = [[] for _ in range(N)]
pops = list(map(int,input().split()))

for i in range(N):
    size, *nums = map(int,input().split())
    while(nums):
        graph[i].append(nums.pop() -1)

def bfs1(first, vis, mask):
    deq = deque([first])
    while deq:
        cur = deq.popleft()
        vis[cur] = True
        for next_idx in graph[cur]:
            if(vis[next_idx] or (mask & (1<<next_idx))): continue
            deq.append(next_idx)
    return

def bfs2(first, vis, mask):
    deq = deque([first])
    while deq:
        cur = deq.popleft()
        vis[cur] = True
        for next_idx in graph[cur]:
            if(vis[next_idx] or not (mask & (1<<next_idx))): continue
            deq.append(next_idx)
    return


def SOLVE(mask):

    ans = 1101010110031013

    for mask in range((1<<N)):
        vis = [False for i in range(N)]
        cnt1 = cnt2 = 0
        for i in range(N):
            if (mask & (1<<i)):
                if not vis[i]:
                    bfs2(i, vis, mask)
                    cnt1+=1
            else:
                if not vis[i]:
                    bfs1(i, vis, mask)
                    cnt2+=1

        cnt = vis.count(True)
        if( cnt == N and (cnt1 == cnt2 == 1 )):
            sF = sS = 0
            for i in range(N):
                if((mask & (1<<i))): sF += pops[i]
                else: sS += pops[i]
            ans = min(ans, abs(sF-sS))

    if(ans == 1101010110031013): 
        print(-1)
        return
    print(ans)

SOLVE(N)