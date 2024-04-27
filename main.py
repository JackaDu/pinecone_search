from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from index import search
import crud, models, schemas
from database import SessionLocal, engine
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/search/{word}")
def find_companies(word: str, db: Session = Depends(get_db)):
    loan_number = search(word)
    loan_record = crud.get_loan(db, loan_number=loan_number)
    return {
        "res": loan_record
    }
