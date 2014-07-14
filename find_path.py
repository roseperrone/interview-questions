'''
Find a path from one node in a graph to another

Input:
  graph = {1: [2, 3],
           2: [3, 4],
           3: [4],
           4: [3],
           5: [6],
           6: [3]}
  graph, 1, 4
Output:
  [1, 2, 3, 4] 

'''

graph = {1: [2, 3],
         2: [3, 4],
         3: [4],
         4: [3],
         5: [6],
         6: [3]}

def find_path(graph, start, end, path=[]):
    path.append(start)
    if start == end:
        return path
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath:
                return newpath

def find_all_paths(graph, start, end, path=[]):
    if start == end:
        return [path]
    if not graph.has_key(start):
        # it's a dead-end
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, paths)
            paths.append(newpaths)
    return paths

assert find_path(graph, 1, 4) == [1, 2, 3, 4]
