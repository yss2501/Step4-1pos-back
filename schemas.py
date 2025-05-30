from pydantic import BaseModel, ConfigDict
from typing import List

# --------------------
# 商品情報（レスポンス用）
# --------------------
class ProductResponse(BaseModel):
    prd_id: int
    code: str
    name: str
    price: int

    model_config = ConfigDict(from_attributes=True)

# --------------------
# 購入リクエスト用アイテム
# --------------------
class PurchaseItem(BaseModel):
    prd_id: int
    prd_code: str
    prd_name: str
    prd_price: int

# --------------------
# 購入リクエスト全体
# --------------------
class PurchaseRequest(BaseModel):
    emp_cd: str
    store_cd: str
    pos_no: str
    items: List[PurchaseItem]

# --------------------
# 購入レスポンス
# --------------------
class PurchaseResponse(BaseModel):
    success: bool
    total_amount: int
