class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = None
        list = []
        while l1 or l2 or carry:
            v1 = 0
            v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            if carry:
                sum = v1 + v2 + carry
            else:
                sum = v1 + v2
            if sum >= 10:
                remainder = sum % 10
                carry = (sum - remainder) / 10
                sum = remainder
            else:
                carry = None
            list.append(sum)
        return list

if __name__ == "__main__":
    sol = Solution()
