from sqlalchemy.orm import Session
from models import ProductMaster, Transaction, TransactionDetail
from schemas import PurchaseRequest

TAX_RATE = 0.1

def get_product_by_code(db: Session, code: str):
    return db.query(ProductMaster).filter(ProductMaster.code == code).first()

def register_purchase(db: Session, req: PurchaseRequest):
    total = 0
    total_ex_tax = 0

    trx = Transaction(
        emp_cd=req.emp_cd,
        store_cd=req.store_cd,
        pos_no=req.pos_no,
        total_amt=0,
        ttl_amt_ex_tax=0
    )
    db.add(trx)
    db.flush()

    for idx, item in enumerate(req.items, start=1):
        total += item.prd_price
        tax_free_price = int(item.prd_price / (1 + TAX_RATE))
        total_ex_tax += tax_free_price

        detail = TransactionDetail(
            trd_id=trx.trd_id,
            dtl_id=idx,
            prd_id=item.prd_id,
            prd_code=item.prd_code,
            prd_name=item.prd_name,
            prd_price=item.prd_price,
            tax_cd="10"
        )
        db.add(detail)

    trx.total_amt = total
    trx.ttl_amt_ex_tax = total_ex_tax

    db.commit()
    return total, total_ex_tax
