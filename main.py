from tkinter import*
from tkinter import messagebox
from tkinter import ttk

import tk

janela = Tk ()
janela.attributes('-fullscreen', True)

janela.title("EMPRÉSTIMOS DE LIVROS - ESCOLA MUNICIPAL")
#---------------------------------------------------------------------
#GRID = DIVIDE A TELA EM GRADES/PARTES
#STICK - USAMOS PARA PREENCHER O ITEM NA TELA
#STICK - ESTICAMOS O ITEM PARA NÃO FICAR VAZIO NAS LATERAIS
#STICK - NSEW - NORTE, SUL, LESTE, OESTE

aluno= Label (text="Aluno/Turma", font="Arial 12 bold", fg= "#4B0082")
aluno.grid(row=1, column=0, stick="W")
#campo para digitar as informações
campoDigitadoAluno = Entry(font="Arial 12")
campoDigitadoAluno.grid(row=1, column=1, stick="W")

livro= Label (text="Livro", font="Arial 12 bold", fg= "#4B0082")
livro.grid(row=1, column=2, stick="W")
#campo para digitar as informações
campoDigitadolivro = Entry(font="Arial 12")
campoDigitadolivro.grid(row=1, column=3, stick="W")

retirada= Label (text="Retirada", font="Arial 12 bold", fg= "#4B0082")
retirada.grid(row=1, column=4, stick="W")
#campo para digitar as informações
campoDigitadoretirada = Entry(font="Arial 12")
campoDigitadoretirada.grid(row=1, column=5, stick="W")

devolucao= Label (text="Devolução", font="Arial 12 bold", fg= "#4B0082")
devolucao.grid(row=1, column=6, stick="W")
#campo para digitar as informações
campoDigitadodevolucao = Entry(font="Arial 12")
campoDigitadodevolucao.grid(row=1, column=7, stick="W")

status= Label (text="Status", font="Arial 12 bold", fg= "#4B0082")
status.grid(row=1, column=8, stick="W")
#campo para digitar as informações
campoDigitadostatus = Entry(font="Arial 12")
campoDigitadostatus.grid(row=1, column=9, stick="W")
#---------------------------------------------------------------------


#BOTÕES DA TELA
#FUNÇÃO QUE ADICIONA O ITEM NA TELA
def addItemTela ():

    if str(campoDigitadoAluno.get())=="":
        # Abre a nova janela
        janela2 = Toplevel()
        # Define o título da janela
        janela2.title("ERRO!")
        # Define o tamanho da janela
        janela2.geometry("300x80")
        # Calcula as coordenadas X e Y para centralizar a janela
        largura_janela = 300
        altura_janela = 80
        largura_tela = janela2.winfo_screenwidth()
        altura_tela = janela2.winfo_screenheight()
        x = (largura_tela - largura_janela) // 2
        y = (altura_tela - altura_janela) // 2
        # Defina a posição da janela
        janela2.geometry(f"{largura_janela}x{altura_janela}+{x}+{y}")
        janela2.config(bg="#C0C0C0")
        lbl_mensagem = Label(janela2, text="ATENÇÃO!!!\n Informe o nome do aluno",font= "Arial 14 bold", fg="#FF0000", bg="#C0C0C0" )
        lbl_mensagem.pack()
        # Adiciona um botão para fechar a janela
        botao_fechar = Button(janela2, text="Fechar", command=janela2.destroy)
        botao_fechar.pack()



    elif str(campoDigitadoretirada.get())=="":
        janela2 = Toplevel()
        janela2.title("ERRO!")
        janela2.geometry("300x80")
        largura_janela = 300
        altura_janela = 80
        largura_tela = janela2.winfo_screenwidth()
        altura_tela = janela2.winfo_screenheight()
        x = (largura_tela - largura_janela) // 2
        y = (altura_tela - altura_janela) // 2
        janela2.geometry(f"{largura_janela}x{altura_janela}+{x}+{y}")
        janela2.config(bg="#C0C0C0")
        lbl_mensagem = Label(janela2, text="ATENÇÃO!!!\n Informe a data de retirada", font="Arial 14 bold", fg="#FF0000",bg="#C0C0C0")
        lbl_mensagem.pack()

        botao_fechar = Button(janela2, text="Fechar", command=janela2.destroy)
        botao_fechar.pack()


    elif str(campoDigitadolivro.get())=="":
        janela2 = Toplevel()
        janela2.title("ERRO!")
        janela2.geometry("300x80")
        largura_janela = 300
        altura_janela = 80
        largura_tela = janela2.winfo_screenwidth()
        altura_tela = janela2.winfo_screenheight()
        x = (largura_tela - largura_janela) // 2
        y = (altura_tela - altura_janela) // 2
        janela2.geometry(f"{largura_janela}x{altura_janela}+{x}+{y}")
        janela2.config(bg="#C0C0C0")
        lbl_mensagem = Label(janela2, text="ATENÇÃO!!!\n Informe o livro ! ", font="Arial 14 bold",fg="#FF0000", bg="#C0C0C0")
        lbl_mensagem.pack()

        botao_fechar = Button(janela2, text="Fechar", command=janela2.destroy)
        botao_fechar.pack()


    elif str(campoDigitadodevolucao.get())=="":
        janela2 = Toplevel()
        janela2.title("ERRO!")
        janela2.geometry("300x80")
        largura_janela = 300
        altura_janela = 80
        largura_tela = janela2.winfo_screenwidth()
        altura_tela = janela2.winfo_screenheight()
        x = (largura_tela - largura_janela) // 2
        y = (altura_tela - altura_janela) // 2
        janela2.geometry(f"{largura_janela}x{altura_janela}+{x}+{y}")
        janela2.config(bg="#C0C0C0")
        lbl_mensagem = Label(janela2, text="ATENÇÃO!!!\n Informe a data de devolução! ", font="Arial 14 bold",
                             fg="#FF0000", bg="#C0C0C0")
        lbl_mensagem.pack()

        botao_fechar = Button(janela2, text="Fechar", command=janela2.destroy)
        botao_fechar.pack()



    elif str(campoDigitadostatus.get())=="":

        janela2 = Toplevel()
        janela2.title("ERRO!")
        janela2.geometry("300x80")
        largura_janela = 300
        altura_janela = 130
        largura_tela = janela2.winfo_screenwidth()
        altura_tela = janela2.winfo_screenheight()
        x = (largura_tela - largura_janela) // 2
        y = (altura_tela - altura_janela) // 2
        janela2.geometry(f"{largura_janela}x{altura_janela}+{x}+{y}")
        janela2.config(bg="#C0C0C0")
        lbl_mensagem = Label(janela2, text="ATENÇÃO!!!\n Informe o status\n ABERTO = Emprestado\n OK = Devolvido", font="Arial 14 bold",
                             fg="#FF0000", bg="#C0C0C0")
        lbl_mensagem.pack()

        botao_fechar = Button(janela2, text="Fechar", command=janela2.destroy)
        botao_fechar.pack()



    else:


        dados.insert("", "end",
                     values=(str(campoDigitadoAluno.get()),
                             str(campoDigitadolivro.get()),
                             str(campoDigitadoretirada.get()),
                             str(campoDigitadodevolucao.get()),
                             str(campoDigitadostatus.get())))

        #função abaixo apaga os dados depois de cadastrados
        campoDigitadoretirada.delete(0, "end")
        campoDigitadostatus.delete(0, "end")
        campoDigitadodevolucao.delete(0, "end")
        campoDigitadolivro.delete(0, "end")
        campoDigitadoAluno.delete(0, "end")

