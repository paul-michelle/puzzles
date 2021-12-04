""" Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia:
“The lowest common ancestor is defined between two nodes p and q
as the lowest node in T that has both p and q as descendants
(where we allow a node to be a descendant of itself).”

    Constraints:
    The number of nodes in the tree is in the range [2, 105].
    -109 <= Node.val <= 109
    All Node.val are unique.
    p != q
    p and q will exist in the tree.

Input: root = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, None, None, 13, 14], p = 5, q = 1
Output: 3
"""
from typing import List, Optional


class BinaryNode:

    def __init__(self, value: Optional[int] = None,
                 left_child: Optional['BinaryNode'] = None,
                 right_child: Optional['BinaryNode'] = None):
        self.value = value
        self.left = left_child
        self.right = right_child

    def __repr__(self):
        return f'Node(value={self.value}, ' \
               f'left_child={self.left}, ' \
               f'right_child={self.right})'

    @classmethod
    def build_tree(cls, values: List[Optional[int]]):
        nodes = [cls(value) for value in values]
        for i, node in enumerate(nodes):                # i:     0 / 1 / 2 / 3 / 4 /  5  /  6 /
            j = 2*i + 1                                 # j:     1 / 3 / 5 / 7 / 9 /  11 / 13 /
            try:
                node.left = nodes[j]                    # index: 1 / 3 / 5 / 7 / 9 /  11 / 13 /
                node.right = nodes[j + 1]               # index: 2 / 4 / 6 / 8 / 10 / 12 / 14 /
            except IndexError:
                break
        return nodes


class BinaryTreeOperator:

    def __init__(self):
        self._result = None

    def find_lowest_common_ancestor(self, root: List[Optional[int]], p, q) -> int:
        primary_node = BinaryNode.build_tree(root)[0]

        def inspect_tree(node) -> int:
            if not node:
                return False

            this_node_wanted = node.value == p or node.value == q   # may be right away one of the two wanted, or ...
            left_child_wanted = inspect_tree(node.left)             # left-child may immediately return true, or ...
            right_child_wanted = inspect_tree(node.right)           # right-child. If not -> repeat recursively !

            if (this_node_wanted + left_child_wanted + right_child_wanted) == (True + True):
                self._result = node.value

            return this_node_wanted or left_child_wanted or right_child_wanted

        inspect_tree(primary_node)
        return self._result
