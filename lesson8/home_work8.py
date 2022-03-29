a = [1, 2, 3]
class Solution:
    def plusOne(digits:list) -> list:
        a.append(a[-1] + 1)
        a.remove(a[-2])
Solution.plusOne(a)
print(a)