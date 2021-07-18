# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        totalnode = 0
        dummy =ListNode(-1,head)
        
        if (head is None) or (k == 1):
            return head
        
        temp = dummy.next
        while temp:
            totalnode += 1
            temp = temp.next
        
        nxt = None
        prev = dummy
        
        while totalnode >= k :
            curr = prev.next
            nxt = curr.next
            for _ in range(1,k):
                curr.next = nxt.next
                nxt.next = prev.next
                prev.next = nxt
                nxt = curr.next
            prev = curr
            totalnode = totalnode - k
        
        return dummy.next

        

        
       
            
            
                    
                    
                    
                
            
            
            
        
                
            
            
        
        