# https://leetcode.com/problems/fizz-buzz/

from typing import List


class FizzBuzz:
    def fizz_buzz(self, n: int) -> List[str]:
        answer = []

        for i in range(1, n + 1):
            mult_of_three = i % 3 == 0
            mult_of_five = i % 5 == 0
            if mult_of_three & mult_of_five:
                answer.append("FizzBuzz")
            elif mult_of_three:
                answer.append("Fizz")
            elif mult_of_five:
                answer.append("Buzz")
            else:
                answer.append(str(i))

        return answer
