---
layout: post
title: 'chapter 13 복습'
date: 2020-10-14
category: practice
---
## 15번 문제 :특정 거리의 도시 찾기
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
