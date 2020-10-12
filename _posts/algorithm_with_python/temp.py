from collections import deque

n, l, r = map(int, input().split())

data = [list(map(int, input()))]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(x, y):
  united = []
  summary = data[x][y] # 연합의 인구 총합
  count = 1 # 연합의 숫자
  q = deque()
  q.append((x, y))
  united.append((x, y))

  while q:
    x, y = q.popleft()

    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]

      if nx >= n or ny >= n or nx < 0 or ny < 0:
        continue

      if l <= abs)data[x]



  
