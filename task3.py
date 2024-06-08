import heapq

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

def create_graph():
    return {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }

def main():
    graph = create_graph()
    start_vertex = 'A'
    shortest_paths = dijkstra(graph, start_vertex)
    
    for vertex, distance in shortest_paths.items():
        print(f"Відстань від вершини {start_vertex} до вершини {vertex} = {distance}")

if __name__ == "__main__":
    main()