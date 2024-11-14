from models.cliente import Cliente
from config import get_session

def cadastrar_cliente(cpf, nome, email):
    session = get_session()
    try:
        cliente_existente = session.query(Cliente).filter(Cliente.cpf == cpf).first()
        if cliente_existente:
            print(f"Cliente com CPF {cpf} já cadastrado.")
        else:
            novo_cliente = Cliente(cpf=cpf, nome=nome, email=email)
            session.add(novo_cliente)
            session.commit()
            print("Cliente cadastrado com sucesso.")
    except Exception as e:
        session.rollback()
        print(f"Ocorreu um erro ao cadastrar o cliente: {e}")
    finally:
        session.close()

def listar_clientes():
    session = get_session()
    try:
        clientes = session.query(Cliente).all()
        if clientes:
            print("Clientes cadastrados:")
            for cliente in clientes:
                print(f"CPF: {cliente.cpf}, Nome: {cliente.nome}, Email: {cliente.email}")
        else:
            print("Nenhum cliente cadastrado.")
    finally:
        session.close()
