from db import engine
from tables import students
from pydantic import Field, EmailStr
from sqlalchemy import Table, column, String, MetaData, Integer, insert, update, select, delete



def create_student(name:str, age:int, city:str=Field(...,max_length=20)):
    with engine.connect() as conn:
        query = insert(students).values(name=name, age=age, city=city)
        conn.execute(query)
        conn.commit()
        conn.close()


def get_student_by_id(id:int):
    with engine.connect() as conn:
        query = select(students).where(students.c.id == id)
        studentobj =  conn.execute(query).first()
        return studentobj
        conn.close()


def get_student_all():
    with engine.connect() as conn:
        query = select(students)
        students_obj = conn.execute(query).fetchall()
        conn.close()
        return students_obj


def student_update(name:str, upd_city:str):
    with engine.connect() as conn:
        query = update(students).where(students.c.name == name).values(city = upd_city)
        conn.execute(query)
        conn.commit()
        conn.close()


def student_delete_by_age(agelimit:int):
    with engine.connect() as conn:
        query = delete(students).where(students.c.age < agelimit)
        conn.execute(query)
        conn.commit()
        conn.close()


def student_delete_by_id(id:int):
    with engine.connect() as conn:
        query = delete(students).where(students.c.id == id)
        conn.execute(query)
        conn.commit()
        conn.close()
