from sqlalchemy import Column, Integer, Boolean
from config import Base


class Mesa(Base):
    __tablename__ = 'mesas'

    id = Column(Integer, primary_key=True, index=True)
    numero = Column(Integer, unique=True, nullable=False)
    disponivel = Column(Boolean, default=True)
