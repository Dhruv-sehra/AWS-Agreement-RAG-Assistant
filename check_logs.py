from database import SessionLocal
from models import QueryLog

db = SessionLocal()

rows = db.query(QueryLog).all()

for row in rows:
    print(row.question)