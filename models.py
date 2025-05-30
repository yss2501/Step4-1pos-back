from sqlalchemy import Column, Integer, String, CHAR, TIMESTAMP, ForeignKey
from database import Base
import datetime

class ProductMaster(Base):
    __tablename__ = "product_master"
    prd_id = Column(Integer, primary_key=True, index=True)
    code = Column(CHAR(13), unique=True, nullable=False)
    name = Column(String(50), nullable=False)
    price = Column(Integer, nullable=False)

class Transaction(Base):
    __tablename__ = "transaction"
    trd_id = Column(Integer, primary_key=True, index=True)
    datetime = Column(TIMESTAMP, default=datetime.datetime.utcnow)
    emp_cd = Column(CHAR(10))
    store_cd = Column(CHAR(5))
    pos_no = Column(CHAR(3))
    total_amt = Column(Integer)

class TransactionDetail(Base):
    __tablename__ = "transaction_detail"
    trd_id = Column(Integer, ForeignKey("transaction.trd_id"), primary_key=True)
    dtl_id = Column(Integer, primary_key=True)
    prd_id = Column(Integer, ForeignKey("product_master.prd_id"))
    prd_code = Column(CHAR(13))
    prd_name = Column(String(50))
    prd_price = Column(Integer)
