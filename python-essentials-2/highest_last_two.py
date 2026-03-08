class StudentScores:
    def __init__(self, studentscores):
        self.scores = studentscores

    
    def highest_last_two(self):
        try:
            if len(self.scores) < 2:
                raise ValueError
            
            last_two = self.scores[-2:]
            return max(last_two)

        except ValueError:
            return("Not enough scores to find highest value")



student1 = StudentScores([10])
student1_highest = student1.highest_last_two()
print(f"Highest score among last two is:",student1_highest)

student2 = StudentScores([10,23,23,45])
student2_highest = student2.highest_last_two()
print(f"Highest score among last two is:",student2_highest)