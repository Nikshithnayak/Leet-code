# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        
        positions = []
        
        # Need previous, current, and next node
        prev = head
        curr = head.next
        
        position = 1
        
        while curr is not None and curr.next is not None:
            
            # Critical point:
            # Local maximum
            if curr.val > prev.val and curr.val > curr.next.val:
                positions.append(position)
            
            # Local minimum
            elif curr.val < prev.val and curr.val < curr.next.val:
                positions.append(position)
            
            prev = curr
            curr = curr.next
            position += 1
        
        # Less than 2 critical points
        if len(positions) < 2:
            return [-1, -1]
        
        # Minimum distance between consecutive critical points
        min_distance = float('inf')
        
        for i in range(1, len(positions)):
            min_distance = min(
                min_distance,
                positions[i] - positions[i - 1]
            )
        
        # Maximum distance = last - first
        max_distance = positions[-1] - positions[0]
        
        return [min_distance, max_distance]