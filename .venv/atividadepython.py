from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QHBoxLayout,
    QTableWidget, QTableWidgetItem)

from PyQt6.QtGui import QPixmap, QIcon
from sys import argv



# TELA 2 - Lista

class TelaDados(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Voluntários Cadastrados")
        self.setGeometry(250, 100, 900, 500)

        layout = QVBoxLayout()

        titulo = QLabel("Voluntários Cadastrados")
        titulo.setStyleSheet("""
            font-size: 22px;
            font-weight: bold;
        """)

        self.tabela = QTableWidget()
        self.tabela.setColumnCount(3)

        cabecalho = ["Nome", "E-mail", "Senha"]
        self.tabela.setHorizontalHeaderLabels(cabecalho)

        self.tabela.setRowCount(20)

        layout.addWidget(titulo)
        layout.addWidget(self.tabela)

        self.setLayout(layout)

        self.linha = 0

    def adicionar_dados(self, nome, email, senha):

        self.tabela.setItem(
            self.linha, 0,
            QTableWidgetItem(nome)
        )

        self.tabela.setItem(
            self.linha, 1,
            QTableWidgetItem(email)
        )

        self.tabela.setItem(
            self.linha, 2,
            QTableWidgetItem(senha)
        )

        self.linha += 1


# Tela 1 - Cadastro

class TelaCadastro(QWidget):

    def __init__(self):
        super().__init__()

        self.tela_dados = TelaDados()

        self.setWindowTitle("Cadastro de Voluntários")
        self.setGeometry(100, 50, 1400, 900)

        self.setWindowIcon(QIcon("angora.jpg"))

        layout_principal = QHBoxLayout()

      
        # Coluna esquerda----imagem
       
        label_foto = QLabel()

        pixmap = QPixmap("CAT.jpg")

        label_foto.setPixmap(pixmap)
        label_foto.setScaledContents(True)
        label_foto.setFixedWidth(700)

        # Coluna direita*****
    
        coluna_direita = QVBoxLayout()

        titulo = QLabel("Seja Voluntário")
        titulo.setStyleSheet("""
            font-size: 30px;
            color: orange;
            font-weight: bold;""")

        subtitulo = QLabel("e ajude um pet a encontrar um lar")

        subtitulo.setStyleSheet("""
            font-size: 18px;
            color: #444;""")

        # Nome
        label_nome = QLabel("Seu nome")
        self.edit_nome = QLineEdit()

        # Email
        label_email = QLabel("Seu e-mail")
        self.edit_email = QLineEdit()

        # Senha
        label_senha = QLabel("Escolha uma senha")
        self.edit_senha = QLineEdit()
        self.edit_senha.setEchoMode(QLineEdit.EchoMode.Password)

        # Botão cadastrar
        btn_cadastrar = QPushButton("Cadastrar")

        btn_cadastrar.setStyleSheet("""
            QPushButton{
                background-color: orange;
                color: white;
                font-size:18px;
                font-weight:bold;
                padding:15px;""")

        btn_cadastrar.clicked.connect(self.cadastrar_voluntario)

        coluna_direita.addStretch()

        coluna_direita.addWidget(titulo)
        coluna_direita.addWidget(subtitulo)

        coluna_direita.addSpacing(30)

        coluna_direita.addWidget(label_nome)
        coluna_direita.addWidget(self.edit_nome)

        coluna_direita.addWidget(label_email)
        coluna_direita.addWidget(self.edit_email)

        coluna_direita.addWidget(label_senha)
        coluna_direita.addWidget(self.edit_senha)

        coluna_direita.addSpacing(20)

        coluna_direita.addWidget(btn_cadastrar)

        coluna_direita.addStretch()

        # Adicionando ao layout principal
        layout_principal.addWidget(label_foto)
        layout_principal.addLayout(coluna_direita)

        self.setLayout(layout_principal)

    def cadastrar_voluntario(self):

        nome = self.edit_nome.text()
        email = self.edit_email.text()
        senha = self.edit_senha.text()

        self.tela_dados.adicionar_dados(
            nome,
            email,
            senha)

        self.tela_dados.show()

        self.edit_nome.clear()
        self.edit_email.clear()
        self.edit_senha.clear()



# Execução final
# Atualização executada

app = QApplication(argv)

janela = TelaCadastro()
janela.show()

app.exec()
