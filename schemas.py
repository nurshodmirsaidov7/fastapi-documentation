from pydantic import BaseModel, Field
from typing import Optional

class SignUpModel(BaseModel):
    id: Optional[int]
    username: str = Field(le=25)
    email: str
    password: str
    is_staff: Optional[bool]
    is_active: Optional[bool]

    class Config:
        orm_mode=True
        schema_extra={
            'example': {
                'username': 'nurshod',
                'email': 'nurmirdev@gmail.com',
                'password': 'nurshoddeveloper7',
                'is_staff': False,
                'is_active': True
            }
        } 
    