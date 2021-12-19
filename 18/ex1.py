import sys
import json
input = list(map(json.loads, sys.stdin.read().strip().split("\n")))
class Node:
    right = None
    left = None
    parent = None
    leaf = False
    val = 0
    def __init__(self):
        pass

def hak(lst):
    cur = Node()
    if isinstance(lst, int):
        cur.leaf = True
        cur.val = lst
        return cur
    cur.left = hak(lst[0])
    cur.left.parent = cur
    cur.right = hak(lst[1])
    cur.right.parent = cur
    return cur
def addLeft(cur, lk):
    if cur.leaf == True:
        cur.val += lk
        return True
    elif addLeft(cur.right, lk) or addLeft(cur.left, lk):
        return True
    return False
def addRight(cur, lk):
    if cur.leaf == True:
        cur.val += lk
        return True
    elif addRight(cur.left, lk) or addRight(cur.right, lk):
        return True
    return False

def reducer1(cur, dp):
    if cur.leaf == False:
        if dp == 4:
            # EXPLODE
            lft = cur
            while lft.parent != None:
                if lft.parent.left != lft and addLeft(lft.parent.left, cur.left.val):
                    break
                lft = lft.parent
            rgt = cur
            while rgt.parent != None:
                if rgt.parent.right != rgt and addRight(rgt.parent.right, cur.right.val):
                    break
                rgt = rgt.parent
            cur.val = 0
            cur.leaf = True
            cur.right = None
            cur.left = None
            return True
        else:
            if reducer1(cur.left, dp+1):
                return True
            if reducer1(cur.right, dp+1):
                return True
    return False
def reducer2(cur, dp):
    if cur.leaf:
        if cur.val >= 10:
            cur.leaf = False
            cur.left = Node()
            cur.left.leaf = True
            cur.left.val = cur.val//2
            cur.left.parent = cur
            cur.right = Node()
            cur.right.leaf = True
            cur.right.val = (cur.val+1)//2
            cur.right.parent = cur
            return True
    else:
        if reducer2(cur.left, dp+1):
            return True
        if reducer2(cur.right, dp+1):
            return True
    return False
def reduce(root):
    cont = True
    while cont:
        cont = False
        while reducer1(root, 0):
            cont = True
        if reducer2(root, 0):
            cont = True
def prnt(cur):
    if cur.leaf == True:
        print(cur.val,end="")
        return
    print("[", end="")
    prnt(cur.left)
    print(",", end="")
    prnt(cur.right)
    print("]",end="")
sm = hak(input[0])
reduce(sm)
for i in input[1:]:
    root = Node()
    root.left = sm
    root.left.parent = root
    root.right = hak(i)
    reduce(root.right)
    root.right.parent = root
    reduce(root)
    sm = root
def ans(cur):
    if cur.leaf == True:
        return cur.val
    return ans(cur.left)*3+ans(cur.right)*2

prnt(sm)
print()
print(ans(sm))
