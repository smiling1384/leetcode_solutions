from utils_py.tree import *

class Solution:

    def is_b(self, node):
        if not node:
            return 0
        l = self.is_b(node.left)
        r = self.is_b(node.right)
        if l == -1 or r == -1:
            return -1
        if abs(l-r) > 1:
            return -1
        return max(l, r) + 1

    def isBalanced(self, root: TreeNode) -> bool:
        return self.is_b(root) != -1


def test(test_name, root, expected):
    res = Solution().isBalanced(root)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    #     3
    #    / \
    #   9  20
    #     /  \
    #    15   7
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    expected1 = True
    test('test1', root1, expected1)

    #        1
    #       / \
    #      2   2
    #     / \
    #    3   3
    #   / \
    #  4   4
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(2)
    root2.left.left = TreeNode(3)
    root2.left.right = TreeNode(3)
    root2.left.left.left = TreeNode(4)
    root2.left.left.right = TreeNode(4)
    expected2 = False
    test('test2', root2, expected2)