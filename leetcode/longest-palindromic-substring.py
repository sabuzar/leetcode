# s="a"
# my_list = list(range(len(s)))
# looping = 0
# for i in range(0, len(s)):
#     if len(s)==1:
#         print(s)
#     else:
#         for comp in range(0, len(s) * 1):
#             Compare1 = s[looping:my_list[comp]]
#             original_string = Compare1
#             reversed_string = ''
#             for char in original_string:
#                 reversed_string = char + reversed_string
#                 if Compare1 == reversed_string:
#                     if len(Compare1) > 1:
#                         print(Compare1)
#         looping = looping + 1


# s = "cbbd"
# my_list = list(range(len(s)))
# looping=0
# for comp in range(0, len(s) * 1):
#     for compr in range(0,len(s)+1):
#         Compare1 = s[comp:compr]
#         original_string = Compare1
#         reversed_string = ''
#         for char in original_string:
#             reversed_string = char + reversed_string
#             if Compare1 == reversed_string:
#                 if len(Compare1)==3:
#                     print(Compare1)
#                 elif len(Compare1) > 2 and len(Compare1) != 3:
#                     print(Compare1)
#         print(Compare1)

# s = "cddt"
# output=[]
# for comp in range(0, len(s) * 1):
#     for compr in range(0, len(s) + 1):
#         Compare1 = s[comp:compr]
#         original_string = Compare1
#         reversed_string = ''
#         for char in original_string:
#             reversed_string = char + reversed_string
#             if Compare1 == reversed_string:
#                 output.append(Compare1)
# data=output[0]
# for result in range(len(output)):
#     for result2 in range(len(output)):
#         if len(output[result]) > len(data):
#             data=output[result]
# print(data)



s = "cccc"
my_list = list(range(len(s)))
class Solution:
    def longestPalindrome(self, s: str) -> str:
        looping = 0
        looping2=0
        for i in range(0, len(s)):
            if len(s) == 1:
                return s
            if len(s) == 2:
                for comp in range(0, 1):
                    Compare2 = s[0:2]
                    original_string = Compare2
                    reversed_string = ''
                    for char in original_string:
                        reversed_string = char + reversed_string
                    if reversed_string == Compare2:
                        return  reversed_string
                    elif reversed_string != Compare2:
                        return s[0]
            else:

                output = []
                for comp in range(0, len(s) * 1):
                    for compr in range(0, len(s) + 1):
                        Compare1 = s[comp:compr]
                        original_string = Compare1
                        reversed_string = ''
                        for char in original_string:
                            reversed_string = char + reversed_string
                            if Compare1 == reversed_string:
                                output.append(Compare1)
                data = output[0]
                for result in range(len(output)):
                    for result2 in range(len(output)):
                        if len(output[result]) > len(data):
                            data = output[result]
                return data

ret = Solution().longestPalindrome(s=s)
print(ret)



#
# s = "ccc"
# my_list = list(range(len(s)))
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         looping = 0
#         looping2=0
#         for i in range(0, len(s)):
#             if len(s) == 1:
#                 return s
#             if len(s) == 2:
#                 for comp in range(0, 1):
#                     Compare2 = s[0:2]
#                     original_string = Compare2
#                     reversed_string = ''
#                     for char in original_string:
#                         reversed_string = char + reversed_string
#                     if reversed_string == Compare2:
#                         return  reversed_string
#                     elif reversed_string != Compare2:
#                         return s[0]
#             else:
#                 for comp in range(0, len(s) * 1):
#                     Compare1 = s[looping:my_list[comp]]
#                     original_string = Compare1
#                     reversed_string = ''
#                     for char in original_string:
#                         reversed_string = char + reversed_string
#                         if Compare1 == reversed_string:
#                             if len(Compare1) > 1:
#                                 return Compare1
#                 looping = looping + 1
#
#
# ret = Solution().longestPalindrome(s=s)
# print(ret)
#
