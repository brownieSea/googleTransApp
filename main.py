import googletrans
import sys
import re
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic  # qt designer에서 만든 ui를 불러오기 위해서 사용

form_class = uic.loadUiType('ui/transUi.ui')[0]
# 디자인한 외부 ui 파일을 불러와서 form_class에 저장

class googleTrans(QMainWindow, form_class):
    def __init__(self):
        super().__init__()  # 부모클래스 생성자 호출
        self.setupUi(self)  # 불러온 ui 파일을 연결

        self.setWindowTitle("google TRANSLATOR")
        self.setWindowIcon(QIcon('img/google.png'))
        self.statusBar().showMessage('by brownieSEA')

        self.bttnTrans.clicked.connect(self.transAction)
        self.inputKor.returnPressed.connect(self.transAction)
        self.bttnIni1.clicked.connect(self.clearText1)
        self.bttnIni2.clicked.connect(self.clearText2)

    def transAction(self):  # 번역 실행 함수 -> slot 함수
        korStr = self.inputKor.text()   # 입력된 한글 텍스트 가져오기
        reg = re.compile(r'[^가-힣|0-9]+$')
        if korStr == "":
            # pass
            QMessageBox.warning(self, "입력오류", "내용을 입력해주세요")
        elif reg.search(korStr):  # 한글 판독
            QMessageBox.warning(self, "입력오류", "한글과 숫자만 입력해주세요")
        else:
            trans = googletrans.Translator()  # 구글트랜스 모듈의 객체 선언
            engStr = trans.translate(korStr, "en")
            jpnStr = trans.translate(korStr, "ja")
            chnStr = trans.translate(korStr, "zh-cn")
            # self.strEng.setText(engStr.text)
            # self.strJpn.setText(jpnStr.text)
            # self.strChn.setText(chnStr.text)
            self.strEng.append(engStr.text)
            self.strJpn.append(jpnStr.text)
            self.strChn.append(chnStr.text)

    def clearText1(self):
        self.inputKor.clear()

    def clearText2(self):
        self.inputKor.clear()
        self.strEng.clear()
        self.strJpn.clear()
        self.strChn.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)  # 모든 응용프로그램이 작동하려면 QApplication 객체 필요.
    googleWin = googleTrans()
    googleWin.show()
    sys.exit(app.exec_())  # 창을 닫아주는 명령어