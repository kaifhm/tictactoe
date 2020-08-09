from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialogButtonBox
from PyQt5 import Qt
import numpy as np

# set player names

player = 'X'
player1 = ''
player2 = ''


class PlayerRegister(QMainWindow):

    def __init__(self):
        super().__init__()
        self.resize(612, 690)
        self.setWindowTitle('TicTacToe')

        font = QtGui.QFont('Helvetica')
        font.setPointSize(16)

        self.player_1_label = QtWidgets.QLabel(self)
        self.player_1_label.setText('Player 1:')
        self.player_1_label.setFont(font)
        self.player_1_label.setGeometry(60, 235, 110, 31)
        self.player_1 = QtWidgets.QLineEdit(self)
        self.player_1.setGeometry(200, 230, 300, 41)
        self.player_1.setFont(font)
        self.player_2_label = QtWidgets.QLabel(self)
        self.player_2_label.setText('Player 2:')
        self.player_2_label.setFont(font)
        self.player_2_label.setGeometry(60, 295, 110, 31)
        self.player_2 = QtWidgets.QLineEdit(self)
        self.player_2.setGeometry(200, 290, 300, 41)
        self.player_2.setFont(font)

        font.setPointSize(12)
        self.submit = QtWidgets.QPushButton('Submit', self)
        self.submit.setGeometry(261, 370, 90, 40)
        self.submit.setFont(font)
        self.submit.clicked.connect(self.setPlayerName)
        self.show()

    def keyPressEvent(self, event):
        if type(event) == QtGui.QKeyEvent:
            if event.key() == QtCore.Qt.Key_Return:
                self.setPlayerName()

    def setPlayerName(self):
        player1 = self.player_1.text()
        player2 = self.player_2.text()
        print(player1, player2)
        if player1 != '' and player2 != '':
            ui.show()
            self.close()


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(612, 690)
        self.setWindowTitle('TicTacToe')

        font = QtGui.QFont('Helvetica')
        font.setPointSize(16)

        self.p1 = QtWidgets.QLabel(self)
        self.p1.setText(f'Player 1: {player1}')
        self.p1.setGeometry(20, 30, 321, 31)
        self.p1.setFont(font)
        self.p2 = QtWidgets.QLabel(self)
        self.p2.setText(f'Player 2: {player2}')
        self.p2.setGeometry(20, 70, 321, 31)
        self.p2.setFont(font)

        font = QtGui.QFont('Helvetica')
        font.setPointSize(46)

        self.entries = []
        for j in range(280, 501, 110):
            row = []
            for i in range(150, 371, 110):
                k = NewLabel(self)
                k.setGeometry(i, j, 101, 101)
                k.setStyleSheet('background-color: #fff;')
                k.mousePressEvent = k.clicked
                k.setFont(font)
                k.setAlignment(Qt.Qt.AlignCenter)
                row.append(k)
            self.entries.append(row)

        # self.show()

    def checkWinner(self):
        matrix = np.array([[j.text() for j in i] for i in self.entries])
        ways = [matrix, matrix.transpose()]
        for k in ways:
            for i in k:
                if i[0] == i[1] == i[2] == 'O':
                    self.declareResult(f'{player1} WON!!')
                elif i[0] == i[1] == i[2] == 'X':
                    self.declareResult(f'{player2} WON!!')

        ways = [matrix.diagonal(), np.fliplr(matrix).diagonal()]
        for i in ways:
            if i[0] == i[1] == i[2] == 'O':
                self.declareResult(f'{player1} WON!!')
            elif i[0] == i[1] == i[2] == 'X':
                self.declareResult(f'{player2} WON!!')

        draw = False
        matrix = matrix.flatten()
        if '' not in matrix:
            draw = True

        if draw:
            for i in self.entries:
                for j in i:
                    j.setDisabled(True)
            self.declareResult("It's a DRAW!")

    def declareResult(self, text):
        self.msg = QtWidgets.QDialog(self)
        self.msg.setWindowTitle('Result')
        self.msg.resize(389, 209)
        self.msg.setModal(True)

        font = QtGui.QFont('Helvetica')
        font.setPointSize(12)

        label = QtWidgets.QLabel(text, self.msg)
        label.setGeometry(120, 10, 141, 91)
        label.setFont(font)

        play = QtWidgets.QLabel('Do you want to play again?', self.msg)
        play.adjustSize()
        print(dir(play))
        print(play.width())
        play.setGeometry(80, 100, 300, 35)
        play.setFont(font)
        play.setFont(font)

        yes = QtWidgets.QPushButton(self.msg)
        yes.setGeometry(300, 160, 81, 41)
        yes.setText('Yes')
        yes.clicked.connect(self.playAgain)
        no = QtWidgets.QPushButton(self.msg)
        no.setGeometry(210, 160, 81, 41)
        no.setText('No')
        no.clicked.connect(lambda: sys.exit())

        self.msg.finished.connect(lambda: sys.exit())

        self.msg.show()

    def playAgain(self):
        global player
        player = 'X'
        for i in self.entries:
            for j in i:
                j.setText('')
                j.setDisabled(False)
        self.msg.close()


class NewLabel(QtWidgets.QLabel):

    def __init__(self, parent=None):
        super().__init__(parent=parent)

    def clicked(self, event):
        global player
        self.setText(player)
        self.setDisabled(True)
        self.setStyleSheet('color: #000; background-color: #fff')
        if player == 'X':
            player = 'O'
        else:
            player = 'X'
        ui.checkWinner()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    player_reg = PlayerRegister()
    ui = Window()
    sys.exit(app.exec())
