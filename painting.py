from binarytree import build
class Solution(object):
    def btreeGameWinningMove(self, root, n, x):
        """
        :type root: TreeNode
        :type n: int
        :type x: int
        :rtype: bool
        """
        def count(node, x, left_right):
            if not node:
                return 0
            left, right = count(node.left, x, left_right), count(node.right, x, left_right)
            if node.val == x:
                left_right[0], left_right[1] = left, right
            return left + right + 1

        left_right = [0, 0]
        count(root, x, left_right)
        blue = max(max(left_right), n-(sum(left_right)+1))
        return blue > n-blue

m,n,x=map(int,input().split())
nodes =list(map(int,input().split())) 
binary_tree = build(nodes)
val=Solution()
print(val.btreeGameWinningMove(binary_tree,n,x))
