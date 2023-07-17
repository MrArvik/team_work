import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QComboBox, QPushButton, QListWidget
from PyQt5.QtGui import QFont, QColor, QPalette


# Тестова інформація про репетиторів
tutors = {
    'Мови': [
        {'ПІБ': 'John', 'опис': 'Досвідчений викладач англійської мови'},
        {'ПІБ': 'Alice', 'опис': 'Професійний репетитор з французької мови з акцентом на розмовну практику'}
    ],
    'Математика': [
        {'ПІБ': 'Jean', 'опис': 'Викладач з досвідом роботи в університеті'},
        {'ПІБ': 'Marie', 'опис': 'Викладач з неймовірним досвідом'}
    ],
    'Фізика': [
        {'ПІБ': 'Олена', 'опис': 'Професійний репетитор для всіх рівнів'},
        {'ПІБ': 'Іван', 'опис': 'Досвідчений викладач'}
    ]
}

class TutorSearchApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Пошук репетиторів')
        self.resize(900, 600)  # Встановлюємо розмір вікна
        self.setup_ui()
        
    def setup_ui(self):
        main_layout = QVBoxLayout()
        
        # Застосовуємо стиль для темної теми
        self.setStyleSheet("""
            QWidget {
                background-color: #222222;
                color: #ffffff;
            }
            
            QLabel {
                color: #ffffff;
            }
            
            QComboBox, QListWidget {
                background-color: #333333;
                color: #ffffff;
                border: none;
                padding: 5px;
            }
            
            QPushButton {
                background-color: #555555;
                color: #ffffff;
                padding: 5px;
                border: none;
            }
            
            QScrollBar:vertical {
                background-color: #333333;
                width: 15px;
                margin: 0px;
            }
            
            QScrollBar::handle:vertical {
                background-color: #888888;
                min-height: 20px;
            }
            
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 0px;
            }
            
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                background-color: #222222;
            }
        """)
        
        title_label = QLabel('Пошук репетиторів')
        title_label.setFont(QFont('Arial', 24, QFont.Bold))
        
        language_layout = QHBoxLayout()
        language_label = QLabel('Виберіть область знань:')
        language_label.setStyleSheet("QLabel { font-weight: bold; font-size: 18px; }")
        
        self.language_combo = QComboBox()
        self.language_combo.addItems(['Мови', 'Математика', 'Фізика'])
        
        self.search_button = QPushButton('Показати репетиторів')
        self.search_button.setFont(QFont('Arial', 14))
        self.search_button.clicked.connect(self.show_tutors)
        
        language_layout.addWidget(language_label)
        language_layout.addWidget(self.language_combo)
        language_layout.addWidget(self.search_button)
        
        self.tutor_list = QListWidget()
        self.tutor_list.setStyleSheet("QListWidget { font-size: 16px; }")
        
        main_layout.addWidget(title_label)
        main_layout.addLayout(language_layout)
        main_layout.addWidget(self.tutor_list)
        
        self.setLayout(main_layout)
    
    def show_tutors(self):
        selected_language = self.language_combo.currentText()
        self.tutor_list.clear()
        
        if selected_language in tutors:
            selected_tutors = tutors[selected_language]
            for tutor in selected_tutors:
                item = f"Ім'я: {tutor['ПІБ']}\nОпис: {tutor['опис']}"
                self.tutor_list.addItem(item)
        else:
            self.tutor_list.addItem("Немає доступних репетиторів для обраної мови")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    # Встановлюємо глобальний стиль для темної теми
    dark_palette = QPalette()
    dark_palette.setColor(QPalette.Window, QColor(34, 34, 34))
    dark_palette.setColor(QPalette.WindowText, QColor(255, 255, 255))
    dark_palette.setColor(QPalette.Base, QColor(51, 51, 51))
    dark_palette.setColor(QPalette.AlternateBase, QColor(34, 34, 34))
    dark_palette.setColor(QPalette.ToolTipBase, QColor(255, 255, 255))
    dark_palette.setColor(QPalette.ToolTipText, QColor(255, 255, 255))
    dark_palette.setColor(QPalette.Text, QColor(255, 255, 255))
    dark_palette.setColor(QPalette.Button, QColor(85, 85, 85))
    dark_palette.setColor(QPalette.ButtonText, QColor(255, 255, 255))
    dark_palette.setColor(QPalette.BrightText, QColor(255, 0, 0))
    dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.HighlightedText, QColor(0, 0, 0))
    app.setPalette(dark_palette)
    
    window = TutorSearchApp()
    window.show()
    sys.exit(app.exec_())
