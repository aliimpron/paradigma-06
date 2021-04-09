def postorder_traverse (tree):
        if tree == []:
                return
        value = tree[0]
        postorder_traverse(tree[1])
        postorder_traverse(tree[2])
        print value