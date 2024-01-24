#Create a program which verify that a node is balanced

class Node():
  def __init__(self,value,name='default'):
    self.name=name
    self.value=value
    self.left=None
    self.right=None
  def __str__(self):
    return self.name

def height(node):
  if node is None:
    return 0
  return max(height(node.left),height(node.right))+1
def is_balanced(node):
  if node is None:    
    yield True
  try:
    if next(is_balanced(node.right)) and next(is_balanced(node.left)) and abs(height(node.left)-height(node.right))<=1:
      str_input=input()
      if str_input=='q':
        return 'END'
      print(node)
      yield True
    yield False
  except StopIteration as e:
    return e.value

if __name__=='__main__':
  root=Node(0,'0')
  node_1=Node(1,'1')
  node_2=Node(1,'2')
  node_3=Node(1,'3')
  node_4=Node(1,'4')
  node_5=Node(1,'5')
  node_6=Node(1,'6')
  node_7=Node(1,'7')
  node_8=Node(1,'8')

  root.left=node_1
  root.right=node_2
  node_1.left=node_3
  node_2.left=node_4
  node_3.left=node_5
  node_4.left=node_6
  gen=is_balanced(root)
  try:
    next(gen)
  except StopIteration as e:
    print(e.value)

  # print(f"Height root {height(root)}")
  # print(f"Height node 1 {height(node_1)}")
  # print(f"Height node 3 {height(node_3)}")
  # print(is_balanced(root))
  