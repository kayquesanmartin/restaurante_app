from models.reserva import Reserva
from config import get_session

def visualizar_reservas():
    session = get_session()
    reservas = session.query(Reserva).all()

    for reserva in reservas:
        print(f"ID: {reserva.id}, Cliente: {reserva.cliente_cpf}, Mesa: {reserva.mesa_id}, Data: {reserva.data_reserva}")

    session.close()
