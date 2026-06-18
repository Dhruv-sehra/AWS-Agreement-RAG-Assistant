from sqlalchemy import func
from database import SessionLocal
from models import QueryLog


def get_analytics():

    db = SessionLocal()

    most_frequent = (
        db.query(
            QueryLog.question,
            func.count(QueryLog.id)
        )
        .group_by(QueryLog.question)
        .order_by(func.count(QueryLog.id).desc())
        .limit(5)
        .all()
    )

    no_answer = (
        db.query(QueryLog)
        .filter(QueryLog.answer_found == 0)
        .all()
    )

    avg_latency = (
        db.query(
            func.avg(QueryLog.latency)
        )
        .scalar()
    )

    db.close()

    return {
        "most_frequent_questions": [
            {
                "question": q,
                "count": count
            }
            for q, count in most_frequent
        ],

        "no_answer_queries": [
            row.question
            for row in no_answer
        ],

        "average_latency": avg_latency
    }