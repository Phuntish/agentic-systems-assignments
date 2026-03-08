class StudentMarks:
    def __init__(self, studentmarks):
        self.marks = studentmarks

    def last_three_avg(self):
        try:
            #check if we have atleast 3 StudentMarks
            if len(self.marks) < 3:
                raise ValueError
            else:
                totaloflastthree = sum(self.marks[-3:])
                average = totaloflastthree/3
                return average

        except ValueError:
            return("Not enough marks to calculate last_three_avg average")



student1 = StudentMarks([10,23])
student1_avg = student1.last_three_avg()
print(f"Average of last 3 marks is: ",student1_avg)

student2 = StudentMarks([10,23,23,45])
student2_avg = student2.last_three_avg()
print(f"Average of last 3 marks is: ",student2_avg)