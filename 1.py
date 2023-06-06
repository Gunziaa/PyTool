import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit


class DocumentWindow(QMainWindow):
    def __init__(self, text):
        super().__init__()

        self.setWindowTitle("说明书")

        text_edit = QTextEdit()
        text_edit.setPlainText(text)
        text_edit.setReadOnly(True)

        self.setCentralWidget(text_edit)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 示例文本内容
    document_text = "6523232322222222222222222222222222222222222222222222222222222222222222222"

    # 创建跳出的文档窗口
    document_window = DocumentWindow(document_text)
    document_window.show()

    sys.exit(app.exec())
