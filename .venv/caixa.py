from PyQt6.QtWidgets import QApplication, QWidget,QLabel,QLineEdit,QTableWidget, QVBoxLayout,QHBoxLayout
from PyQt6.QtGui import QPixmap
from sys import argv

class Caixa(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Caixa da Padaria")
        self.setGeometry(150,50,1600,900)

        # Criar o layout horizontal
        self.layout_horizontal = QHBoxLayout()
        # Vamos criar as duas colunas: Esquerda e Direita
        self.label_col_esquerda = QLabel()
        # Alterar a cor de fundo da label esquerda
        self.label_col_esquerda.setStyleSheet("QLabel{background-color:#ffff00}")
        self.label_col_esquerda.setFixedWidth(800)

        # Criar o layout dos elementos da coluna da esquerda. Este layout é vertical
        self.layout_vert_col_esq = QVBoxLayout()

        # Vamos criar uma label para adicionar o logo da padaria
        self.label_logo = QLabel()
        # Vamos setar o Pixmap a label para carregar a imagem
        self.label_logo.setPixmap(QPixmap("logo3.png"))
        # AJustar a imagem a label
        self.label_logo.setScaledContents(True)

        # criar a label do código do produto
        self.label_nome_produto = QLabel("Nome do Produto")
        self.label_nome_produto.setStyleSheet("QLabel{font-weight:bold;font-size:15pt;color:#000000}")   
        self.edit_nome_produto = QLineEdit()
        self.edit_nome_produto.setStyleSheet("QLineEdit{font-size:15pt}")


         # criar a label e o edit do nome do produto ===============================
        self.label_cod_produto = QLabel("Código do Produto")
        self.label_cod_produto.setStyleSheet("QLabel{font-weight:bold;font-size:15pt;color:#000000}")   
        self.edit_cod_produto = QLineEdit()
        self.edit_cod_produto.setStyleSheet("QLineEdit{font-size:15pt}")


         # criar a label da descricao do produto
        self.label_descricao_produto = QLabel("Descrição do Produto")
        self.label_descricao_produto.setStyleSheet("QLabel{font-weight:bold;font-size:15pt;color:#000000}")   
        self.edit_descricao_produto = QLineEdit()
        self.edit_descricao_produto.setStyleSheet("QLineEdit{font-size:15pt}")
        self.edit_descricao_produto.setFixedHeight(120)

        
           # criar o Preço unitário do produto ====
        self.label_preco_unitario_produto = QLabel("Preco unitario do Produto")
        self.label_preco_unitario_produto.setStyleSheet("QLabel{font-weight:bold;font-size:15pt;color:#000000}")   
        self.edit_preco_unitario_produto = QLineEdit()
        self.edit_preco_unitario_produto.setStyleSheet("QLineEdit{font-size:15pt}")


        # criar a Quantidade do produto ====
        self.label_quantidade_produto = QLabel("Quantidade do Produto")
        self.label_quantidade_produto.setStyleSheet("QLabel{font-weight:bold;font-size:15pt;color:#000000}")   
        self.edit_quantidade_produto = QLineEdit()
        self.edit_quantidade_produto.setStyleSheet("QLineEdit{font-size:15pt}")


        
        # Adicionar o logo ao layout vertical
        self.layout_vert_col_esq.addWidget(self.label_logo)
        # adicionar o código do produto
        self.layout_vert_col_esq.addWidget(self.label_cod_produto)
        self.layout_vert_col_esq.addWidget(self.edit_cod_produto)


         # adicionar o nome do produto
        self.layout_vert_col_esq.addWidget(self.label_nome_produto)
        self.layout_vert_col_esq.addWidget(self.edit_nome_produto)

         # adicionar o descricao do produto
        self.layout_vert_col_esq.addWidget(self.label_descricao_produto)
        self.layout_vert_col_esq.addWidget(self.edit_descricao_produto)

         # adicionar a quantidade do produto
        self.layout_vert_col_esq.addWidget(self.label_quantidade_produto)
        self.layout_vert_col_esq.addWidget(self.edit_quantidade_produto)

         # adicionar o preço unitário do produto
        self.layout_vert_col_esq.addWidget(self.label_preco_unitario_produto)
        self.layout_vert_col_esq.addWidget(self.edit_preco_unitario_produto)


        # Setar o layout vertical a label coluna esquerda.
        self.label_col_esquerda.setLayout(self.layout_vert_col_esq)

       
        
        
        
        self.label_col_direita = QLabel()
        self.label_col_direita.setStyleSheet("QLabel{background-color:#6E7F8D}")
        



        # Adicionar as colunas esquerda e direita ao layout horizontal
        self.layout_horizontal.addWidget(self.label_col_esquerda)
        self.layout_horizontal.addWidget(self.label_col_direita)

        #  Setar o layout horizontal a nossa janela
        self.setLayout(self.layout_horizontal)
        
app = QApplication(argv)
janela = Caixa()
janela.show()
app.exec()