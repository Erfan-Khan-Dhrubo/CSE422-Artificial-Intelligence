with open('Input file.txt', 'r') as file:
    lines = file.readlines()  # Making the textfile into array
    stored_graph = {}
    for i, line in enumerate(lines):
        s = line.strip()  # removing newline
        data = s.split()  # splitting line into array

        stored_graph[data[0]] = [int(data[1])]  # setting the location and heuristic value
        for j in range(2, len(data), 2):
            stored_graph[data[0]].append(
                [data[j], int(data[j + 1])])  # setting the city and distance ase list in the value


def a_star_search(graph, start, destination):
    open_list = [[start, 0, [start]]]
    visited = []

    while len(open_list) > 0:

        smallest_node = open_list[0]  # assuming the 1st index as smallest node
        for node in open_list:
            node_cost = node[1] + graph[node[0]][0]  # total_distance + heuristic value
            smallest_cost = smallest_node[1] + graph[smallest_node[0]][
                0]  # present smallest node total_distance + heuristic value
            if node_cost < smallest_cost:
                smallest_node = node

        open_list.remove(smallest_node)
        current_node, total_cost, Path = smallest_node

        if current_node == destination:
            return Path, total_cost

        visited.append(current_node)  # tracking the visiting node

        neighbors = graph[current_node][1:]  # storing all the neighbors and there distance
        for neighbor in neighbors:
            neighbor_name, distance = neighbor
            if neighbor_name not in visited:
                new_cost = total_cost + distance  # total distance from stating node
                new_path = Path + [neighbor_name]  # path from the starting node
                open_list.append([neighbor_name, new_cost, new_path])

    return "NO PATH FOUND", 0


start_node = input("Start node: ").strip()
destination_node = input("Destination: ").strip()

path, total_distance = a_star_search(stored_graph, start_node, destination_node)
if path == "NO PATH FOUND":
    print(path)
else:
    print(f"Path: {' -> '.join(path)}")
    print(f"Total distance: {total_distance} km")