import unittest


class Node:
    def __init__(self, value, height=1):
        self.value = value
        self.height = height
        self.left = None
        self.right = None

    # TODO: How calculate height and how could optmize when I rotate nodes. Review getters and setters in python chatGPT
    @property
    def height(self):
        left_height = self.left.height if self.left else -1
        right_height = self.right.height if self.right else -1
        return max(left_height, right_height) + 1

    @height.setter
    def height(self, height):
        self._height = height

    def __str__(self) -> str:
        return str(self.value)


class AVLTree:
    def __init__(self, root: Node = None) -> None:
        self.root = root

    def _insert(self, root: Node, new_node):
        if not isinstance(new_node, Node):
            new_node = Node(value=new_node)
        if not root:
            return new_node
        # Here we could change the behavior of where the
        # equals node could be gone
        elif root.value <= new_node.value:
            root.right = self._insert(root.right, new_node)
        else:
            root.left = self._insert(root.left, new_node)
        root = self.balance_tree(root)
        return root

    def balance_tree(self, node: Node):
        if self._is_balanced(node):
            return node
        # Verify if the tree is balanced
        balance = self.check_balance(node)
        # Balance data
        # TODO: Check case to insert 10,5 and then 8.
        try:
            # unbalanced in right side
            if balance < -1:
                right_child = node.right
                left_weight = right_child.left.height if right_child.left else -1
                right_weight = right_child.right.height if right_child.right else -1
                # Make RL Rotation
                if left_weight > right_weight:
                    node.right = self.right_rotation(right_child)
                    right_child = node.right
                # Otherwise make Left Rotation
                node = self.left_rotation(node)
            # unbalanced in left side
            elif balance > 1:
                left_child = node.left
                left_weight = left_child.left.height if left_child.left else -1
                right_weight = left_child.right.height if left_child.right else -1
                # Make LR Rotation
                if right_weight > left_weight:
                    node.left = self.left_rotation(left_child)
                    left_child = node.left
                # Otherwise make Right Rotation
                node = self.right_rotation(node)
            self.balance_tree(node)
            return node
        except ValueError as e:
            print(f"Error: {e}")

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
            return
        self.root = self._insert(self.root, value)

    def check_balance(self, root: Node):

        l_height = root.left.height if root.left else -1
        r_height = root.right.height if root.right else -1
        return l_height - r_height

    def has_both_childs(self, node: Node):
        return node.right and node.left

    # Modify to insert the non parents nodes
    def right_rotation(self, node: Node):
        new_parent_node = node.left
        if new_parent_node is None:
            raise ValueError(f"Left node should not be empty in {node}")
        node.left = None
        old_right_child_node = new_parent_node.right
        new_parent_node.right = node
        if old_right_child_node:
            new_parent_node = self._insert(new_parent_node, old_right_child_node)
        return new_parent_node

    # Modify to insert the non parents nodes
    def left_rotation(self, node: Node):
        new_parent_node = node.right
        if new_parent_node is None:
            raise ValueError(f"Right node should not be empty in {node}")
        node.right = None
        old_left_child_node = new_parent_node.left
        new_parent_node.left = node
        if old_left_child_node:
            new_parent_node = self._insert(new_parent_node, old_left_child_node)
        return new_parent_node

    def is_balanced(self):
        return self._is_balanced(self.root)

    def _is_balanced(self, node):
        balance = self.check_balance(node)
        return balance in (-1, 0, 1)


class TestAVLTree(unittest.TestCase):
    def test_insertion(self):
        avl = AVLTree()
        avl.insert(10)
        avl.insert(5)
        avl.insert(15)
        avl.insert(3)
        avl.insert(8)
        avl.insert(12)
        avl.insert(20)
        # Check if tree maintains AVL properties after insertions
        self.assertTrue(avl.is_balanced())
        # Add more tests for insertion if needed

    def test_left_side_balance(self):
        avl = AVLTree(Node(10))
        avl.insert(5)
        avl.insert(8)
        avl.insert(7)
        avl.insert(12)
        self.assertTrue(avl.is_balanced())

    def test_double_rotation(self):
        avl = AVLTree()
        avl.insert(10)
        avl.insert(5)
        avl.insert(15)
        avl.insert(3)
        avl.insert(8)
        avl.insert(12)
        avl.insert(20)
        avl.insert(2)
        avl.insert(4)

        # Before double rotation
        # Tree should look like:
        #            10
        #          /    \
        #         5      15
        #        / \    / \
        #       3   8  12  20
        #      / \
        #     2   4

        # Now let's insert a node that causes a double rotation
        avl.insert(1)

        # After double rotation
        # Tree should look like:
        #            10
        #          /    \
        #         3      15
        #        / \    / \
        #       2   5  12  20
        #      /   / \
        #     1   4   8

        # Check if tree maintains AVL properties after double rotation
        self.assertTrue(avl.is_balanced())

        # Check if the tree structure is correct after double rotation
        self.assertEqual(avl.root.value, 10)

        self.assertEqual(avl.root.left.value, 3)
        self.assertEqual(avl.root.right.value, 15)

        self.assertEqual(avl.root.left.left.value, 2)
        self.assertEqual(avl.root.left.right.value, 5)

        self.assertEqual(avl.root.right.right.value, 20)
        self.assertEqual(avl.root.right.left.value, 12)

        self.assertEqual(avl.root.left.left.left.value, 1)

        self.assertEqual(avl.root.left.right.left.value, 4)
        self.assertEqual(avl.root.left.right.right.value, 8)
        self.assertEqual(avl.root.right.right.value, 20)
        self.assertEqual(avl.root.right.left.value, 12)

    def test_equals_values(self):
        avl = AVLTree()
        avl.insert(10)
        avl.insert(5)
        avl.insert(15)
        avl.insert(3)
        avl.insert(8)
        avl.insert(12)
        avl.insert(20)
        avl.insert(2)
        avl.insert(4)

        # Before double rotation
        # Tree should look like:
        #            10
        #          /    \
        #         5      15
        #        / \    / \
        #       3   8  12  20
        #      / \
        #     2   4

        # Now let's insert a node that causes a double rotation
        avl.insert(1)
        avl.insert(0)
        avl.insert(5)

        # After double rotation
        # Tree should look like:
        #            5
        #          /   \
        #         3     10
        #        / \    / \
        #       1   4  8  15
        #      / \    /   / \
        #     0   2  5   12 20

        # Check if tree maintains AVL properties after double rotation
        self.assertTrue(avl.is_balanced())

        # Check if the tree structure is correct after double rotation
        self.assertEqual(avl.root.value, 5)

        self.assertEqual(avl.root.left.value, 3)
        self.assertEqual(avl.root.right.value, 10)

        self.assertEqual(avl.root.left.left.value, 1)
        self.assertEqual(avl.root.left.right.value, 4)

        self.assertEqual(avl.root.right.left.value, 8)
        self.assertEqual(avl.root.right.right.value, 15)

        self.assertEqual(avl.root.left.left.left.value, 0)
        self.assertEqual(avl.root.left.left.right.value, 2)

        self.assertEqual(avl.root.right.left.left.value, 5)

        self.assertEqual(avl.root.right.right.left.value, 12)
        self.assertEqual(avl.root.right.right.right.value, 20)


if __name__ == "__main__":
    # TestAVLTree().test_insertion()
    unittest.main()
