from pydantic import BaseModel, Field, EmailStr

class Student(BaseModel):
    name: str 
    age: int 
    grade: str




new_student2= Student(name="Rakib", age=234, grade="A")

new_student={'name': 'Rakib', 'age': '234', 'grade': 'A'}

student=Student(**new_student)
print(student)

class ST(BaseModel):
    name: str= Field(..., description="The name of the student"),
    age: int= Field(..., description="The age of the student"),
    email: EmailStr=Field(..., description="The email of the student"),
    cgpa: float=Field(gt=0,le=4, default=2, description='A decimal value representing the cgpa of the student')
s={
    
    'name': 'Rakib',
    'age': '123',
    'email': 'anik@gmail.com'
}
student=ST(**s)
print(student)


from typing import Optional
class test(BaseModel):
   name: str='Rakib',
   age: Optional[int]=None

t={'age':123}
new_obj=test(**t)
print(new_obj)

student_dict=dict(student)
print(student_dict)

student_json=student.model_dump_json()
print(student_json)