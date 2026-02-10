# from pydantic import BaseModel
# from typing import Optional

# class SignUpModel(BaseModel):
#     username: str
#     email: str
#     password: str
#     is_staff: Optional[bool]
#     is_active: Optional[bool]

#     class Config:
#         orm_mode = True
#         schema_extra={
#             'example': {
#                 'username': 'nurshod_dev',
#                 'email': 'nurshoddeveloper@gmail.com',
#                 'password': 'nurshoddeveloper7',
#                 'is_staff': False,
#                 'is_active': True
#             }
#         }





from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

user = User(name='Nurshod', age=20)
print(user.name)
print(user.age)













