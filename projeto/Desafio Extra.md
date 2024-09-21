### Desafio Extra: Cadastro de Contas

Você deve implementar um sistema simples de controle de clientes e contas em Python. O sistema deve permitir que a operadora possa cadastrar, listar, atualizar ou deletar clientes, bem como cadastrar e listar contas vinculadas a clientes ativos.

### Especificações do Sistema:

1. **Menu Principal:**
    - O sistema deve exibir um menu principal com as seguintes opções:
        
        ```csharp
        [1] Gerenciar Clientes
        [2] Gerenciar Contas
        [3] Sair
        ```

2. **Menu de Clientes:**
    - O sistema deve exibir um menu para gerenciamento de clientes com as seguintes opções:
        
        ```csharp
        [1] Cadastrar Cliente
        [2] Listar Clientes
        [3] Atualizar Cliente
        [4] Inativar Cliente
        [5] Voltar ao Menu Principal
        ```

3. **Menu de Contas:**
    - O sistema deve exibir um menu para gerenciamento de contas com as seguintes opções:
        
        ```csharp
        [1] Cadastrar Conta
        [2] Listar Contas
        [3] Voltar ao Menu Principal
        ```

4. **Funcionalidades:**
    - **Cadastrar Cliente ([1] no Menu de Clientes)**:
        - O usuário deve informar os dados do cliente (nome, email, telefone).
        - O cliente deve ser adicionado à lista de clientes.
    - **Listar Clientes ([2] no Menu de Clientes)**:
        - Exiba todos os clientes cadastrados.
        - Exiba o status do cliente (Ativo/Inativo).
    - **Atualizar Cliente ([3] no Menu de Clientes)**:
        - O usuário deve informar o ID do cliente a ser atualizado.
        - O usuário deve informar os novos dados do cliente.
        - Atualize os dados do cliente na lista.
    - **Inativar Cliente ([4] no Menu de Clientes)**:
        - O usuário deve informar o ID do cliente a ser inativado.
        - Atualize o status do cliente para inativo.
    - **Cadastrar Conta ([1] no Menu de Contas)**:
        - O usuário deve informar o ID do cliente ao qual a conta será vinculada.
        - Verifique se o cliente está ativo.
        - O usuário deve informar o número da conta e o saldo inicial.
        - A conta deve ser adicionada à lista de contas.
    - **Listar Contas ([2] no Menu de Contas)**:
        - Exiba todas as contas cadastradas, juntamente com as informações do cliente vinculado.
    - **Sair ([3] no Menu Principal)**:
        - Encerre o programa.

5. **Validações:**
    - Valide se as entradas são válidas e exiba mensagens de erro apropriadas para cada situação:
        - "Opção inválida! Por favor, selecione uma opção válida."
        - "Cliente não encontrado."
        - "Cliente inativo. Não é possível cadastrar conta."
        - "Cliente cadastrado com sucesso!"
        - "Cliente atualizado com sucesso!"
        - "Cliente inativado com sucesso!"
        - "Conta cadastrada com sucesso!"

### Exemplo de Execução:

```csharp
[1] Gerenciar Clientes
[2] Gerenciar Contas
[3] Sair

=> 1
[1] Cadastrar Cliente
[2] Listar Clientes
[3] Atualizar Cliente
[4] Inativar Cliente
[5] Voltar ao Menu Principal

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
[5] Voltar ao Menu Principal

=> 5
[1] Gerenciar Clientes
[2] Gerenciar Contas
[3] Sair

=> 2
[1] Cadastrar Conta
[2] Listar Contas
[3] Voltar ao Menu Principal

=> 1
Cadastrar Conta
Digite o ID do cliente: 1
Digite o número da conta: 12345
Digite o saldo inicial: 1000
Conta cadastrada com sucesso!

[1] Cadastrar Conta
[2] Listar Contas
[3] Voltar ao Menu Principal

=> 2
Listar Contas
Número da Conta: 12345 | Saldo: 1000 | Cliente: Grace Hopper | Status: Ativo

[1] Cadastrar Conta
[2] Listar Contas
[3] Voltar ao Menu Principal

=> 3
[1] Gerenciar Clientes
[2] Gerenciar Contas
[3] Sair

=> 3
Programa finalizado