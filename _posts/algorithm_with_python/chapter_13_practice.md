---
layout: post
title: 'chapter 13 복습'
date: 2020-10-14
category: practice
---
## 15번 문제 : 특정 거리의 도시 찾기
```python
# 특정 거리의 도시  찾기
# n개의 도시, m개의 도로
# 특정 도시 x로부터 출발하여 도달할 수 있는 모든 도시 중에서, 최단 거리가 정확히 k인 모든 도시를 출력하는 프로그램 작성

# 입력 -> 각 도시의 최단 거리를 나타내는 리스트 생성 -> 그래프를 순회하면서(bfs) 최단거리 갱신 -> 최단거리가 k인 도시 출력하는
from collections import deque


n, m, k, x = map(int, input().split()) 
graph = [[] * (n + 1) for _ in range(n + 1)] # 그래프 생성

# 그래프 입력(linked graph)
for _ in range(m):
  start, end = map(int, input().split())
  graph[start].append(end)

# 최단 거리 정보를 담는 리스트
dist = [1e9] * (n + 1)

def bfs(start):
  q = deque()
  distance = 0
  dist[start] = distance
  q.append(start)
  
  while q:
    
    distance += 1
    
    for _ in range(len(q)):
      start = q.popleft()
      
      for i in graph[start]:
        dist[i] = min(dist[i], distance)
        q.append(i)
        
bfs(x)

result = False

for idx, value in enumerate(dist):
  if value == k:
    result = True
    print(idx)

if not result:
  print(-1)
```
## 16번 문제 : 연구소
```python
# 연구소
# 바이러스 유출 -> 막기위해서 연구소에 벽을 세움
# n* m 의 크기의 연구소, 빈칸 or 벽으로 나뉘어져있음
# 일부 칸에 바이러스 존재, 바이러스는 상하좌우로 퍼져나감

# 연구소의 지도가 주어졌을 떄 얻을 수 있는 안전 영역 크기의 최대값을 구하는 프로그램 작성

# 입력 -> 벽을 세우고 -> 바이러스 퍼트리고 -> 안전 영역 크기 계싼
from collections import deque
import copy


n, m = map(int, input().split())

lab = [list(map(int, input().split())) for _ in range(n)] # 연구소 입력
temp = [[0] * m for _ in range(n)]
result = 0

def get_score():
  result = 0
  for i in range(n):
    for j in range(m):
      if temp[i][j] == 0:
        result += -1
        
  return result

def virus(x, y):
  q = deque()
  q.append((x, y))
  dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
  
  while q:
    x, y = q.popleft()
    
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      
      if nx >= n or ny >= m or nx < 0 or ny < 0:
        continue
      
      if temp[nx][ny] == 0:
        q.append((nx, ny))
        temp[nx][ny] = 2

def dfs(count):
  global result
  if count == 3:
    for i in range(n):
      for j in range(m):
        temp[i][j] = lab[i][j]
    
    for i in range(n):
      for j in range(m):
        if temp[i][j] == 2:
          virus(i, j)
          
    result = max(get_score(), result)
    return
  
  for i in range(n):
    for j in range(m):
      if lab[i][j] == 0:
        lab[i][j] = 1
        count += 1
        dfs(count)
        lab[i][j] = 0
        count -= 1
        
dfs(0)
print(result)
```
