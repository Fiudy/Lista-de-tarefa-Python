import customtkinter
from tkinter import *
from tkcalendar import DateEntry
import mysql.connector
from mysql.connector import Error
import tkinter as tk
from tktimepicker import SpinTimePickerModern, SpinTimePickerOld
from tktimepicker import constants

import os

# Conexão com o banco de dados
def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",  # Substitua pelo seu host
            user="root",  # Substitua pelo seu usuário
            passwd="1234",  # Substitua pela sua senha
            database="Tarefas"  # Substitua pelo nome do seu banco de dados
        )
        print("Conexão com o MySQL foi bem sucedida")
    except Error as e:
        print(f"O erro '{e}' ocorreu")

    return connection

# Função para executar uma query no banco de dados
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executada com sucesso")
    except Error as e:
        print(f"O erro '{e}' ocorreu")



def salvar():
    tarefa_titulo = entrada_titulo.get()
    tarefa_datainicio= entrada_data.get_date() 
    tarefa_status = status.get()
    tarefa_descricao = descricao_texto.get("1.0", "end-1c").strip()
    # tarefa_datatermino = entrada_data.get_date()

    # Conecta ao banco de dados e salva a tarefa
    connection = create_connection()
    query = f"INSERT INTO tarefas (titulo, descricao, status, data_inicio) VALUES ('{tarefa_titulo}', '{tarefa_descricao}', '{tarefa_status}', '{tarefa_datainicio}')"

    execute_query(connection, query)

    # Atualiza a lista de tarefas
    atualizar_tarefas()
    
    # Função para atualizar a lista de tarefas
def atualizar_tarefas():
    # Limpa o frame de tarefas
    for widget in frameesquerda.winfo_children():
        widget.destroy()

    # Busca tarefas do banco de dados
    connection = create_connection()
    query = "SELECT * FROM tarefas"
    tarefas = fetch_tasks(connection, query)

    # Adiciona tarefas ao frame
    for tarefa in tarefas:
        tarefa_label = customtkinter.CTkLabel(master=frameesquerda, text=tarefa[1], font=('Roboto', 14))  # Substitua o índice 1 pelo índice da coluna de texto na sua tabela
        tarefa_label.pack(pady=5)


# Função para filtrar tarefas
def filtrar_tarefas():
    # Limpa o frame de tarefas
    for widget in frameesquerda.winfo_children():
        widget.destroy()

     # Busca todas as tarefas do banco de dados
    connection = create_connection()
    select_tarefas_query = "SELECT * from tarefas"
    tarefas = fetch_tasks(connection, select_tarefas_query)
    # Adiciona todas as tarefas à lista de tarefas
    for tarefa in tarefas:
        tarefa_label = customtkinter.CTkLabel(master=frameesquerda, text=tarefa[1], font=('Roboto', 12))  
        tarefa_label.pack()
    
def fetch_tasks(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"O erro '{e}' ocorreu")





# Configuração inicial
print(os.getcwd())

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

janela = customtkinter.CTk()
janela.geometry('900x1000')
janela.title('Lista de Tarefas')
janela.iconbitmap('icon.ico')
janela.resizable(False, False)

# Frame da direita para adicionar tarefa
framedireita = customtkinter.CTkFrame(master=janela, width=450, height=550)
framedireita.pack(side=RIGHT, fill=BOTH, expand=True, padx=20, pady=20)

fonte = ('Roboto', 24)
label = customtkinter.CTkLabel(master=framedireita, text='Adicione sua Tarefa', font=fonte, fg_color='transparent')
label.pack(pady=8)

# Entrada de texto para a tarefa
entrada_titulo = customtkinter.CTkEntry(master=framedireita, placeholder_text="Informe a tarefa", width=300, font=fonte)
entrada_titulo.pack(pady=14)

# Seleção de data
data_label= customtkinter.CTkLabel(master=framedireita, text="Adicione a Data:", font=('Roboto', 20), fg_color='transparent')
data_label.pack(pady=10)
entrada_data = DateEntry(master=framedireita, width=16, background="darkblue", foreground="white", borderwidth=2)
entrada_data.pack(pady=12)

# Seleção de Status
status_label = customtkinter.CTkLabel(master=framedireita, text="Status:", font=('Roboto', 20), fg_color='transparent')
status_label.pack(pady=14)
status = StringVar(value="A fazer")
todos_status = ["Concluído", "A fazer", "Em andamento"]
menu_status = customtkinter.CTkOptionMenu(master=framedireita, variable=status, values=todos_status)
menu_status.pack(pady=15)

# Descrição detalhada
descricao_label = customtkinter.CTkLabel(master=framedireita, text="Descrição:", font=('Roboto', 14))
descricao_label.pack(pady=10)
descricao_texto = Text(master=framedireita, height=5, width=40)
descricao_texto.pack(pady=10)

# Cria o botão
botao = customtkinter.CTkButton(master=framedireita, text="Adicionar tarefa")
botao.configure(command=salvar)
botao.pack()


# Frame da esquerda para filtros e lista de tarefas
frameesquerda = customtkinter.CTkFrame(master=janela, width=450, height=550)
frameesquerda.pack(side=LEFT, fill=BOTH, expand=True, padx=20, pady=20)

# Filtros
filtro_label = customtkinter.CTkLabel(master=frameesquerda, text="Filtros", font=('Roboto', 16))
filtro_label.pack(pady=10)

# Filtro por data
data_filtro_label = customtkinter.CTkLabel(master=frameesquerda, text="Filtrar por Data:", font=('Roboto', 14))
data_filtro_label.pack(pady=5)
data_filtro = DateEntry(master=frameesquerda, width=16, background="darkblue", foreground="white", borderwidth=2)
data_filtro.pack(pady=5)

# Filtro por status
status_filtro_label = customtkinter.CTkLabel(master=frameesquerda, text="Filtrar por status:", font=('Roboto', 14))
status_filtro_label.pack(pady=5)
status_filtro = StringVar(value="A fazer")
todos_status_filtro = ["Concluído", "A fazer", "Em andamento"]
menu_status_filtro = customtkinter.CTkOptionMenu(master=frameesquerda, variable=status_filtro, values=todos_status_filtro)
menu_status_filtro.pack(pady=5)

# Lista de tarefas criadas
frameesquerda = customtkinter.CTkFrame(master=frameesquerda, width=400, height=400)
frameesquerda.pack(pady=10, fill=BOTH, expand=True)

# Adicione um botão para aplicar os filtros
botao_filtrar = customtkinter.CTkButton(master=frameesquerda, text="Aplicar Filtros", command=filtrar_tarefas)
botao_filtrar.pack(pady=20)

# Chama a função para atualizar a lista de tarefas quando o programa inicia
atualizar_tarefas()

janela.mainloop()
