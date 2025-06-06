from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from database import SessionLocal
import crud, schemas
import os
import traceback  # ← 追加
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/products/{code}", response_model=schemas.ProductResponse)
def read_product(code: str, db: Session = Depends(get_db)):
    product = crud.get_product_by_code(db, code)
    if not product:
        raise HTTPException(status_code=404, detail="商品が見つかりません")
    return {
        "prd_id": str(product.prd_id),  # ✅ 明示的に文字列へ
        "code": product.code,
        "name": product.name,
        "price": product.price,
    }

@app.post("/purchase", response_model=schemas.PurchaseResponse)
def purchase(req: schemas.PurchaseRequest, db: Session = Depends(get_db)):
    try:
        total, total_ex_tax = crud.register_purchase(db, req)
        return {
            "success": True,
            "total_amount": total,
            "total_amount_ex_tax": total_ex_tax
        }
    except Exception as e:
        print("❗例外発生:", e)
        traceback.print_exc()  # ← コンソールにスタックトレースを出力
        raise HTTPException(status_code=500, detail=str(e))
