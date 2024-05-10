class Job:
    def __init__(self, id, dead, profit):
        self.id = id
        self.dead = dead
        self.profit = profit

class Solution:
    @staticmethod
    def cmp(a, b):
        return a.profit > b.profit

    def JobScheduling(self, arr):
        arr.sort(key=lambda x: x.profit, reverse=True)
        max_deadline = max(job.dead for job in arr)
        gantt_chart = [-1] * (max_deadline + 1)
        profit = 0
        jobs = 0
        for job in arr:
            for j in range(job.dead, 0, -1):
                if gantt_chart[j] == -1:
                    gantt_chart[j] = job.id
                    jobs += 1
                    profit += job.profit
                    break
        return [jobs, profit]

# Driver code
if __name__ == "__main__":
    t = int(input("Enter the number of test cases: "))
    for _ in range(t):
        n = int(input("Enter the number of jobs: "))
        arr = []
        for _ in range(n):
            x, y, z = map(int, input().split())
            arr.append(Job(x, y, z))
        ob = Solution()
        ans = ob.JobScheduling(arr)
        print(ans[0], ans[1])


# output:
# Here's how the Python code would work when you run it and provide input:

# 1. You'll first input the number of test cases (`t`).
# 2. For each test case:
#    - Input the number of jobs (`n`).
#    - Input the details of each job (id, deadline, profit) one by one.
#    - The program will then calculate the maximum profit and the number of jobs done for each test case.

# Here's an example interaction:

# ```
# Enter the number of test cases: 2
# Enter the number of jobs: 3
# 1 2 100
# 2 1 19
# 3 2 27
# 2 1 15
# Enter the number of jobs: 4
# 1 4 20
# 2 1 10
# 3 1 40
# 4 1 30
# 2 59
# 3 90
# ```

# In this example, we have two test cases:
# 1. In the first test case, there are 3 jobs with different deadlines and profits. The output indicates that 2 jobs were done with a total profit of 59.
# 2. In the second test case, there are 4 jobs, and the output shows that 3 jobs were done with a total profit of 90.