botao_adicionar = Button (text="Cadastrar",
                          font=" Arial 12",
                          command= addItemTela,fg="#FFFFF0", bg="#008000")


botao_adicionar.grid(row=2, column=0, columnspan=2, stick="NSEW")


#-------------------------------------------------------------------------------------
#BOTÃO DELETAR
def deletarItemTela():
    #pega o item selecionado
    itemSelecionado = dados.selection()
    #para cada item selecionado dentro dos itens ele vai apagar
    for item in itemSelecionado:
        dados.delete(item)

botao_deletar = Button (text="Deletar",
                          font=" Arial 12",
                          command= deletarItemTela,fg="#FFFFF0", bg="#8B0000")


botao_deletar.grid(row=2, column=2, columnspan=2, stick="NSEW")

#---------------------------------------------------------------------------------
def alterarItemTela():
    # pega o item selecionado na posição 0
    itemSelecionado = dados.selection()[0]
    #substituir o item selecionado
    dados.item(itemSelecionado,
                     values=(str(campoDigitadoAluno.get()),
                             str(campoDigitadolivro.get()),
                             str(campoDigitadoretirada.get()),
                             str(campoDigitadodevolucao.get()),
                             str(campoDigitadostatus.get())))


    # função abaixo apaga os dados depois de cadastrados
    campoDigitadoretirada.delete(0, "end")
    campoDigitadostatus.delete(0, "end")
    campoDigitadodevolucao.delete(0, "end")
    campoDigitadolivro.delete(0, "end")
    campoDigitadoAluno.delete(0, "end")


botao_alterar = Button (text="Alterar",
                          font=" Arial 12",
                          command= alterarItemTela,fg="#FFFFF0", bg="#DAA520")


botao_alterar.grid(row=2, column=4, columnspan=2, stick="NSEW")

# #---------------------------------------------------------------------------------
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
import pandas as pd
from tkinter import messagebox, filedialog  # Importe filedialog aqui

