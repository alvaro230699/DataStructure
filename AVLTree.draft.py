# # BINARY TREE SEARCH - Left less value, right higher values
# class AVLTree2:
#     def __init__(self, value) -> None:
#         self.root = Node(value)

#     @staticmethod
#     def appendNodes(nodeParent, nodeChild, newNode, node_type):
#         if nodeChild is None:
#             if node_type == "right":
#                 nodeParent.right = newNode
#             else:
#                 nodeParent.left = newNode
#         if nodeChild.value >= newNode.value:
#             AVLTree2.appendNodes(nodeChild, nodeChild.right, newNode, "right")

#     def insert(self, node: Node):
#         current_height = self.root.height
#         if current_height == 1:
#             if node.value >= self.root.value:
#                 self.root.right = node
#             else:
#                 self.root.left = node
#         else:
#             if node.value > self.root.value:
#                 ...
#                 # append
#         ...

#     # def
