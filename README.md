# Graduation-Puzzle
In a university, your attendance determines whether you will be
allowed to attend your graduation ceremony.
You are not allowed to miss classes for four or more consecutive days.
Your graduation ceremony is on the last day of the academic year,
which is the Nth day.

Your task is to determine the following:

1. The number of ways to attend classes over N days.
2. The probability that you will miss your graduation ceremony.

Represent the solution in the string format as "Answer of (2) / Answer
of (1)", don't actually divide or reduce the fraction to decimal

Input is read from input.txt file

Test cases:

for 5 days: 14/29
for 10 days: 372/773

## **Dynamic Programming Approach**

The solution uses a bottom-up approach to populate the dp table that stores the count of ways to attend classes.
The table dp[i][j] represents the count of ways to attend classes on the ith day without having j consecutive absences (where j ranges from 0 to 4). The recurrence relationship is that dp[i - 1][0] represents the count of ways to attend classes on the previous day without any consecutive absences. Adding this count to dp[i - 1][j + 1] considers the cases where the previous day had j + 1 consecutive absences.

### **Time Complexity**
O(m*n) where m=5(4 consecutive days +1)

### **Space Complexity**
O(m*n) where m=5(4 consecutive days +1)

