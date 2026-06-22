from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
import sys

class Janela2(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Minha Janela")
        # Largura, altura e posição da janela
        self.setGeometry(10,30,800,400)
        self.texto = QLabel("Clique no botão abaixo")
        self.botao = QPushButton("Clique aqui")
        # para organizar os controles(label, pushbutton) usaremos o comando 
        # QVBoxLayout, para distribuir os controles de forma vertical na tela 
        layout_vertical = QVBoxLayout()
        layout_vertical.addWidget(self.texto)
        layout_vertical.addWidget(self.botao)
        # Adicionar o layout vertical na tela 
        self.setLayout(layout_vertical)

app = QApplication(sys.argv)
tela = Janela2()
tela.show()
app.exec()
