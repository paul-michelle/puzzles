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

Input: root = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, None, None, 11, 13], p = 5, q = 1
Output: 3
"""
from typing import List, Optional, Generator


class Node:

    def __init__(self, value: Optional[int] = None,
                 left_child: Optional['Node'] = None,
                 right_child: Optional['Node'] = None):
        self.value = value
        self.left = left_child
        self.right = right_child

    def __repr__(self):
        return f'Node(value={self.value}, ' \
               f'left_child={self.left}, ' \
               f'right_child={self.right}'

    @classmethod
    def generate_nodes(cls, values: List[Optional[int]]) \
            -> Generator['Node', None, None]:
        for i in range(len(values)):
            j = 2*i + 1                             # i: 0 / 1/  2 / 3/  4 /
            try:
                value = values[i]               # index: 0 / 1 / 2 / 3 / 4 /
                left = values[j]                # index: 1 / 3 / 5 / 7 / 9 /
                right = values[j + 1]
                yield cls(value, left, right)
            except (IndexError, StopIteration):
                break

    @classmethod
    def get_tree(cls, values: List[Optional[int]]):
        return list(cls.generate_nodes(values))


class LowestCommonAncestor:

    @staticmethod
    def find_lca(root: List[Optional[int]], p, q) -> int:
        tree = Node.get_tree(root)

        def inspect_tree(node) -> int:
            left = inspect_tree(node.left)
            right = inspect_tree(node.right)
            mid = node.value == p or node.value == q
            if mid + left + right >= 2:
                return node.value
            return mid or left or right

        return inspect_tree(tree[0])
