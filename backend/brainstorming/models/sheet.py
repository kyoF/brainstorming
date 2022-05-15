from enum import unique
from sqlalchemy import Column, Integer, String

from brainstorming.database import Base


class Sheet(Base):
    __tablename__ = 'sheet'

    id = Column(Integer, primary_key=True)
    sheet_id = Column(Integer, unique=True, nullable=False)
    divide_area = Column(Integer, nullable=False)
    formula = Column(String(255))
