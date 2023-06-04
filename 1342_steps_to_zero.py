# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

class StepsToZero:
    def number_of_steps(self, num: int) -> int:
        if num == 0:
            return 0
        elif num % 2 == 0:
            return 1 + self.number_of_steps(int(num / 2))
        else:
            return 1 + self.number_of_steps(num - 1)
