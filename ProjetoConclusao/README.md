# Lista de Tarefas

Este é um aplicativo simples de lista de tarefas com interface gráfica desenvolvida em Python usando o módulo customtkinter para uma experiência visual personalizada. O aplicativo permite adicionar novas tarefas, editar tarefas existentes, filtrar tarefas por data e status, marcar tarefas como concluídas e remover tarefas. Tudo isso feito usando persistência de dados com mysql.

## Sobre o Projeto

Esse projeto é foi feito para servir de conclusão para o curso de programação Fullstack na Infinity School. O desenvolvimento dele levou cerca de quase um mês. Está implementado de forma completa, servindo os requisitos passados. 

Esse Projeto foi desenvolvido por mim, Luis Guilherme de Oliveira Carvalho.

## Funcionalidades

1. **Adicionar Tarefa**
   - Insira o título da tarefa, a data de início e uma descrição detalhada.
   - O status da tarefa será automaticamente definido com base na data de início. Se você colocou para uma data atual, o status da tarefá será: "Em andamento". Caso seja para dias posteriores, o status da tarefa será: "A fazer"

2. **Editar Tarefa**
   - Clique em qualquer tarefa da lista para abrir uma janela de edição.
   - Ao abrir a janela de edição você terá acesso à data de início, e se a tarefa já estiver concluída, verá também a data de término.
   - Edite o título e a descrição da tarefa e salve as alterações.

3. **Filtrar Tarefas**
   - Filtrar tarefas por data específica e/ou por status (Concluído, A fazer, Em andamento).
   - Aplique e limpe os filtros facilmente.
   - Se filtrar por Todos ele não vai mostrar todas as tarefas independente da data
   - Obs: Se for filtrar pelo status "A fazer", mude a data para o dia posterior que você selecionou

4. **Marcar Tarefa**
   - Marque uma tarefa como concluída através de uma caixa de seleção.
   - O status e a data de término serão atualizados automaticamente.

5. **Remover Tarefa**
   - Remova uma tarefa da lista.

## Configuração

### Pré-requisitos

- Certifique-se de ter Python instalado em seu sistema.
- Instale as seguintes dependências Python:
```bash
pip install customtkinter tkcalendar mysql-connector-python
pip install customtkinter 
pip install tkcalendar
pip install mysql-connector-python
```

### Execução do Programa

1. Abra o arquivo `main.py` em seu editor de código Python.
2. Atualize as credenciais do banco de dados em `create_connection()` no arquivo main.py
3. Execute o programa:

```bash
python main.py
```



