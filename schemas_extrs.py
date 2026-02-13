from pydantic import BaseModel, Field, computed_field, field_validator, model_validator, field_serializer
from typing import Optional, Generic, TypeVar
from pydantic.config import ConfigDict

# # class SignUpModel(BaseModel):
# #     username: str
# #     email: str
# #     password: str
# #     is_staff: Optional[bool]
# #     is_active: Optional[bool]

# #     class Config:
# #         orm_mode = True
# #         schema_extra={
# #             'example': {
# #                 'username': 'nurshod_dev',
# #                 'email': 'nurshoddeveloper@gmail.com',
# #                 'password': 'nurshoddeveloper7',
# #                 'is_staff': False,
# #                 'is_active': True
# #             }
# #         }






# class User(BaseModel):
#     name: str
#     age: int

# user = User(name='Nurshod', age=20)
# print(user.name)
# print(user.age)


# class Book(BaseModel):
#     title: str
#     pages: int
#     price: float

# book = Book(title='Python Guide', pages=350, price=29.99)
# print(book.title)
# print(book.pages)
# print(book.price)

# # book = Book(title='Python Guide', pages='two hundred', price=29.99)



# class Product(BaseModel):
#     name: str
#     price: float
#     is_available: bool = False
#     stock_count: int | None = None


# product1 = Product(name='Apple', price=12.22, is_available=True, stock_count=2)
# product2 = Product(name='Apple', price='12.22', stock_count='2')
# product3 = Product(name='Apple', price='12.22', is_available='true')


# print(product1)
# print(product2)
# print(product3)


# class BlogPost(BaseModel):
#     title: str
#     content: str
#     author: str | None = None
#     published: bool = False
#     views: int = 0
#     tags: str | None = None

# blogPost1 = BlogPost(title='Hello world', content='Hello world hi my name is Nurshod')
# blogpost2 = BlogPost(title='Hello wolrd', content='Wsup everybody!', author='Tony')
# blogpost3 = BlogPost(title='Hello wolrd3', content='Wsup everybody! How  yall', author='Tony', published=True, views=32, tags='interesting')



# class RegisterUser(BaseModel):
#     username: str = Field(min_length=3, max_length=20)
#     password: str = Field(min_length=8)
#     age: int = Field(ge=18, le=100)
#     email: str
#     referral_code: Optional[str] = Field(default=None, pattern=r'REF-\d{6}')

# user = RegisterUser(username='nurshod', password='nurshoddeveloper7', age=20, email='nurmirdev@gmail.com', referral_code='REF-123456')
# user2 = RegisterUser(username='nur', password='nurshoddeveloper7', age=20, email='nurmirdev@gmail.com', referral_code='REF-123456')
# user3 = RegisterUser(username='nurshod', password='per7', age=11, email='nurmirdev@gmail.com', referral_code='REF-123456')
# print(user)
# print(user2)
# print(user3)



# class Product(BaseModel):
#     price: float
#     tax_rate: float  # You have to calculate this manually!

#     @property
#     def price_with_tax(self) -> float:
#         return self.price * self.tax_rate
    
# # Problem: You might forget to update it
# product = Product(price=100, tax_rate=0.1)
# print(product.price_with_tax)
# product.price = 200  # Changed price
# # But price_with_tax is still 110! ❌ Wrong!






class Circle(BaseModel):
    radius: float = Field(gt=0)

    @computed_field
    @property
    def diameter(self) -> float:
        return self.radius * 2
    
    @computed_field
    @property
    def area(self) -> float:
        return 3.14159 * self.radius * self.radius
    
# circle = Circle(radius=5)
# print(circle.model_dump())

# circle2 = Circle(radius=10)
# print(circle2.model_dump_json())





class Password(BaseModel):
    password: str

    @field_validator('password')
    def validate_all(cls, v):
        if len(v) < 8:
            raise ValueError('password must be at least 8 characters')
        if not any(c.isupper() for c in v):
            raise ValueError('password must be contain at least 1 uppercase letter')
        if not any(c.isdigit() for c in v):
            raise ValueError('password must contain at least one number')
        return v
    
