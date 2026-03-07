# ============================================================
# Add Two Numbers - Full Runnable Solution
# ============================================================
# Problem:
#   Given two numbers represented as reversed linked lists,
#   return their sum as a reversed linked list.
#
# Example:
#   Input:  l1 = 2->4->3  (342)
#           l2 = 5->6->4  (465)
#   Output: 7->0->8       (807)
# ============================================================


# ── Node definition ─────────────────────────────────────────

class ListNode:
    def __init__(self, val=0, next=None):
        self.val  = val
        self.next = next


# ── Helper: build linked list from a plain list ─────────────

def build_linked_list(numbers):
    """Convert a Python list to a linked list.
    Example: [2, 4, 3] → 2->4->3
    """
    dummy   = ListNode(0)
    current = dummy
    for num in numbers:
        current.next = ListNode(num)
        current      = current.next
    return dummy.next


# ── Helper: convert linked list back to a plain list ────────

def linked_list_to_list(node):
    """Convert a linked list back to a Python list.
    Example: 2->4->3 → [2, 4, 3]
    """
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


# ── Main solution ────────────────────────────────────────────

def addTwoNumbers(l1, l2):
    """
    Add two numbers represented as reversed linked lists.

    Args:
        l1 (ListNode): Head of first linked list
        l2 (ListNode): Head of second linked list

    Returns:
        ListNode: Head of result linked list (also reversed)
    """
    dummy   = ListNode(0)  # placeholder node
    current = dummy        # pointer to build result
    carry   = 0            # carry from previous addition

    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0  # digit from l1
        v2 = l2.val if l2 else 0  # digit from l2

        total  = v1 + v2 + carry  # sum of both digits + carry
        carry  = total // 10      # carry for next iteration
        digit  = total % 10       # digit to store in result

        current.next = ListNode(digit)  # attach new node
        current      = current.next     # move pointer

        l1 = l1.next if l1 else None    # advance l1
        l2 = l2.next if l2 else None    # advance l2

    return dummy.next  # return result (skip dummy)


# ── Test cases ───────────────────────────────────────────────

def run_tests():
    test_cases = [
        {
            "description": "Basic case: 342 + 465 = 807",
            "l1":      [2, 4, 3],
            "l2":      [5, 6, 4],
            "expected": [7, 0, 8],
        },
        {
            "description": "With carry at end: 999 + 1 = 1000",
            "l1":      [9, 9, 9],
            "l2":      [1],
            "expected": [0, 0, 0, 1],
        },
        {
            "description": "Both zeros: 0 + 0 = 0",
            "l1":      [0],
            "l2":      [0],
            "expected": [0],
        },
        {
            "description": "Different lengths: 99 + 1 = 100",
            "l1":      [9, 9],
            "l2":      [1],
            "expected": [0, 0, 1],
        },
    ]

    all_passed = True

    for i, test in enumerate(test_cases, 1):
        l1     = build_linked_list(test["l1"])
        l2     = build_linked_list(test["l2"])
        result = linked_list_to_list(addTwoNumbers(l1, l2))
        passed = result == test["expected"]

        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"Test {i}: {status} | {test['description']}")

        if not passed:
            print(f"         Expected: {test['expected']}")
            print(f"         Got:      {result}")
            all_passed = False

    print()
    print("All tests passed! 🎉" if all_passed else "Some tests failed. 😬")


if __name__ == "__main__":
    run_tests()