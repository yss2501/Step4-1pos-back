from sqlalchemy.orm import Session
from models import ProductMaster, Transaction, TransactionDetail
from schemas import PurchaseRequest

def get_product_by_code(db: Session, code: str):
    return db.query(ProductMaster).filter(ProductMaster.code == code).first()

def register_purchase(db: Session, req: PurchaseRequest):
    total = sum(item.prd_price for item in req.items)

    trx = Transaction(
        emp_cd=req.emp_cd,
        store_cd=req.store_cd,
        pos_no=req.pos_no,
        total_amt=total
    )
    db.add(trx)
    db.flush()  # trd_id 取得

    for idx, item in enumerate(req.items, start=1):
        detail = TransactionDetail(
            trd_id=trx.trd_id,
            dtl_id=idx,
            prd_id=item.prd_id,
            prd_code=item.prd_code,
            prd_name=item.prd_name,
            prd_price=item.prd_price
        )
        db.add(detail)

    db.commit()
    return total
