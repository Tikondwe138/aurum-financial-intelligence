from sqlalchemy import Column, Integer, Float, String
from app.models.base import Base, TimestampMixin, TenantMixin

class Expense(Base, TimestampMixin, TenantMixin):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
