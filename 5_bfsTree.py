class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bfs(root):
    if not root:
        return

    queue = [root]

    while queue:
        node = queue.pop(0)
        print(node.val, end=" ")

        for child in (node.left, node.right):
            if child:
                queue.append(child)


# Example usage:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

bfs(root)

