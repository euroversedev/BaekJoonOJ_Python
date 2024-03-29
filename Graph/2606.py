import sys
sys.setrecursionlimit(10**9)

N = int(input())
graph = [[] for _ in range(N+1)]

M = int(input())
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)
def dfs(i):
    visited[i] = True
    
    for j in graph[i]:
        if visited[j] == False:
            visited[j] = True
            dfs(j)
    
dfs(1)
print(sum(visited) -1)