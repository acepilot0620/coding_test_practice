class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        answer = [0]*len(temperatures)
        stack = []
        for cur_day,cur_temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < cur_temp:
                prev_day = stack.pop()
                answer[prev_day] = cur_day-prev_day
            stack.append(cur_day)
        return answer

sol = Solution()
temp = [73,74,75,71,69,72,76,73]
print(sol.dailyTemperatures(temperatures=temp))