from services.cliente_service import cadastrar_cliente
from services.mesa_service import reservar_mesa, adicionar_mesas, listar_mesas_disponiveis
from services.pedido_service import fazer_pedido, cancelar_pedido, alterar_pedido
from services.reserva_service import visualizar_reservas
from config import Base, engine

# Cria as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

def exibir_menu():
    print("\n=== Menu de Gerenciamento do Restaurante ===")
    print("1. Cadastrar Cliente")
    print("2. Adicionar 50 Mesas")
    print("3. Listar Mesas")
    print("4. Reservar Mesa")
    print("5. Fazer Pedido")
    print("6. Cancelar Pedido")
    print("7. Alterar Pedido")
    print("8. Visualizar Reservas")
    print("9. Sair")

def main():
    while True:
        exibir_menu()
        opcao = int(input("Escolha uma opção (1-7): "))

        if opcao == 1:
            cpf = int(input("Digite o cpf do cliente: "))
            nome = input("Digite o nome do cliente: ")
            email = input("Digite o email do cliente: ")
            cadastrar_cliente(cpf, nome, email)

        elif opcao == 2:
            adicionar_mesas()

        elif opcao == 3:
            listar_mesas_disponiveis()

        elif opcao == 4:
            cliente_cpf = int(input("Digite o CPF do cliente: "))
            mesa_id = int(input("Digite o ID da mesa: "))
            data_reserva_str = input("Digite a data da reserva (YYYY-MM-DD HH:MM): ")
            reservar_mesa(cliente_cpf, mesa_id, data_reserva_str)

        elif opcao == 5:
            reserva_id = int(input("Digite o ID da reserva: "))
            descricao = input("Digite a descrição do pedido: ")
            fazer_pedido(reserva_id, descricao)

        elif opcao == 6:
            pedido_id = int(input("Digite o ID do pedido a ser cancelado: "))
            cancelar_pedido(pedido_id)

        elif opcao == 7:
            pedido_id = int(input("Digite o ID do pedido a ser alterado: "))
            nova_descricao = input("Digite a nova descrição do pedido: ")
            alterar_pedido(pedido_id, nova_descricao)

        elif opcao == 8:
            visualizar_reservas()

        elif opcao == 9:
            print("Saindo... Até logo!")
            break

if __name__ == "__main__":
    main()
