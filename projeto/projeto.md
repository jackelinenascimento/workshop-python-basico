### Desafio: Banco CloudGirls

Você deve implementar um sistema simples de controle de clientes em Python. O sistema deve permitir que a operadora possa cadastrar, listar, atualizar ou deletar clientes.

### Especificações do Sistema:

1. **Menu Principal:**
    - O sistema deve exibir um menu com as seguintes opções:
        
        ```csharp
        [1] Cadastrar Cliente
        [2] Listar Clientes
        [3] Atualizar Cliente
        [4] Inativar Cliente
        [5] Sair
        ```
        
2. **Funcionalidades:**
    - **Cadastrar Cliente ([1])**:
        - O usuário deve informar os dados do cliente (nome, email, telefone).
        - O cliente deve ser adicionado à lista de clientes.
    - **Listar Clientes ([2])**:
        - Exiba todos os clientes cadastrados.
        - Exiba o status do cliente (Ativo/Inativo).
    - **Atualizar Cliente ([3])**:
        - O usuário deve informar o ID do cliente a ser atualizado.
        - O usuário deve informar os novos dados do cliente.
        - Atualize os dados do cliente na lista.
    - **Inativar Cliente ([4])**:
        - O usuário deve informar o ID do cliente a ser inativado.
        - Atualize o status do cliente para inativo.
    - **Sair ([5])**:
        - Encerre o programa.

3. **Validações:**
    - Valide se as entradas são válidas e exiba mensagens de erro apropriadas para cada situação:
        - "Opção inválida! Por favor, selecione uma opção válida."
        - "Cliente não encontrado."
        - "Cliente cadastrado com sucesso!"
        - "Cliente atualizado com sucesso!"
        - "Cliente inativado com sucesso!"

### Exemplo de Execução:

```csharp
[1] Cadastrar Cliente
[2] Listar Clientes
[3] Atualizar Cliente
[4] Inativar Cliente
[5] Sair

=> 1
Cadastrar Cliente
Nome: Ada Lovelace
Email: ada@lovelace.com
Telefone: 123456789
Cliente cadastrado com sucesso!

[1] Cadastrar Cliente
[2] Listar Clientes
[3] Atualizar Cliente
[4] Inativar Cliente
[5] Sair

=> 2
Listar Clientes
Id: 1 | Nome: Grace Hopper | Email: grace@hopper.com | Telefone: 123456789 | Status: Ativo
Id: 2 | Nome: Ada Lovelace | Email: ada@lovelace.com | Telefone: 123456789 | Status: Ativo

[1] Cadastrar Cliente
[2] Listar Clientes
[3] Atualizar Cliente
[4] Inativar Cliente
[5] Sair

=> 3
Atualizar Cliente
Digite o id do cliente que deseja atualizar: 2
Nome: Ada Byron
Email: ada@byron.com
Telefone: 987654321
Cliente atualizado com sucesso!

[1] Cadastrar Cliente
[2] Listar Clientes
[3] Atualizar Cliente
[4] Inativar Cliente
[5] Sair

=> 4
Inativar Cliente
Digite o id do cliente que deseja inativar: 2
Cliente inativado com sucesso!

[1] Cadastrar Cliente
[2] Listar Clientes
[3] Atualizar Cliente
[4] Inativar Cliente
[5] Sair

=> 5
Programa finalizado