# Documentação

Este programa é uma aplicação de console para gerenciar as operações de um restaurante, incluindo cadastro de clientes, reservas de mesas, pedidos de clientes e controle de disponibilidade de mesas.

<br>

## Funcionalidades Disponíveis:

1. **Cadastrar Cliente**: O usuário pode cadastrar clientes fornecendo o nome, CPF e e-mail do cliente.
2. **Adicionar Mesas**: Uma opção para adicionar múltiplas mesas ao banco de dados.
3. **Listar Mesas Disponíveis**: Exibe todas as mesas atualmente disponíveis para reserva.
4. **Reservar Mesa**: Permite que o usuário faça uma reserva para um cliente em uma mesa específica. A mesa fica reservada para o cliente por um período de duas horas.
5. **Fazer Pedido**: Permite registrar um pedido associado a uma reserva existente.
6. **Cancelar Pedido**: O usuário pode cancelar pedidos feitos anteriormente.
7. **Alterar Pedido**: Permite que o usuário modifique um pedido existente.
8. **Visualizar Reservas**: Exibe todas as reservas feitas no restaurante, com detalhes do cliente, mesa e data da reserva.
9. **Sair**: Encerra o programa.

<br>

## Diagrama de Relacionamento (ERD)

O diagrama a seguir ilustra o relacionamento entre as entidades no banco de dados:

Clientes possui uma relação de 1 para muitos com Reservas (um cliente pode ter várias reservas).
Mesas possui uma relação de 1 para muitos com Reservas (uma mesa pode ter várias reservas ao longo do tempo).
Reservas possui uma relação de 1 para 1 com Pedidos (uma reserva possui apenas um pedido associado).

