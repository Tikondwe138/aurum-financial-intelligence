from sqlalchemy import Column, Integer, String, Float
from app.models.base import Base, TimestampMixin, TenantMixin

class Product(Base, TimestampMixin, TenantMixin):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
