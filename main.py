from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from database import SessionLocal
import crud, schemas
import os
from dotenv import load_dotenv

# .env 読み込み
load_dotenv()

app = FastAPI()

# CORS設定（必要に応じて "*" や本番URLも許可）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# DBセッション取得
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

print("DATABASE_URL:", os.getenv("DATABASE_URL"))

# 商品コード検索API
@app.get("/products/{code}", response_model=schemas.ProductResponse)
def read_product(code: str, db: Session = Depends(get_db)):
    product = crud.get_product_by_code(db, code)
    if not product:
        raise HTTPException(status_code=404, detail="商品が見つかりません")
    return product

# 購入処理API
@app.post("/purchase", response_model=schemas.PurchaseResponse)
def purchase(req: schemas.PurchaseRequest, db: Session = Depends(get_db)):
    try:
        total = crud.register_purchase(db, req)
        return {"success": True, "total_amount": total}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
