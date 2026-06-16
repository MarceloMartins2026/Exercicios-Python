from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit
import sys

class CadastroProduto(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Minha Janela")
        #Largura, altura e posição da janela
        self.setGeometry(750,250,300,450)

        self.setStyleSheet("background-color:#b2ebf2")

        self.nome_label = QLabel("Nome do Produto") 
        # Vamos aplicar uma formatação na label usando comandos de CSS(Cascade Style Sheet - Folha de Estilo em Cascata)
        self.nome_label.setStyleSheet("QLabel{font-size:15pt;color:#4db6ac;font-weight:bold}")
        self.nome_edit = QLineEdit()
        self.nome_edit.setStyleSheet("QLineEdit{border: 2px solid #4db6ac;border-radius:15px;background-color:#b2dfdb;font-size:20pt;color:#000000}")

        self.tipo_label = QLabel("Tipo")
        self.tipo_edit = QLineEdit()
        self.tipo_edit.setStyleSheet("QLineEdit{border: 2px solid #4db6ac;border-radius:15px;background-color:#b2dfdb;font-size:20pt;color:#000000}")
        self.tipo_label.setStyleSheet("QLabel{font-size:15pt;color:#4db6ac;font-weight:bold}")

        self.preco_label = QLabel("Preço")
        self.preco_edit = QLineEdit()
        self.preco_edit.setStyleSheet ("QLineEdit{border: 2px solid #4db6ac;border-radius:15px;background-color:#b2dfdb;font-size:20pt;color:#000000}")
        self.preco_label.setStyleSheet("QLabel{font-size:15pt;color:#4db6ac;font-weight:bold}")

        self.cadastrar_button = QPushButton("Cadastrar")
        self.cadastrar_button.setStyleSheet ("QPushButton {border: 2px solid #80cbc4;border-radius:15px;background-color:#80cbc4;font-size:15pt;color:#000000}")

        self.layout_vartical = QVBoxLayout()
        # adicionar os controles no layout
        self.layout_vartical.addWidget(self.nome_label)
        self.layout_vartical.addWidget(self.nome_edit)

        self.layout_vartical.addWidget(self.tipo_label)
        self.layout_vartical.addWidget(self.tipo_edit)

        self.layout_vartical.addWidget(self.preco_label)
        self.layout_vartical.addWidget(self.preco_edit)

        self.layout_vartical.addWidget(self.cadastrar_button)

        # Adicionar o layout vertical com todos os controles da nossa janela
        self.setLayout(self.layout_vartical)



# Apresentar a janela
app = QApplication(sys.argv)
cad = CadastroProduto()
cad.show()
app.exec()

