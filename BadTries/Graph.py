#Create a Deep-First Search

class Graph():
  def __init__(self,node,edge):
    self.node=node
    self.edge=edge
class Node():
  def __init__(self,value):
    self.value=value
  def __str__(self):
    return self.value
class Edge():
  def __init__(self,start_node,end_node,is_directed=False):
    self.start=start_node
    self.end=end_node
    self.is_directed=is_directed
if __name__=='__main__':
  node_a=Node('a')
  node_b=Node('b')
  node_c=Node('c')
  node_d=Node('d')
  edge_a_c=Edge(node_a,node_c)
  edge_a_d=Edge(node_a,node_d)
  edge_a_b=Edge(node_a,node_b)
  edge_b_d=Edge(node_b,node_d)
  edge_c_d=Edge(node_c,node_d)
  graph_a_c=Graph(node_a,edge_a_c)
  graph_a_d=Graph(node_a,edge_a_d)
  graph_a_b=Graph(node_a,edge_a_b)
  graph_c_d=Graph(node_a,edge_c_d)
  graph_b_d=Graph(node_a,edge_b_d)


