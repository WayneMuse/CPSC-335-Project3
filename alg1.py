from collections import deque
def spread_of_fire(forest):
    if not forest:
        return -1

    rows, cols = len(forest), len(forest[0])
    queue = deque()
    healthy_trees = 0
    days = 0
    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    for r in range(rows):
        for c in range(cols):
            if forest[r][c] == 2:
                queue.append((r, c, 0))  
            elif forest[r][c] == 1:
                healthy_trees += 1


    if healthy_trees == 0:
        return 0
    if not queue:
        return -1

    while queue:
        r, c, d = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and forest[nr][nc] == 1:
                forest[nr][nc] = 2
                healthy_trees -= 1
                queue.append((nr, nc, d + 1))
                days = d + 1

    return days if healthy_trees == 0 else -1