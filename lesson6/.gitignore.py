# mass = [i for i in range(1_000_000)]
# #
# # target = 999_999
# #
# for num in range(len(mass)):
#     if target == mass[num]:
#         print(num)
# # print(mass)
# def get_list() -> list:
#     return list(range(0, 1_000_000, 1))
#
# # print((get_list()))
#
# class Solution:
#
#     def find_target(self, list, target):
#         low = 0
#         up = len(list)
#
#         while low < up:
#             midle = (low + up) // 2
#
#             if list[midle] == target:
#                 return midle
#             elif list[midle] > target:
#                 up = midle - 1
#             elif list[midle] < target:
#                 low = midle + 1
#         return - 1




    # def otvet(self):
    #
    #     if self.list == self.target:
    #         print(f'ваша цифра: 'target)


# Solution().find_target(get_list(), 888888)
def get_list() -> list:
    return list(range(0, 1_000_000, 2))


class Solution:

    def find_target(self, list, target):
        mini_limit = 0
        max_limit = len(list)
        peremennaia = 0
        while mini_limit <= max_limit:
            peremennaia += 1
            middle_index = (mini_limit + max_limit) // 2
            if list[middle_index] < target:
                mini_limit = middle_index + 1
            elif list[middle_index] > target:
                max_limit = middle_index - 1
            else:
                return peremennaia

print(Solution().find_target(get_list(), 500))