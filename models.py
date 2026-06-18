from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    DateTime
)

from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()


class QueryLog(Base):

    __tablename__ = "query_logs"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    question = Column(String)

    answer = Column(String)

    answer_found = Column(Integer)

    latency = Column(Float)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )
