class Attendance:
    
    def __init__(self, n):
        # n: Total number of days
        if n < 4 or n < 0:
            raise Exception("Total Number of days should be greater than 4")

        self.n = n
    
    
    def solution(self):
 
        n = self.n
        dp = [[0] * 5 for i in range(n + 1)]

        for i in range(4):
            dp[0][i] = 1

        for i in range(1, n + 1):
            for j in range(3, -1, -1):
                dp[i][j] = dp[i - 1][0] + dp[i - 1][j + 1]

        a = dp[n][0]  
        b = dp[n - 1][1]  

        return f"{b}/{a}"

 
    def printSolution(self):
        print("The answer is ",self.solution()," when n = ",self.n)

inputs = [5, 10]
for n in inputs:
    obj = Attendance(n)
    obj.printSolution()

