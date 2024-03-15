import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0
        self.h = 0

    def __lt__(self, other):
        return (self.g + self.h) < (other.g + other.h)

def astar(graph, start, goal):
    open_list = []
    closed_list = set()

    start_node = Node(start)
    goal_node = Node(goal)

    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)

        if current_node.position == goal_node.position:
            path = []
            while current_node is not None:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]

        closed_list.add(current_node.position)

        for neighbor in graph[current_node.position]:
            if neighbor in closed_list:
                continue

            neighbor_node = Node(neighbor, parent=current_node)
            neighbor_node.g = current_node.g + 1
            neighbor_node.h = abs(neighbor[0] - goal[0]) + abs(neighbor[1] - goal[1])  # Manhattan distance

            for node in open_list:
                if neighbor_node.position == node.position and neighbor_node.g >= node.g:
                    break
            else:
                heapq.heappush(open_list, neighbor_node)

    return None

graph = {
    (0, 0): [(0, 1), (1, 0)],
    (0, 1): [(0, 0), (1, 1)],
    (1, 0): [(0, 0), (1, 1)],
    (1, 1): [(0, 1), (1, 0)]
}

start = (0, 0)
goal = (1, 1)

path = astar(graph, start, goal)

if path:
    print("Path from", start, "to", goal, ":", path)
else:
    print("No path found")
