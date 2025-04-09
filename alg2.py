# alg2.py
import heapq

def find_cheapest_delivery(n, routes, src, dst, k):
    graph = {i: [] for i in range(n)}
    for u, v, price in routes:
        graph[u].append((v, price))

    # (cost, current_node, stops)
    heap = [(0, src, 0)]
    visited = {}

    while heap:
        cost, node, stops = heapq.heappop(heap)

        if node == dst:
            return cost

        if stops > k or (node in visited and visited[node] <= stops):
            continue
        visited[node] = stops

        for neighbor, price in graph[node]:
            heapq.heappush(heap, (cost + price, neighbor, stops + 1))

    return -1
