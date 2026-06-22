from PyQt6.QtWidgets import QApplication, QWidget,QLabel,QLineEdit,QTableWidget, QVBoxLayout,QHBoxLayout
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
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


        # criar oa label e o edit do Subtotal do produto ======
        self.label_sub_total_produto = QLabel("Sub total do Produto")
        self.label_sub_total_produto.setStyleSheet("QLabel{font-weight:bold;font-size:15pt;color:#000000}")   
        self.edit_sub_total_produto = QLineEdit("Tecle F3 para calcular o subtotal")
        self.edit_sub_total_produto.setStyleSheet("QLineEdit{font-size:15pt}")
        self.edit_sub_total_produto.setEnabled(False)

          # criar o Preço unitário do produto ====
        self.label_quantidade_produto = QLabel("Quantidade Produto")
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

             # adicionar o Sub Total do produto
        self.layout_vert_col_esq.addWidget(self.label_sub_total_produto)
        self.layout_vert_col_esq.addWidget(self.edit_sub_total_produto)


        # Setar o layout vertical a label coluna esquerda.
        self.label_col_esquerda.setLayout(self.layout_vert_col_esq)

       
        #===============================Trabalhando com a coluna da direita=========================
        
        
        self.label_col_direita = QLabel()
        self.label_col_direita.setStyleSheet("QLabel{background-color:#6E7F8D}")



        # Criar o layout vertical da coluna da direita para os elementos:
        # QTableWidget, QLabel, QLineEdit
        self.layout_vert_col_dir = QVBoxLayout()

        self.tabel_produtos = QTableWidget()
        # Criar os itens do cabeçalho da tabela
        cabecalho = ["Cod.Produto", "Nome do Produto", "Quantidade", "Preço", "Sub total"]
        # Definir a quantidade de colunas da nossa tabela
        self.tabel_produtos.setColumnCount(5)
        # Adcionar o cabeçalho a tabela
        self.tabel_produtos.setHorizontalHeaderLabels(cabecalho)
        # Adicionar algumas linhas
        self.tabel_produtos.setRowCount(20)


        self.label_total_pagar =QLabel("Total a Pagar")
        self.label_total_pagar.setStyleSheet("QLabel{font-size:40pt}")
        

        self.edit_total_pagar = QLineEdit("0,00")
        self.edit_total_pagar.setStyleSheet("QLineEdit{font-size:40pt}")
        self.edit_total_pagar.setEnabled(False)

        # Adicionar os controles do layout vertical da col direita
        self.layout_vert_col_dir.addWidget(self.tabel_produtos)
        self.layout_vert_col_dir.addWidget(self.label_total_pagar)
        self.layout_vert_col_dir.addWidget(self.edit_total_pagar)

        # Setar o layout vertical da col direita na coluna da direita
        self.label_col_direita.setLayout(self.layout_vert_col_dir)



        # Adicionar as colunas esquerda e direita ao layout horizontal
        self.layout_horizontal.addWidget(self.label_col_esquerda)
        self.layout_horizontal.addWidget(self.label_col_direita)

        #  Setar o layout horizontal a nossa janela
        self.setLayout(self.layout_horizontal)

        # Vamos usar a função keyPress para fazer a janela
        # observar as teclas que estão sendo digitadas
        # e, assim, capturar a tecla especifica e executar
        # uma ação.

        self.keyPressEvent = self.keyPressEvent

    def keyPressEvent(self, e):
        if(e.key()==Qt.Key.Key_F3):
            print("Você digitou a tecla f3")

        




app = QApplication(argv)
janela = Caixa()
janela.show()
app.exec()