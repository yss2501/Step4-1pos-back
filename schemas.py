from pydantic import BaseModel, ConfigDict
from typing import List

class ProductResponse(BaseModel):
    prd_id: str
    code: str
    name: str
    price: int
    model_config = ConfigDict(from_attributes=True)

class PurchaseItem(BaseModel):
    prd_id: str
    prd_code: str
    prd_name: str
    prd_price: int

class PurchaseRequest(BaseModel):
    emp_cd: str
    store_cd: str
    pos_no: str
    items: List[PurchaseItem]

class PurchaseResponse(BaseModel):
    success: bool
    total_amount: int
    total_amount_ex_tax: int
