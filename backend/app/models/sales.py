from sqlalchemy import Column, Integer, Float, Date
from app.models.base import Base, TimestampMixin, TenantMixin

class Sale(Base, TimestampMixin, TenantMixin):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)
    revenue = Column(Float, nullable=False)
    date = Column(Date, nullable=False)
