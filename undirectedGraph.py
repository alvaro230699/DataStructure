graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F", "G"],
    "F": ["C", "E"],
}


def find_path(graph, initial, target):
    assert isinstance(initial, str) and isinstance(target, str)
    seen_nodes = {}
    nodes_to_explore = []
    path_dict = {}
    pointer = initial
    result = None
    is_all_nodes_seen = False
    while result is None and not is_all_nodes_seen:
        if pointer in seen_nodes:
            pointer = nodes_to_explore.pop(0)
            continue
        seen_nodes[pointer] = True
        is_all_nodes_seen = len(seen_nodes) == len(graph)
        result = breadth_first_search_per_graph(
            graph, pointer, target, nodes_to_explore, path_dict, seen_nodes
        )
        pointer = nodes_to_explore.pop(0)
    if is_all_nodes_seen and not result:
        raise ValueError("target was not in the initial graph")
    return " -> ".join(([target] + path_dict[target])[::-1])


def breadth_first_search_per_graph(
    graph, node, target, nodes_to_explore: list, path_dict: dict, seen_nodes: dict
):
    neighbors = graph[node]
    for neighbor in neighbors:
        if neighbor in seen_nodes:
            continue
        if node in path_dict:
            current_path = path_dict[node]
            path_dict[neighbor] = [node] + current_path
        else:
            path_dict[neighbor] = [node]
        if neighbor == target:
            return neighbor
        nodes_to_explore.append(neighbor)
    return None


if __name__ == "__main__":
    print(find_path(graph, "A", "G"))
