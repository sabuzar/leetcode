from typing import Optional


class ListNode:
    pass


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pass

l1=[5,4,3]
l2=[5,6,4]




def add_digits_with_carry(digit1, digit2):
    # Add two digits
    digit_sum = digit1 + digit2

    # Calculate the carry
    carry = digit_sum // 10

    # Extract the result (the sum of the digits without carry)
    result = digit_sum % 10

    return result, carry

def add_numbers_with_carry(num1, num2):
    result = []
    carry = 0
    num1, num2 = str(num1).rjust(len(str(num2)), '0'), str(num2).rjust(len(str(num1)), '0')
    for i in range(len(num1) - 1, -1, -1):
        digit1, digit2 = int(num1[i]), int(num2[i])
        digit_sum, carry = add_digits_with_carry(digit1, digit2 + carry)
        result.insert(0, digit_sum)
    if carry:
        result.insert(0, carry)
    return result
num1 = 78
num2 = 96
result_list = add_numbers_with_carry(num1, num2)
print(f"{num1} + {num2} = {result_list}")




