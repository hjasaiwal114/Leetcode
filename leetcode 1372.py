# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        q = collections.deque([]) # (node, from, steps)
        if root.left:
            q.append((root.left, 'L', 1))
        if root.right:
            q.append((root.right, 'R', 1))
        best = 0

        while q:
            node, frm, steps = q.popleft()
            best = max(best, steps)

            if node.left:
                if frm == 'R':
                    q.append((node.left, 'L', steps + 1))
                if frm == 'L':
                    q.append((node.left, 'L', 1))
            
            if node.right:
                if frm == 'L':
                    q.append((node.right, 'R', steps + 1))
                if frm == 'R':
                    q.append((node.right, 'R', 1))
        
        return best 

        