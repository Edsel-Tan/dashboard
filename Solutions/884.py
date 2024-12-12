import math
from avltree import AVLTree
from prime import memoize

def icrt(x):
    l = 1
    r = x
    while r-l:
        m = (l+r+1)//2
        if (m*m*m) > x:
            r = m-1
        else:
            l = m
    return l

n = 10**17-1
ans = 0
s = AVLTree()
s.insert_key(n, 1)

while s.count > 0:
    node = s.max_value_node(s.root)
    s.delete_key(node.key)
    x = node.key
    y = node.value
    if x == 0:
        break
    z = icrt(node.key)
    z = z**3
    node = s.search_key(x-z)
    ans += (x-z+1)*y
    if not node or node.key != x-z:
        s.insert_key(x-z, y)
    else:
        node.value += y
    node = s.search_key(z-1)
    if not node or node.key != z-1:
        s.insert_key(z-1, y)
    else:
        node.value += y

print(ans)