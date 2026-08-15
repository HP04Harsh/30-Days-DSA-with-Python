class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n

        one_step_behind = 2
        two_step_behind = 1

        current_ways = 0

        for i in range(3,n+1):
            current_ways = one_step_behind+two_step_behind
            two_step_behind =  one_step_behind
            one_step_behind = current_ways

        return current_ways    


        