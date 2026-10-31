from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):

    name : str = 'Prajyot'  # default value
    age : Optional[int] = None
    email : EmailStr
    cgpa : float = Field(gt=0, lt=10, default=9, description='A decimal value representing the cgpa of the student')

new_student = {'age' : 22, 'email' : 'abc@gmail.com'}

student = Student(**new_student)

print(student)
print(type(student))
print()

student_dict = dict(student)
print(student_dict['age'])

student_json = student.model_dump_json()