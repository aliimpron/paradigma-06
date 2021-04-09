def inorder_traverse (tree):
    if tree == []:
            return
    value = tree [0]
    inorder_traverse (tree[1])
    print value
    inorder_traverse (tree[2])
    