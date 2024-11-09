from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config import Base

class Pedido(Base):
    __tablename__ = 'pedidos'

    id = Column(Integer, primary_key=True, index=True)
    reserva_id = Column(Integer, ForeignKey('reservas.id'))
    descricao = Column(String, nullable=False)
    reserva = relationship("Reserva")
