import sys
import re
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget, QFileDialog, QLabel
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QColor, QFont


class TypeWriter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.words = []
        self.current_word = 0
        self.current_char = 0
        self.colors = {
            'keyword': QColor(70, 130, 180),  # Blue for general keywords
            'control': QColor(255, 127, 80),  # Coral for control flow keywords
            'def': QColor(221, 160, 221),     # Plum for function definitions
            'string': QColor(50, 205, 50),    # Lime Green for strings
            'comment': QColor(105, 105, 105), # Dim Grey for comments
            'import': QColor(255, 215, 0),    # Gold for import statements
            'default': QColor(255, 255, 255)  # White for default text
        }
        self.setup_window()
        self.ask_for_file()

    def setup_window(self):
        self.setWindowTitle("Dawillygene Code")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: #1e1e1e; color: white;")

        layout = QVBoxLayout()

        self.header = QLabel("DAWILLYGENE CODE")
        self.header.setStyleSheet("color: #00ff00; font-size: 36px; font-weight: bold;")
        layout.addWidget(self.header)

        self.text_display = QTextEdit(self)
        self.text_display.setStyleSheet("background-color: #1e1e1e; color: white;")
        self.text_display.setFont(QFont("Georgia", 14))
        self.text_display.setReadOnly(True)
        layout.addWidget(self.text_display)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def ask_for_file(self):
        options = QFileDialog.Options()
        file, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;Python Files (*.py)", options=options)
        if file:
            self.load_file(file)
            self.start_typing()

    def load_file(self, filename):
        try:
            with open(filename, 'r') as f:
                lines = f.readlines()
                self.words = []
                for line in lines:
                    tokens = re.findall(r'\s+|\S+', line)
                    self.words.extend(tokens)
        except Exception as e:
            print(f"Error loading file: {str(e)}")

    def get_color_tag(self, word):
        python_keywords = {
            'def', 'class', 'return', 'if', 'else', 'elif', 'for', 'while',
            'import', 'from', 'as', 'try', 'except', 'finally', 'raise',
            'with', 'lambda', 'pass', 'break', 'continue', 'yield'
        }
        control_keywords = {'if', 'else', 'elif', 'for', 'while', 'try', 'except', 'finally'}
        
        if word in python_keywords:
            if word in control_keywords:
                return 'control'
            elif word == 'def':
                return 'def'
            elif word in {'import', 'from', 'as'}:
                return 'import'
            else:
                return 'keyword'
        elif word.startswith(('"', "'")) or word.endswith(('"', "'")):
            return 'string'
        elif word.startswith('#'):
            return 'comment'
        return 'default'

    def start_typing(self):
        if self.current_word < len(self.words):
            self.type_next_character()

    def type_next_character(self):
        if self.current_word >= len(self.words):
            return

        word = self.words[self.current_word]
        
        if self.current_char < len(word):
            char = word[self.current_char]
            color_tag = self.get_color_tag(word)
            
            cursor_pos = self.text_display.textCursor()
            cursor_pos.movePosition(cursor_pos.EndOfBlock, cursor_pos.KeepAnchor)

            if color_tag:
                color = self.colors.get(color_tag, self.colors['default'])
                self.text_display.setTextColor(color)
            else:
                self.text_display.setTextColor(self.colors['default'])
            
            self.text_display.insertPlainText(char)
            self.current_char += 1
            QTimer.singleShot(90, self.type_next_character)  # Delay typing
        else:
            self.handle_word_end()

    def handle_word_end(self):
        self.current_word += 1
        self.current_char = 0
        self.start_typing()


def main():
    app = QApplication(sys.argv)
    window = TypeWriter()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
