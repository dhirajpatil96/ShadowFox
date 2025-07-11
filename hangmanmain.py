
import sys
import random
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt
from ui_hangman import Ui_MainWindow

class HangmanCanvas(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.incorrect_guesses = 0

    def set_incorrect_guesses(self, count):
        self.incorrect_guesses = count
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        pen = QPen(Qt.black, 3)
        painter.setPen(pen)
        painter.drawLine(20, 230, 180, 230)
        painter.drawLine(50, 230, 50, 20)
        painter.drawLine(50, 20, 130, 20)
        painter.drawLine(130, 20, 130, 40)
        errors = self.incorrect_guesses
        if errors >= 1:
            painter.drawEllipse(110, 40, 40, 40)
        if errors >= 2:
            painter.drawLine(130, 80, 130, 140)
        if errors >= 3:
            painter.drawLine(130, 100, 100, 120)
        if errors >= 4:
            painter.drawLine(130, 100, 160, 120)
        if errors >= 5:
            painter.drawLine(130, 140, 110, 180)
        if errors >= 6:
            painter.drawLine(130, 140, 150, 180)

class HangmanWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.canvas = HangmanCanvas(self)
        self.ui.verticalLayout.replaceWidget(self.ui.canvasWidget, self.canvas)
        self.ui.canvasWidget.deleteLater()
        self.words = ["python", "hangman", "developer", "interface", "programming"]
        self.ui.btnSubmit.clicked.connect(self.submit_guess)
        self.ui.btnPlayAgain.clicked.connect(self.new_game)
        self.new_game()

    def new_game(self):
        self.word = random.choice(self.words)
        self.guessed_letters = []
        self.incorrect_guesses = []
        self.ui.btnPlayAgain.setEnabled(False)
        self.ui.btnSubmit.setEnabled(True)
        self.ui.lineEditGuess.setEnabled(True)
        self.ui.lineEditGuess.clear()
        self.update_display()

    def update_display(self):
        display = " ".join([ch if ch in self.guessed_letters else "_" for ch in self.word])
        self.ui.labelWord.setText(display)
        self.ui.labelInfo.setText(
            f"Incorrect: {' '.join(self.incorrect_guesses)} | Attempts Left: {6 - len(self.incorrect_guesses)}"
        )
        self.canvas.set_incorrect_guesses(len(self.incorrect_guesses))

    def submit_guess(self):
        guess = self.ui.lineEditGuess.text().lower()
        self.ui.lineEditGuess.clear()
        if not guess.isalpha() or len(guess) != 1:
            self.ui.labelInfo.setText("Enter a single alphabet letter.")
            return
        if guess in self.guessed_letters or guess in self.incorrect_guesses:
            self.ui.labelInfo.setText(f"You already guessed '{guess}'.")
            return
        if guess in self.word:
            self.guessed_letters.append(guess)
        else:
            self.incorrect_guesses.append(guess)
        self.update_display()
        if all(ch in self.guessed_letters for ch in self.word):
            self.ui.labelInfo.setText(f"🎉 You won! Word was '{self.word}'")
            self.end_game()
        elif len(self.incorrect_guesses) >= 6:
            self.ui.labelWord.setText(self.word)
            self.ui.labelInfo.setText(f"💀 Game over! Word was '{self.word}'")
            self.end_game()

    def end_game(self):
        self.ui.btnSubmit.setEnabled(False)
        self.ui.lineEditGuess.setEnabled(False)
        self.ui.btnPlayAgain.setEnabled(True)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = HangmanWindow()
    window.show()
    sys.exit(app.exec_())
