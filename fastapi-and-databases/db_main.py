from dbcrud import get_student_all, get_student_by_id, create_student, student_update, student_delete_by_age, student_delete_by_id
from sqlalchemy import Column

#below lines were used to ceate the entries
# create_student("Ashish", 34, "Delhi")
# create_student("Rahul", 24, "Bagalore")
# create_student("Chunky", 19, "Mumbai")

#fetch all students
all_students = get_student_all()
print(all_students[0].name)

#update the city of Rahul
student_update("Rahul", "Kanpur")

#delete the student whose age is less than 20 (sending 20 as config param)
student_delete_by_age(20)

##****************below is for tesing**************
# student = get_student(1)
# print(student.name)
# student_update(2,"newname")
# student_delete_by_id(3)
# student_delete_by_id(4)
# print(len(All_users))
