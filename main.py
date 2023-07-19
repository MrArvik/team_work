import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QComboBox, QPushButton, QListWidget
from PyQt5.QtGui import QFont, QColor, QPalette


# Тестова інформація про репетиторів
tutors = {
    'Мови': [
        {'ПІБ': 'Захарченко Катерина Федорівна', 'опис': '3 дипломи спеціаліста. Досвід -31 рік. Найвища категорія. Учні – багаторазові переможці конкурсів, олімпіад різних рівнів. ДПА та ЗНО на високому рівні. Підготувала сотні учнів – переможців Всеукраїнських конкурсів та олімпіад. Мобільний телефон - 0983783981'}, 
        {'ПІБ': 'Федоренко Анатолій Петрович', 'опис': 'Репетитори з англійської мови, української мови, німецької мови, китайської мови, готуємо до ЗНО, IELTS, TOEFL, займаємося в групах та індивідуально Мобільний телефон - 09049439821.'},
        {'ПІБ': 'Юрченко Вероніка Євгеніївна', 'опис': 'Репетитор з російської мови. Готую до ДПА та ЗНО. До своєї роботи ставлюся відповідально та докладаю максимум зусиль для того, щоб учні показали прогрес у навчанні Мобільний телефон - 07363939831'},
        {'ПІБ': 'Семак Ксенія Романівна', 'опис': 'Вчитель вищої категорiї. 21 рік – стаж роботи. Якісна підготовка до ЗНО, НМТ, ДПА. Входжу до складу комісії з перевірки ЗНО-робіт. Індивідуальний підхід до кожного Мобільний телефон - 09637849831.'} 
    ],
    'Математика': [
        {'ПІБ': 'Балихіна Анастасія Єгоровна', 'опис': 'Насамперед - вчу думати і мислити логічно, адже головна мета вивчення математики - це не вирішення завдань та прикладів, а набуття навички мислення! Індивідуальна програма підготовки кожного учня залежно від мети та рівня. Для уроків я використовую онлайн дошку та графічний планшет, щоб уроки були максимально ефективними та цікавими Мобільний телефон - 0683783981.'},
        {'ПІБ': 'Філатова Дарина Олександрівна', 'опис': 'Маю досвід викладання більше 15 років. Зрозумілою мовою пояснюю складні теми. Працюю на результат. Шукаю індивідуальний підхід до кожного учня. Маю позитивні відгуки від батьків та учнів Мобільний телефон - 0937433981.'},
        {'ПІБ': 'Івлев Костянтин Валерійович', 'опис': 'Захоплююсь математикою впродовж життя, напрацював власні оптимальні підходи розв`язування задач зовнішнього незалежного оцінювання Мобільний телефон - 0783743981 '},
        {'ПІБ': 'Шведов Станіслав Вадимович', 'опис': 'Не викладаю на стандартному рівні, а намагаюсь зацікавити дитину, та проявити любов та розуміння до королеви наук математики! Мобільний телефон - 0973782981'} 
    ], 
    'Фізика': [
        {'ПІБ': 'Бородько Степан Валентинович', 'опис': 'Гарантую швидке підвищення рівня знань з математики, фізики, біології. Працюю з учнями з будь-яким рівнем підготовки Мобільний телефон - 0883723981'},
        {'ПІБ': 'Степанова Таїсія Петрівна', 'опис': 'Під час вивчення фізики використовую індивідуальний підхід до учня, показую практичне застосування, використовую віртуальні лабораторії. Допомагаю учням покращити їх знання на теми Мобільний телефон - 0783789581'},
        {'ПІБ': 'Браженко Анастасія Віталіївна', 'опис': 'Допомагаю дітям полюбити та висвітлити предмет, навчаю вирішувати завдання та виконувати лабораторні роботи, використовуючи сучасні методи викладання в умовах дистанційного навчання Мобільний телефон - 0783783581'},
        {'ПІБ': 'Стименко Ніколай Михайлович', 'опис': 'ПРепетитор з математики та фізики. Кандидат фізико-математичних наук. Науковий співробітник Інституту ядерних досліджень. Вчитель математики та фізики Мобільний телефон - 0963743981'},
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
        self.search_button.setFont(QFont('Arial', 12))  # Уменьшаем размер шрифта кнопки на 2 пункта
        
        language_layout.addWidget(language_label)
        language_layout.addWidget(self.language_combo)
        language_layout.addWidget(self.search_button)
        
        self.tutor_list = QListWidget()
        self.tutor_list.setStyleSheet("QListWidget { font-size: 14px; }")  # Уменьшаем размер шрифта списка на 2 пункта
        
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
