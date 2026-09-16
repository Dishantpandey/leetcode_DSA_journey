def is_same_tree(p, q):
    # Agar dono nodes khali hain
    if not p and not q:
        return True
    
    # Agar ek khali hai ya value match nahi karti
    if not p or not q or p.val != q.val:
        return False
    
    # Left aur right dono parts ko recursively check karo
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)