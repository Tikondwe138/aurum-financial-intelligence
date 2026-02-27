from sqlalchemy import Column, Integer, String
from app.models.base import Base, TimestampMixin, TenantMixin

class Customer(Base, TimestampMixin, TenantMixin):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
