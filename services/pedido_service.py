from models.pedido import Pedido
from config import get_session

def fazer_pedido(reserva_id, descricao):
    session = get_session()
    pedido = Pedido(reserva_id=reserva_id, descricao=descricao)
    session.add(pedido)
    session.commit()
    session.close()
    print("Pedido realizado com sucesso.")

def cancelar_pedido(pedido_id):
    session = get_session()
    pedido = session.query(Pedido).filter(Pedido.id == pedido_id).first()

    if pedido:
        session.delete(pedido)
        session.commit()
        print("Pedido cancelado com sucesso.")
    else:
        print("Pedido não encontrado.")
    session.close()

def alterar_pedido(pedido_id, nova_descricao):
    session = get_session()
    pedido = session.query(Pedido).filter(Pedido.id == pedido_id).first()

    if pedido:
        pedido.descricao = nova_descricao
        session.commit()
        print("Pedido alterado com sucesso.")
    else:
        print("Pedido não encontrado.")
    session.close()
