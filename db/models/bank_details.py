from db.sqlalchemy_db import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class BankDetails(Base):
    __tablename__ = "bank_details"
    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey("clients.id"), nullable=False)
    branch = Column(String(20))
    account = Column(String(20))
    bank_name = Column(String(50))
