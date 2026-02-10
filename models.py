from database import Base, Session 
from sqlalchemy import Column, Integer, String, Boolean, Text, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy_utils.types import ChoiceType

class User(Base):
    __tablename__= 'user'

    # id = Column(Integer, primary_key=True)
    # username = Column(String(25), unique=True) 
    # email = Column(String(70), unique=True)
    # password = Column(Text, nullable=True)
    # is_staff = Column(Boolean, default=False)
    # is_active = Column(Boolean, default=False)

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(25), unique=True)
    email: Mapped[str] = mapped_column(String(70), unique=True)
    password: Mapped[str] = mapped_column(Text)
    is_staff: Mapped[bool] = mapped_column(default=False)
    is_active: Mapped[bool] = mapped_column(default=False)


    # orders = relationship('Order', back_populates='user')
    orders: Mapped[list['Order']] = relationship(back_populates='user')

    def __repr__(self):
        return f'<User {self.username}>'

class Order(Base):
    __tablename__= 'orders'

    ORDER_STATUS = (
        ('PENDING', 'pending'),
        ('IN_TRANSIT', 'in_transit'),
        ('DELIVERED', 'delivered')
    )

    # id = Column(Integer, primary_key=True)
    id: Mapped[int] = mapped_column(primary_key=True)

    # quantity = Column(Integer, nullable=False)
    quantity: Mapped[int] = mapped_column()

    # user_id = Column(Integer, ForeignKey('user.id'))
    # product_id = Column(Integer, ForeignKey('product.id'))
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    product_id_id: Mapped[int] = mapped_column(ForeignKey('product.id'))
    
    # user = relationship('User', back_populates='orders')
    # product = relationship('Product', back_populates='orders')
    user: Mapped['User'] = relationship(back_populates='orders')
    product: Mapped['Product'] = relationship(back_populates='orders')


    order_statuses = Column(ChoiceType(choices=ORDER_STATUS), default='PENDING')
    
    def __repr__(self):
        return f'<Order {self.id}>'


class Product(Base):
    __tablename__= 'product'

    # id = Column(Integer, primary_key=True)
    id: Mapped[int] = mapped_column(primary_key=True)

    # name = Column(String(200))
    name: Mapped[str] = mapped_column(String(200))

    # price = Column(Integer)
    price: Mapped[int] = mapped_column()

    # orders = relationship('Order', back_populates='product')
    orders: Mapped[list['Order']] = relationship(back_populates='product')


    def __repr__(self):
        return f'<Product {self.name}>'
