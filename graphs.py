
def dfs(graph,start_node,parent=None,visitors=None):
  if visitors is None:
    visitors=set()
  visitors.add(start_node)
  print(f'visitting {start_node}'+ (f' from {parent}' if parent else ''))
  for neighbor in graph[start_node]:
    if neighbor in visitors:
      print(f"{neighbor} has already visited" + (f' from {start_node}' if start_node else ''))
      continue
    dfs(graph,neighbor,start_node,visitors)

graph={
  'A':['B','C'],
  'B':['C','F'],
  'C':['D','E'],
  'D':['A','B'],
  'E':['F','G'],
  'F':['H'],
  'G':[],
  'H':['A','C'],
}

if __name__=='__main__':
  dfs(graph,'A')