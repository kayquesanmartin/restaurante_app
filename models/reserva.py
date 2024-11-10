from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from config import Base


class Reserva(Base):
    __tablename__ = 'reservas'

    id = Column(Integer, primary_key=True, index=True)
    cliente_cpf = Column(Integer, ForeignKey('clientes.cpf'))
    mesa_id = Column(Integer, ForeignKey('mesas.id'))
    data_reserva = Column(DateTime, nullable=False)
    cliente = relationship("Cliente")
    mesa = relationship("Mesa")