def exportar_para_excel():
    # Abre a caixa de diálogo para escolher o local e o nome do arquivo
    file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Arquivos Excel", "*.xlsx")])

    if file_path:
        # Cria um novo arquivo Excel
        workbook = Workbook()
        planilha = workbook.active

        # Cria um DataFrame com pelo menos uma linha vazia
        dados_dataframe = pd.DataFrame(columns=["Aluno/Turma", "Livro", "Retirada", "Devolução", "Status"])
        dados_dataframe.loc[0] = ["", "", "", "", ""]

        # Preenche o DataFrame com os dados da Treeview, começando da segunda linha
        row_index = 1
        for item in dados.get_children():
            item_values = dados.item(item, "values")
            dados_dataframe.loc[row_index] = item_values
            row_index += 1

        # Escreve os dados do DataFrame na planilha Excel
        for row in dataframe_to_rows(dados_dataframe, index=False, header=True):
            planilha.append(row)

        # Salva o arquivo Excel no local escolhido pelo usuário
        workbook.save(file_path)

        messagebox.showinfo("Exportar para Excel", "Dados exportados com sucesso!")

botao_exportar = Button(text="Exportar",
                        font="Arial 12",
                        command=exportar_para_excel, fg="#FFFFF0", bg="#008080")

botao_exportar.grid(row=2, column=6, columnspan=1, stick="NSEW")



#______________________________________________________________________________________
def carregar_excel():
    # Define os tipos de arquivos que podem ser abertos
    tipo_de_arquivo = [("Excel files", "*.xlsx;*.xls")]
    # Abre a janela para selecionar o arquivo e armazena o caminho na variável "nome_do_arquivo"
    nome_do_arquivo = filedialog.askopenfilename(title="Selecione o arquivo", filetypes=tipo_de_arquivo)

    # Verifica se o usuário selecionou um arquivo
    if nome_do_arquivo:
        try:
            # Lê o arquivo Excel na biblioteca pandas e armazena o conteúdo em um DataFrame
            df = pd.read_excel(nome_do_arquivo)

            # Limpa a Treeview, removendo todas as linhas existentes
            for item in dados.get_children():
                dados.delete(item)

            # Preenche a Treeview com os dados do DataFrame
            for _, row in df.iterrows():
                dados.insert("", "end", values=row.tolist())

        except Exception as e:
            # Exibe uma mensagem de erro se não for possível abrir o arquivo
            messagebox.showerror("Erro", f"Não foi possível abrir o arquivo {e}")

botao_abrir = Button (text="Abrir/Excel",
                          font=" Arial 12",
                          command= carregar_excel,fg="#FFFFF0", bg="#3CB371")


botao_abrir.grid(row=2, column=7, columnspan=1, stick="NSEW")




#---------------------------------------------------------------------
def botao_sair():
    janela.destroy()
botao_sair = Button (text="Sair",
                          font=" Arial 12",
                          command= botao_sair,fg="#FFFFF0", bg="#B22222")


botao_sair.grid(row=2, column=8, columnspan=1, stick="NSEW")

#------------------------------------------------------------------------


#ESTILIZAÇÃO DA TELA
estilodatela = ttk.Style()
estilodatela.theme_use("alt")#há os temas alt, defalt e classic
estilodatela.configure(".", font = "Arial 12")


#---------------------------------------------------------------------
#criando 5 colunas
dados = ttk.Treeview(janela, column=(1,2,3,4,5), show="headings")
#abaixo = centralizando o texto da coluna
dados.column("1", anchor=CENTER)
dados.heading("1", text="Aluno/Turma")

#abaixo = centralizando o texto da coluna
dados.column("2", anchor=CENTER)
dados.heading("2", text="Livro")

#abaixo = centralizando o texto da coluna
dados.column("3", anchor=CENTER)
dados.heading("3", text="Retirada")

#abaixo = centralizando o texto da coluna
dados.column("4", anchor=CENTER)
dados.heading("4", text="Devolução")

#abaixo = centralizando o texto da coluna
dados.column("5", anchor=CENTER)
dados.heading("5", text="Status")

#------------------------------------------------------------------
#criando a tela
dados.grid(row=3, column=0, columnspan=10, stick="NSEW")
#----------------------------------------------------------------
from PIL import Image, ImageTk  # Importe Image e ImageTk do módulo PIL
label_criador = Label(janela, width=19, height= 4, text='Desenvolvido por:\n @EduardoBernardes ', font=('Arial 9'), fg='#000080')
label_criador.place(x= 1000, y=640)


# Carregue a imagem usando o PIL e converta-a para ImageTk
imagem_leitura = Image.open("D:\\PYTHON\\cadastro_simples\\leitura.png")
imagem_tk = ImageTk.PhotoImage(imagem_leitura)

# Crie um rótulo para exibir a imagem
imagem_label = Label(image=imagem_tk)
imagem_label.image = imagem_tk  # Mantenha uma referência à imagem para evitar que seja coletada pelo garbage collector
imagem_label.place(x=350, y=350)  # Coloque o rótulo em uma coluna separada


label_titulo = Label(janela, width=19, height= 4, text='BIBLIOTECA ESCOLAR ', font=('Arial 28 bold'), fg='#000000')
label_titulo.place(x= 420, y=300)

imagem_logo = Image.open("D:\\PYTHON\\cadastro_simples\\logo.png")
imagem_tk = ImageTk.PhotoImage(imagem_logo)
logo_label = Label(image=imagem_tk)
logo_label.image = imagem_tk
logo_label.place(x=450, y=450)





janela.mainloop()