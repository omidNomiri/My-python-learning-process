import sys
import numpy as np
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QFileDialog
from PySide6.QtGui import QPixmap


class Image_EncryptDecryptApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image Encrypt/Decrypt")
        self.layout = QVBoxLayout()

        self.loadImageButton = QPushButton("Load Image")
        self.loadImageButton.clicked.connect(self.load_image)
        self.layout.addWidget(self.loadImageButton)

        self.encryptButton = QPushButton("Encrypt Image")
        self.encryptButton.clicked.connect(self.encryptImage)
        self.layout.addWidget(self.encryptButton)

        self.decryptButton = QPushButton("Decrypt Image")
        self.decryptButton.clicked.connect(self.decryptImage)
        self.layout.addWidget(self.decryptButton)

        self.imageLabel = QLabel()
        self.layout.addWidget(self.imageLabel)

        self.setLayout(self.layout)

    def load_image(self):
        input_path, _ = QFileDialog.getOpenFileName(
            self, "Open Image", "", "Image Files (*.png *.jpg *.bmp)")
        if input_path:
            self.imagePath = input_path
            pixmap = QPixmap(input_path)
            self.imageLabel.setPixmap(pixmap)
            self.imageLabel.adjustSize()

    def save_image(self):
        output_path, _ = QFileDialog.getSaveFileName(
            self, "Select Directory", "")

        return output_path

    def encryptImage(self):
        from decoder_encoder import encrypt_image
        output_path = self.save_image()
        encrypt_image(self.imagePath, output_path)
        self.imageLabel.setPixmap(QPixmap(output_path))
        self.imageLabel.adjustSize()

    def decryptImage(self):
        from decoder_encoder import decrypt_image
        output_path = self.save_image()
        decrypt_image(self.imagePath, output_path, "output/output_encrypted.npy")
        self.imageLabel.setPixmap(QPixmap(output_path))
        self.imageLabel.adjustSize()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Image_EncryptDecryptApp()
    window.show()

    sys.exit(app.exec())
