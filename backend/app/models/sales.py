from sqlalchemy import Column, Integer, Float, Date
from app.core.database import Base

class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)
    revenue = Column(Float, nullable=False)
    date = Column(Date, nullable=False)
