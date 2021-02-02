class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 0
        for i in range(len(digits)):
            if i == 0:
                temp = (digits[-i-1] + carry + 1)%10
                carry = (digits[-i-1] + carry + 1)//10
                digits[-i-1] = temp
            else:
                temp = (digits[-i-1] + carry)%10
                carry = (digits[-i-1] + carry)//10
                digits[-i-1] = temp
        if carry == 1:
            digits.insert(0, 1)
        return digits