from services.cliente_service import cadastrar_cliente, listar_clientes
from services.mesa_service import reservar_mesa
from services.pedido_service import fazer_pedido, cancelar_pedido, alterar_pedido, listar_pedidos
from services.reserva_service import visualizar_reservas
from config import Base, engine

# Cria as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

def exibir_menu_principal():
    print("\n=== Menu de Gerenciamento do Restaurante ===")
    print("1. Gerenciar Clientes")
    print("2. Gerenciar Mesas")
    print("3. Gerenciar Reservas")
    print("4. Gerenciar Pedidos")
    print("5. Sair")

def exibir_menu_clientes():
    print("\n=== Gerenciamento de Clientes ===")
    print("1. Cadastrar Cliente")
    print("2. Listar Clientes")
    print("3. Voltar")

def exibir_menu_mesas():
    print("\n=== Gerenciamento de Mesas ===")
    print("1. Adicionar Mesas")
    print("2. Listar Mesas Disponíveis")
    print("3. Voltar")

def exibir_menu_reservas():
    print("\n=== Gerenciamento de Reservas ===")
    print("1. Reservar Mesa")
    print("2. Visualizar Reservas")
    print("3. Voltar")

def exibir_menu_pedidos():
    print("\n=== Gerenciamento de Pedidos ===")
    print("1. Fazer Pedido")
    print("2. Cancelar Pedido")
    print("3. Alterar Pedido")
    print("4. Listar Pedidos")
    print("5. Voltar")

def main():
    while True:
        exibir_menu_principal()
        opcao = int(input("Escolha uma opção (1-5): "))

        if opcao == 1:
            exibir_menu_clientes()
            opcao_cliente = int(input("Escolha uma opção: "))
            if opcao_cliente == 1:
                cpf = int(input("Digite o cpf do cliente: "))
                nome = input("Digite o nome do cliente: ")
                email = input("Digite o email do cliente: ")
                cadastrar_cliente(cpf, nome, email)
            elif opcao_cliente == 2:
                listar_clientes()

        elif opcao == 2:
            exibir_menu_mesas()
            opcao_mesa = int(input("Escolha uma opção: "))
            if opcao_mesa == 1:
                adicionar_mesas()
            elif opcao_mesa == 2:
                listar_mesas_disponiveis()

        elif opcao == 3:
            exibir_menu_reservas()
            opcao_reserva = int(input("Escolha uma opção: "))
            if opcao_reserva == 1:
                cliente_cpf = int(input("Digite o CPF do cliente: "))
                mesa_id = int(input("Digite o ID da mesa: "))
                data_reserva_str = input("Digite a data da reserva (YYYY-MM-DD HH:MM): ")
                reservar_mesa(cliente_cpf, mesa_id, data_reserva_str)
            elif opcao_reserva == 2:
                visualizar_reservas()

        elif opcao == 4:
            exibir_menu_pedidos()
            opcao_pedido = int(input("Escolha uma opção: "))
            if opcao_pedido == 1:
                reserva_id = int(input("Digite o ID da reserva: "))
                descricao = input("Digite a descrição do pedido: ")
                fazer_pedido(reserva_id, descricao)
            elif opcao_pedido == 2:
                pedido_id = int(input("Digite o ID do pedido a ser cancelado: "))
                cancelar_pedido(pedido_id)
            elif opcao_pedido == 3:
                pedido_id = int(input("Digite o ID do pedido a ser alterado: "))
                nova_descricao = input("Digite a nova descrição do pedido: ")
                alterar_pedido(pedido_id, nova_descricao)
            elif opcao_pedido == 4:
                listar_pedidos()

        elif opcao == 5:
            print("Saindo... Até logo!")
            break

if __name__ == "__main__":
    main()