# password = Password(password='SecurePass122')
# password2 = Password(password='short')
# password3 = Password(password='alllowercase123')
# password3 = Password(password='Nonumber')

# print(password.model_dump())



class Product(BaseModel):
    name: str
    price: float = Field(gt=0)


class CartItem(BaseModel):
    product: Product
    quantity: int = Field(ge=1)


class ShoppingCart(BaseModel):
    customer_name: str
    items: list[CartItem]

john_shopping_cart = ShoppingCart(
    customer_name='John',
    items=[
        {
           'product': {'name': 'Laptop', 'price':999.99}, 
            'quantity': 2
        },
        {
           'product': {'name': 'Mouse', 'price':25.99}, 
            'quantity': 1
        }
    ]
)

# print(f"Customer: {john_shopping_cart.customer_name}")

# print("\nItems in cart:")
# for item in john_shopping_cart.items:
#     print(f"- {item.product.name}: {item.quantity} x ${item.product.price}")

# total = sum(item.product.price * item.quantity for item in john_shopping_cart.items)
# print(f"\nTotal Cost: ${total:.2f}")


class StrictUser(BaseModel):
    model_config = ConfigDict(
        str_strip_whitespace=True,
        extra='forbid',
        frozen=True
    )

    username: str
    email: str
    age: int


# user1 = StrictUser(username='   alice    ', email=' nurshod@gmail ', age=22)
# print(user1)
# user2 = StrictUser(username='   alice    ', email=' nurshod@gmail ', age=22, role='admin')
# print(user2)

# user1.username = '  nurshod '
# print(user1)


class UserProfile(BaseModel):
    username: str
    email: str
    password: str
    age: int
    bio: str | None = None
    website: str | None = None

    @field_serializer('password')
    def hide_password(self, v):
        return '*' * len(v)
    

user = UserProfile(
    username='nurshod',
    email='nurmirdev@gmail.com',
    password='123455',
    age=33
)
# print(user.model_dump())
# print(user.model_dump(exclude_none=True))
# print(user.model_dump(exclude={'password'}))
# print(user.model_dump())

# T = TypeVar('T')

# class APIResponse(BaseModel, Generic[T]):
#     success: bool
#     data: T | None = None
#     message: str | None = None

# class User(BaseModel):
#     name: str
#     email: str

# class Product(BaseModel):
#     name: str
#     price: float

# user = APIResponse[User](
#     success=True,
#     data={'name': 'nurshod', 'email': 'nurmirdev@gmail.com'},
#     message='Done'
# )
# product = APIResponse[Product](
#     success=True,
#     data={'name': 'apple', 'price': '12.22'},
#     message='Done'
# )

# print(user.model_dump())
# print(product.model_dump())


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Generic, TypeVar
from pydantic_settings import BaseSettings

app = FastAPI()

class BookCreate(BaseModel):
    title: str
    author: str
    pages: int = Field(ge=1)
    price: float = Field(ge=0)


class BookResponse(BookCreate):
    id: int
    

books_db = {}
counter = 1

@app.post('/books', response_model=BookResponse)
async def create_book(book: BookCreate):
    global counter
    new_book = {'id': counter, **book.model_dump()}
    books_db[counter] = new_book
    counter += 1
    return new_book

@app.get('/books', response_model=list[BookResponse])
async def list_books():
    return list(books_db.values())


@app.get('/books/{book_id}', response_model=BookResponse)
async def get_book(book_id: int):
    if book_id not in books_db:
        raise HTTPException(status_code=404, detail='Book not found')
    return books_db[book_id]




class Settings(BaseSettings):
    app_name: str = 'My Awesome API'
    debug: bool = True
    database_url: str
    secret_key: str
    max_connections: int
    api_version: str = 'v1'
    allowed_hosts: list[str] = ['*']

    class Config:
        env_file = '.env'

setting = Settings()
app = FastAPI(title=setting.app_name)

@app.get('/settings')
async def get_settings():
    return {
        'app_name': setting.app_name,
        'debug': setting.debug,
        'max_connections': setting.max_connections,
        'api_version': setting.api_version,
        
    }
