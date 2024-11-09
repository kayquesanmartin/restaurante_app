from sqlalchemy import Column, Integer, String
from config import Base

class Cliente(Base):
    __tablename__ = 'clientes'

    cpf = Column(Integer, primary_key=True, index=False)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
