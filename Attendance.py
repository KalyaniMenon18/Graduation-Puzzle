class Attendance:
    def __init__(self, n):
        # n: Total number of days
        if n < 4 or n < 0:
            raise Exception("Total Number of days should be greater than 4")

        self.n = n
