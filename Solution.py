# ============================================================
# LeetCode #2 - Add Two Numbers
# Difficulty: Medium
# Topic: Linked List, Math
# Time Complexity:  O(max(m, n)) - m and n are lengths of l1, l2
# Space Complexity: O(max(m, n)) - for the result linked list
# ============================================================

# Definition for singly-linked list (provided by LeetCode)
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy   = ListNode(0)  # placeholder node to simplify result building
        current = dummy        # pointer to build the result list
        carry   = 0            # carry from previous digit addition

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0  # get value from l1, or 0 if exhausted
            v2 = l2.val if l2 else 0  # get value from l2, or 0 if exhausted

            total  = v1 + v2 + carry  # sum of digits + carry
            carry  = total // 10      # new carry (1 if total >= 10, else 0)
            digit  = total % 10       # actual digit to store

            current.next = ListNode(digit)  # create new node with digit
            current      = current.next     # move current pointer forward

            l1 = l1.next if l1 else None    # move l1 forward
            l2 = l2.next if l2 else None    # move l2 forward

        return dummy.next  # skip the dummy node, return real result