# ListNode class definition (zaroori hai linked list ke nodes banane ke liye)
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(list1, list2):
    # Ek dummy node banate hain nayi list ki shuruat karne ke liye
    dummy = ListNode(-1)
    current = dummy
    
    # Jab tak dono lists mein nodes bache hain
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
        
    # Agar ek list khatam ho jaye aur dusri mein elements bache hon
    if list1:
        current.next = list1
    else:
        current.next = list2
        
    return dummy.next