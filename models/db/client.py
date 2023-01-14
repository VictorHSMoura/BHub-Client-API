from datetime import datetime

from db.sqlalchemy_db import Base
from sqlalchemy import Column, Integer, Float, String, Date
from sqlalchemy.orm import relationship

class Client(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True, index=True)
    corporate_name = Column(String(100))
    phone = Column(String(20))
    register_date = Column(Date, default = datetime.now().date())
    declared_billing = Column(Float)
    bank_details = relationship("BankDetails")
