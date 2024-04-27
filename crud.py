from sqlalchemy.orm import Session

import models, schemas


def get_loan(db: Session, loan_number: str):
    return db.query(models.Loan).filter(models.Loan.LoanNumber == loan_number).first()

