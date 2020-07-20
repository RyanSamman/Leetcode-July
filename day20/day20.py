# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int):
        if head is None:
            return head
        while head.val == val:
            if head.next is None:
                return None
            head = head.next

        prevNode = head
        currNode = head.next

        while currNode is not None:
            if prevNode is None:
                return None

            if currNode.val == val:
                prevNode.next = currNode.next
                currNode = prevNode.next
            else:
                prevNode = currNode
                currNode = currNode.next

        return head


if __name__ == '__main__':
    # Your input
    i_list = [1, 2, 1]
    head = ListNode(i_list[0])
    node = head
    for i in i_list[1:]:
        node.next = ListNode(i)
        node = node.next

    x = Solution()
    x.removeElements(head, 2)
