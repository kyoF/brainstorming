from operator import index
from sqlalchemy import Column, Integer, String, Text, ForeignKey

from brainstorming.database import Base


class Postit(Base):
    __tablename__ = 'postit'

    id = Column(Integer, primary_key=True)
    postit_id = Column(Integer, unique=True, nullable=False)
    title = Column(String(255), nullable=False)
    remarks = Column(Text)
    xaxis = Column(Integer, nullable=False)
    yaxis = Column(Integer, nullable=False)
    sheet_id = Column(Integer, ForeignKey('sheet.sheet_id'), nullable=False)
