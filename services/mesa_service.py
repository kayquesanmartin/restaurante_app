from datetime import datetime
from models.mesa import Mesa
from models.cliente import Cliente
from config import get_session
from models.reserva import Reserva

def reservar_mesa(cliente_cpf, mesa_id, data_reserva_str):
    session = get_session()
    try:
        # Valida se o CPF existe
        cliente = session.query(Cliente).filter(Cliente.cpf == cliente_cpf).first()
        if not cliente:
            print(f"Erro: Cliente com CPF {cliente_cpf} não encontrado.")
            return

        data_reserva = datetime.strptime(data_reserva_str, "%Y-%m-%d %H:%M")
        mesa = session.query(Mesa).filter(Mesa.id == mesa_id, Mesa.disponivel == True).first()

        if mesa:
            nova_reserva = Reserva(cliente_cpf=cliente_cpf, mesa_id=mesa_id, data_reserva=data_reserva)
            session.add(nova_reserva)
            mesa.disponivel = False
            session.commit()
            print(f"Mesa {mesa_id} reservada com sucesso para o cliente {cliente_cpf} na data {data_reserva}.")
        else:
            print("Mesa indisponível.")
    except Exception as e:
        session.rollback()
        print(f"Ocorreu um erro ao tentar reservar a mesa: {e}")
    finally:
        session.close()
