# Gallery module, 
from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

class Gallery:
    def __init__(self, image_paths):
        self.images = [QPixmap(p) for p in image_paths]
        self.index = 0
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet("background-color: rgba(0,0,0,150); border-radius: 15px;")
        self.update()

    def next(self):
        self.index = (self.index + 1) % len(self.images)
        self.update()

    def prev(self):
        self.index = (self.index - 1) % len(self.images)
        self.update()

    def enlarge(self):
        new_width = min(int(self.label.width() * 1.2), 800)
        new_height = min(int(self.label.height() * 1.2), 600)
        self.label.resize(new_width, new_height)

    def shrink(self):
        new_width = min(int(self.label.width() * 0.8), 800)
        new_height = min(int(self.label.height() * 0.8), 600)
        self.label.resize(new_width, new_height)

    def update(self):
        self.label.setPixmap(self.images[self.index].scaled(
            400, 400, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation
        ))
