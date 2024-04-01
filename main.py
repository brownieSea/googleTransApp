import googletrans
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType('ui/transUi.ui')[0]

class myWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("google TRANSLATOR")

        self.statusBar().showMessage('by brownieSEA')
        self.bttnTrans.clicked.connect(self.buttonTrans)
        self.inputKor.returnPressed.connect(self.buttonTrans)
        self.bttnIni.clicked.connect(self.buttonIni)

    def buttonTrans(self):
        korStr = self.inputKor.text()
        trans = googletrans.Translator()
        resultEng = trans.translate(korStr, "en")
        resultJpn = trans.translate(korStr, "ja")
        resultChn = trans.translate(korStr, "zh-cn")
        self.strEng.setText(resultEng.text)
        self.strJpn.setText(resultJpn.text)
        self.strChn.setText(resultChn.text)

    def buttonIni(self):
        self.inputKor.setText("")
        self.strEng.setText("")
        self.strJpn.setText("")
        self.strChn.setText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)  # 모든 응용프로그램이 작동하려면 QApplication 객체 필요.
    myWin = myWindow()
    myWin.show()
    sys.exit(app.exec_())  # 창을 닫아주는 명령어