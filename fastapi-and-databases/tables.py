from sqlalchemy import Table, Column, MetaData, String, Integer, CheckConstraint
from db import engine

metada_obj = MetaData()

students = Table("student",metada_obj, Column("id", Integer, primary_key =True),
   Column("name", String, nullable=False),
   Column("age", Integer, CheckConstraint("age > 18"),nullable=False), 
    Column("city", String(20), nullable=True)
)

metada_obj.create_all(engine)