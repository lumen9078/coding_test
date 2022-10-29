from sys import stdin
input = stdin.readline

def dfs(graph, start, visited):
    visited[start] = True
    cnt = 0

    for i in graph[start]:
        if not visited[i]:
            cnt += 1
            cnt += dfs(graph, i, visited)

    return cnt

T = int(input())

for _ in range (T):
    N, M = map(int, input().split())
    graph = [[] for i in range(N + 1)]
    visited = [False for i in range(N + 1)]

    for i in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    print(dfs(graph, 1, visited))