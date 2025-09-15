# Activar el entorno donde se encuentran las librerias en las versionesz correctas para python 3.11
# mp_env\Scripts\activate
# mp_env\Scripts\deactivate

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtCore import QTimer
from camera_module import Camera
from gesture_module import GestureDetector
from gallery_module import Gallery
from pathlib import Path

IMAGE_FOLDER = Path("D:\\Imágenes") 
IMAGE_PATHS = [str(p) for p in IMAGE_FOLDER.glob("*") if p.suffix.lower() in [".jpg", ".png", ".jpeg"]]

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Galería con Gestos")
        self.setGeometry(100, 100, 800, 600)

        self.camera = Camera()
        self.detector = GestureDetector()
        self.gallery = Gallery(IMAGE_PATHS)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.camera_label = QLabel()
        self.layout.addWidget(self.camera_label)
        self.layout.addWidget(self.gallery.label)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)

    def update_frame(self):
        frame = self.camera.get_frame()
        if frame is not None:
            gesture, frame = self.detector.detect(frame)
            if gesture == "next":
                self.gallery.next()
            elif gesture == "prev":
                self.gallery.prev()
            elif gesture == "agrandar":
                self.gallery.enlarge()
            elif gesture == "reducir":
                self.gallery.shrink()

            h, w, ch = frame.shape
            bytes_per_line = ch * w
            qt_img = QImage(frame.data, w, h, bytes_per_line, QImage.Format.Format_BGR888)
            self.camera_label.setPixmap(QPixmap.fromImage(qt_img))

    def closeEvent(self, event):
        self.camera.release()
        event.accept()

app = QApplication(sys.argv)
window = App()
window.show()
sys.exit(app.exec())
