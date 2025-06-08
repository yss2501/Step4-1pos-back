from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, CHAR, TIMESTAMP
from sqlalchemy.orm import relationship
from database import Base
import datetime

class ProductMaster(Base):
    __tablename__ = "product_master"
    prd_id = Column(CHAR(13), primary_key=True, index=True)
    code = Column(String(50), unique=True)
    name = Column(String(100))
    price = Column(Integer)

class Transaction(Base):
    __tablename__ = "transaction"
    trd_id = Column(Integer, primary_key=True, index=True)
    datetime = Column(TIMESTAMP, default=datetime.datetime.utcnow)
    emp_cd = Column(CHAR(10))
    store_cd = Column(CHAR(5))
    pos_no = Column(CHAR(5))
    total_amt = Column(Integer)
    ttl_amt_ex_tax = Column(Integer)

    details = relationship("TransactionDetail", back_populates="transaction")

class TransactionDetail(Base):
    __tablename__ = "transaction_detail"
    id = Column(Integer, primary_key=True, index=True)
    trd_id = Column(Integer, ForeignKey("transaction.trd_id"))

    dtl_id = Column(Integer)

    prd_id = Column(CHAR(13))
    prd_code = Column(String(50))
    prd_name = Column(String(100))
    prd_price = Column(Integer)
    tax_cd = Column(CHAR(2))

    transaction = relationship("Transaction", back_populates="details")
