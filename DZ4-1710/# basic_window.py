import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QPixmap, QMovie, QFont
from PyQt6.QtCore import QSize

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 960, 660)
        self.setWindowTitle("Привет!")
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        hello_label = QLabel(self)
        hello_label.setText("Добро пожаловать в тестовое окно!")
        hello_label.move(400, 10)
        image = "images/Hello.jpg"

        try:
            with open(image):
                world_label = QLabel(self)
                pixmap = QPixmap(image)
                world_label.setPixmap(pixmap)
                world_label.move(-2, 40)
                world_label.lower()
        except FileNotFoundError as error:
            print(f"Image not found.\nError: {error}")

        gif_label = QLabel(self)
        gif_label.move(0, 570) 
        gif_path = "images/pc.gif"

        try:
            movie = QMovie(gif_path)
            if movie.isValid():
                movie.setScaledSize(QSize(100, 100))
                gif_label.setMovie(movie)
                
                gif_label.raise_()
                
                movie.start()
                
        except Exception as error:
            print(f"Ошибка загрузки GIF: {error}")

class MainWindowProfile(QWidget):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(50, 50, 250, 400)
        self.setWindowTitle("User Profile GUI")
        self.setUpMainWindow()
        self.show()

    def createImageLabels(self):
        images = ["images/Scenary.jpg","images/Cat.jpg"]
        for image in images:
            try:
                with open(image):
                    label = QLabel(self)
                    pixmap = QPixmap(image)
                    label.setPixmap(pixmap)
                if image == "images/Cat.jpg":
                    label.move(1, 30)
            except FileNotFoundError as error:
                print(f"Image not found.\nError: {error}")

    def setUpMainWindow(self):
        
        self.createImageLabels()
        
        user_label = QLabel(self)
        user_label.setText("Ковалев Егор")
        user_label.setFont(QFont("Arial", 20))
        user_label.move(35, 3)

        bio_label = QLabel(self)
        bio_label.setText("Биография")
        bio_label.setFont(QFont("Arial", 17))
        bio_label.move(15, 185)

        about_label = QLabel(self)
        about_label.setText("Я - начинающий инженер инноватик")
        about_label.setWordWrap(True)
        about_label.move(15, 210)
        about_label.resize(220, 40)

        skills_label = QLabel(self)
        skills_label.setText("Умения")
        skills_label.setFont(QFont("Arial", 17))
        skills_label.move(15, 250)

        languages_label = QLabel(self)
        languages_label.setText("Математика, музыка, искусство и, конечно, программирование")
        languages_label.move(15, 275)

        experience_label = QLabel(self)
        experience_label.setText("Опыт")
        experience_label.setFont(QFont("Arial", 17))
        experience_label.move(15, 295)

        developer_label = QLabel(self)
        developer_label.setText("Python, 11 классов образования + музыкальная школа")
        developer_label.move(15, 320)
        
        driver_dates_label = QLabel(self)
        driver_dates_label.setText("oct 25 2025 - oct 26 2025")
        driver_dates_label.setFont(QFont("Arial", 10))
        driver_dates_label.move(15, 340)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    window1 = MainWindow()
    window2 = MainWindowProfile()
    
    sys.exit(app.exec())