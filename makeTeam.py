import random
import sys
import webbrowser
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QComboBox, QCheckBox, QSpinBox, QMessageBox
from PyQt5.QtGui import QIcon

def makeTeam(People):

    Line = ['탑', '정글', '미드', '바텀', '서폿', '상관없음']

    TopPool = []
    JunPool = []
    MidPool = []
    BotPool = []
    SupPool = []
    Pool = [TopPool, JunPool, MidPool, BotPool, SupPool]


    # 1지망 우선 배치

    for j in range(len(Line)-1):
        Position = Line[j]
        Pool1 = []

        for i in People:
            if(Position==i[1][0]):
                Pool1.append(i)

        if(len(Pool1)>=2):
            Pool1 = random.sample(Pool1,2)

        for i in Pool1:    
            People.remove(i)

        Pool[j].extend(Pool1)

        Pool1.clear()

    #2지망 배치

    for j in range(len(Line)-1):
        Position = Line[j]
        Pool2 = []

        if len(Pool[j])!=2:
            for i in People:
                if(Position==i[1][1]):
                    Pool2.append(i)
            
            if(len(Pool2)>2-len(Pool[j])):
                Pool2 = random.sample(Pool2,2-len(Pool[j]))
        
        for i in Pool2:
            People.remove(i)

        Pool[j].extend(Pool2)
        
        Pool2.clear()


    #1, 2지망에서 떨어진 나머지 인원 및 상관없음 인원 배치

    if len(People)>0:
        for j in range(len(Line)-1):
            if(len(Pool[j])<2):
                temp = random.sample(People,2-len(Pool[j]))
                for i in temp:
                    People.remove(i)
                Pool[j].extend(temp)

    Team1 = []
    Team2 = []

    #포지션 풀에서 팀으로 인원 배치
    
    for j in range(len(Line)-1):
        temp = random.choice(Pool[j])
        Pool[j].remove(temp)
        Team1.append([temp][0][0])
        Team2.append(Pool[j][0][0])

    return [Team1, Team2]

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        #타이틀
        self.setWindowTitle('롤 내전 팀 메이커')

        #창 크기 설정
        self.resize(500, 1000)

        #아이콘 설정
        self.setWindowIcon(QIcon('league-of-legends.ico'))

        self.PutName = QLabel(self)
        self.PutName.move(25,25)
        self.PutName.setText('이름')

        self.Pref1 = QLabel(self)
        self.Pref1.move(125,25)
        self.Pref1.setText('1지망 포지션')

        self.Pref2 = QLabel(self)
        self.Pref2.move(250,25)
        self.Pref2.setText('2지망 포지션')

        #1지망, 2지망 표현 위한 리스트
        Positions = ['탑', '정글', '미드', '바텀', '서폿', '상관없음']

        #플레이어0
        self.P0name = QLineEdit(self)
        self.P0name.move(25,50)
        self.P0name.setFixedWidth(75)

        self.P0Pref1 = QComboBox(self)
        self.P0Pref1.addItems(Positions)
        self.P0Pref1.setFixedWidth(110)
        self.P0Pref1.move(125,50)
        self.P0Pref1.activated[str].connect(self.P0PrefCombo)

        self.P0Pref2 = QComboBox(self)
        self.P0Pref2.setFixedWidth(110)
        self.P0Pref2.move(250,50)

        #플레이어1
        self.P1name = QLineEdit(self)
        self.P1name.move(25,100)
        self.P1name.setFixedWidth(75)

        self.P1Pref1 = QComboBox(self)
        self.P1Pref1.addItems(Positions)
        self.P1Pref1.setFixedWidth(110)
        self.P1Pref1.move(125,100)
        self.P1Pref1.activated[str].connect(self.P1PrefCombo)

        self.P1Pref2 = QComboBox(self)
        self.P1Pref2.setFixedWidth(110)
        self.P1Pref2.move(250,100)

        #플레이어2
        self.P2name = QLineEdit(self)
        self.P2name.move(25,150)
        self.P2name.setFixedWidth(75)

        self.P2Pref1 = QComboBox(self)
        self.P2Pref1.addItems(Positions)
        self.P2Pref1.setFixedWidth(110)
        self.P2Pref1.move(125,150)
        self.P2Pref1.activated[str].connect(self.P2PrefCombo)

        self.P2Pref2 = QComboBox(self)
        self.P2Pref2.setFixedWidth(110)
        self.P2Pref2.move(250,150)

        #플레이어3
        self.P3name = QLineEdit(self)
        self.P3name.move(25,200)
        self.P3name.setFixedWidth(75)

        self.P3Pref1 = QComboBox(self)
        self.P3Pref1.addItems(Positions)
        self.P3Pref1.setFixedWidth(110)
        self.P3Pref1.move(125,200)
        self.P3Pref1.activated[str].connect(self.P3PrefCombo)

        self.P3Pref2 = QComboBox(self)
        self.P3Pref2.setFixedWidth(110)
        self.P3Pref2.move(250,200)

        #플레이어4
        self.P4name = QLineEdit(self)
        self.P4name.move(25,250)
        self.P4name.setFixedWidth(75)

        self.P4Pref1 = QComboBox(self)
        self.P4Pref1.addItems(Positions)
        self.P4Pref1.setFixedWidth(110)
        self.P4Pref1.move(125,250)
        self.P4Pref1.activated[str].connect(self.P4PrefCombo)

        self.P4Pref2 = QComboBox(self)
        self.P4Pref2.setFixedWidth(110)
        self.P4Pref2.move(250,250)

        #플레이어5
        self.P5name = QLineEdit(self)
        self.P5name.move(25,300)
        self.P5name.setFixedWidth(75)

        self.P5Pref1 = QComboBox(self)
        self.P5Pref1.addItems(Positions)
        self.P5Pref1.setFixedWidth(110)
        self.P5Pref1.move(125,300)
        self.P5Pref1.activated[str].connect(self.P5PrefCombo)

        self.P5Pref2 = QComboBox(self)
        self.P5Pref2.setFixedWidth(110)
        self.P5Pref2.move(250,300)

        #플레이어6
        self.P6name = QLineEdit(self)
        self.P6name.move(25,350)
        self.P6name.setFixedWidth(75)

        self.P6Pref1 = QComboBox(self)
        self.P6Pref1.addItems(Positions)
        self.P6Pref1.setFixedWidth(110)
        self.P6Pref1.move(125,350)
        self.P6Pref1.activated[str].connect(self.P6PrefCombo)

        self.P6Pref2 = QComboBox(self)
        self.P6Pref2.setFixedWidth(110)
        self.P6Pref2.move(250,350)

        #플레이어7
        self.P7name = QLineEdit(self)
        self.P7name.move(25,400)
        self.P7name.setFixedWidth(75)

        self.P7Pref1 = QComboBox(self)
        self.P7Pref1.addItems(Positions)
        self.P7Pref1.setFixedWidth(110)
        self.P7Pref1.move(125,400)
        self.P7Pref1.activated[str].connect(self.P7PrefCombo)

        self.P7Pref2 = QComboBox(self)
        self.P7Pref2.setFixedWidth(110)
        self.P7Pref2.move(250,400)

        #플레이어8
        self.P8name = QLineEdit(self)
        self.P8name.move(25,450)
        self.P8name.setFixedWidth(75)

        self.P8Pref1 = QComboBox(self)
        self.P8Pref1.addItems(Positions)
        self.P8Pref1.setFixedWidth(110)
        self.P8Pref1.move(125,450)
        self.P8Pref1.activated[str].connect(self.P8PrefCombo)

        self.P8Pref2 = QComboBox(self)
        self.P8Pref2.setFixedWidth(110)
        self.P8Pref2.move(250,450)

        #플레이어9
        self.P9name = QLineEdit(self)
        self.P9name.move(25,500)
        self.P9name.setFixedWidth(75)

        self.P9Pref1 = QComboBox(self)
        self.P9Pref1.addItems(Positions)
        self.P9Pref1.setFixedWidth(110)
        self.P9Pref1.move(125,500)
        self.P9Pref1.activated[str].connect(self.P9PrefCombo)

        self.P9Pref2 = QComboBox(self)
        self.P9Pref2.setFixedWidth(110)
        self.P9Pref2.move(250,500)

        #1,2지망에 따라 팀 구성 버튼
        self.PrefTeam = QPushButton(self)
        self.PrefTeam.move(25, 550)
        self.PrefTeam.setText('지망에 따라 팀 만들기')
        self.PrefTeam.clicked.connect(self.PrefTeam_event)

        #포지션 튕김 확률 적용 여부 체크 박스
        self.PosTroll = QCheckBox('포지션 튕김 확률 적용(20%)',self)
        self.PosTroll.move(225,555)

        #지망 무시하고 랜덤으로 팀 구성 버튼
        self.RandTeam = QPushButton(self)
        self.RandTeam.move(25, 600)
        self.RandTeam.setText('지망 무시하고 랜덤 팀 만들기')
        self.RandTeam.clicked.connect(self.RandTeam_event)

        #팀 구성 결과
        self.Team1 = QLabel(self)
        self.Team1.move(25, 650)
        self.Team1.setText('팀1')

        self.Team1p1 = QLabel(self)
        self.Team1p1.move(25, 700)
        self.Team1p1.setText('팀1 탑')

        self.Team1p2 = QLabel(self)
        self.Team1p2.move(25, 750)
        self.Team1p2.setText('팀1 정글')

        self.Team1p3 = QLabel(self)
        self.Team1p3.move(25, 800)
        self.Team1p3.setText('팀1 미드')

        self.Team1p4 = QLabel(self)
        self.Team1p4.move(25, 850)
        self.Team1p4.setText('팀1 원딜')

        self.Team1p5 = QLabel(self)
        self.Team1p5.move(25, 900)
        self.Team1p5.setText('팀1 서폿')

        self.Team2 = QLabel(self)
        self.Team2.move(175, 650)
        self.Team2.setText('팀2')

        self.Team2p1 = QLabel(self)
        self.Team2p1.move(175, 700)
        self.Team2p1.setText('팀2 탑')

        self.Team2p2 = QLabel(self)
        self.Team2p2.move(175, 750)
        self.Team2p2.setText('팀2 정글')

        self.Team2p3 = QLabel(self)
        self.Team2p3.move(175, 800)
        self.Team2p3.setText('팀2 미드')

        self.Team2p4 = QLabel(self)
        self.Team2p4.move(175, 850)
        self.Team2p4.setText('팀2 원딜')

        self.Team2p5 = QLabel(self)
        self.Team2p5.move(175, 900)
        self.Team2p5.setText('팀2 서폿')

        #변경사항
        self.Noti = QPushButton(self)
        self.Noti.move(25,945)
        self.Noti.setText('변경사항')
        self.Noti.clicked.connect(self.NotiEvent)

        #GitHub 링크
        self.GitHub = QLabel(self)
        self.GitHub.move(175,950)
        self.GitHub.setText("<a href='https://github.com/DonkeyLion/MakeTeam'>GitHub Link</a>")
        self.GitHub.setOpenExternalLinks(True)

        self.show()

    #지망 반영 팀 구성
    def PrefTeam_event(self):
        P0 = [self.P0name.text(),[self.P0Pref1.currentText(),self.P0Pref2.currentText()]]
        P1 = [self.P1name.text(),[self.P1Pref1.currentText(),self.P1Pref2.currentText()]]
        P2 = [self.P2name.text(),[self.P2Pref1.currentText(),self.P2Pref2.currentText()]]
        P3 = [self.P3name.text(),[self.P3Pref1.currentText(),self.P3Pref2.currentText()]]
        P4 = [self.P4name.text(),[self.P4Pref1.currentText(),self.P4Pref2.currentText()]]
        P5 = [self.P5name.text(),[self.P5Pref1.currentText(),self.P5Pref2.currentText()]]
        P6 = [self.P6name.text(),[self.P6Pref1.currentText(),self.P6Pref2.currentText()]]
        P7 = [self.P7name.text(),[self.P7Pref1.currentText(),self.P7Pref2.currentText()]]
        P8 = [self.P8name.text(),[self.P8Pref1.currentText(),self.P8Pref2.currentText()]]
        P9 = [self.P9name.text(),[self.P9Pref1.currentText(),self.P9Pref2.currentText()]]

        People = [P0, P1, P2, P3, P4, P5, P6, P7, P8, P9]

        if self.PosTroll.isChecked():
            for i in range(10):
                if random.random()<0.2:
                    Positions = ['탑', '정글', '미드', '바텀', '서폿']
                    People[i][1] = random.sample(Positions,2)

        Team = makeTeam(People)

        self.Team1p1.setText(Team[0][0])
        self.Team1p2.setText(Team[0][1])
        self.Team1p3.setText(Team[0][2])
        self.Team1p4.setText(Team[0][3])
        self.Team1p5.setText(Team[0][4])

        self.Team2p1.setText(Team[1][0])
        self.Team2p2.setText(Team[1][1])
        self.Team2p3.setText(Team[1][2])
        self.Team2p4.setText(Team[1][3])
        self.Team2p5.setText(Team[1][4])

    #지망 무시하고 랜덤 팀 구성
    def RandTeam_event(self):
        P0 = [self.P0name.text()]
        P1 = [self.P1name.text()]
        P2 = [self.P2name.text()]
        P3 = [self.P3name.text()]
        P4 = [self.P4name.text()]
        P5 = [self.P5name.text()]
        P6 = [self.P6name.text()]
        P7 = [self.P7name.text()]
        P8 = [self.P8name.text()]
        P9 = [self.P9name.text()]

        People = [P0, P1, P2, P3, P4, P5, P6, P7, P8, P9]
        Team1 = random.sample(People,5)
        for i in Team1:
            People.remove(i)
        Team2 = random.sample(People,5)

        self.Team1p1.setText(Team1[0][0])
        self.Team1p2.setText(Team1[1][0])
        self.Team1p3.setText(Team1[2][0])
        self.Team1p4.setText(Team1[3][0])
        self.Team1p5.setText(Team1[4][0])

        self.Team2p1.setText(Team2[0][0])
        self.Team2p2.setText(Team2[1][0])
        self.Team2p3.setText(Team2[2][0])
        self.Team2p4.setText(Team2[3][0])
        self.Team2p5.setText(Team2[4][0])

    def P0PrefCombo(self,text):
        self.P0Pref2.clear()
        if text == '상관없음':
            self.P0Pref2.addItem('상관없음')
        else:
            Positions = ['탑', '정글', '미드', '바텀', '서폿', '상관없음']
            Positions.remove(text)
            self.P0Pref2.addItems(Positions)
    
    def P1PrefCombo(self,text):
        self.P1Pref2.clear()
        if text == '상관없음':
            self.P1Pref2.addItem('상관없음')
        else:
            Positions = ['탑', '정글', '미드', '바텀', '서폿', '상관없음']
            Positions.remove(text)
            self.P1Pref2.addItems(Positions)
    
    def P2PrefCombo(self,text):
        self.P2Pref2.clear()
        if text == '상관없음':
            self.P2Pref2.addItem('상관없음')
        else:
            Positions = ['탑', '정글', '미드', '바텀', '서폿', '상관없음']
            Positions.remove(text)
            self.P2Pref2.addItems(Positions)

    def P3PrefCombo(self,text):
        self.P3Pref2.clear()
        if text == '상관없음':
            self.P3Pref2.addItem('상관없음')
        else:
            Positions = ['탑', '정글', '미드', '바텀', '서폿', '상관없음']
            Positions.remove(text)
            self.P3Pref2.addItems(Positions)

    def P4PrefCombo(self,text):
        self.P4Pref2.clear()
        if text == '상관없음':
            self.P4Pref2.addItem('상관없음')
        else:
            Positions = ['탑', '정글', '미드', '바텀', '서폿', '상관없음']
            Positions.remove(text)
            self.P4Pref2.addItems(Positions)

    def P5PrefCombo(self,text):
        self.P5Pref2.clear()
        if text == '상관없음':
            self.P5Pref2.addItem('상관없음')
        else:
            Positions = ['탑', '정글', '미드', '바텀', '서폿', '상관없음']
            Positions.remove(text)
            self.P5Pref2.addItems(Positions)

    def P6PrefCombo(self,text):
        self.P6Pref2.clear()
        if text == '상관없음':
            self.P6Pref2.addItem('상관없음')
        else:
            Positions = ['탑', '정글', '미드', '바텀', '서폿', '상관없음']
            Positions.remove(text)
            self.P6Pref2.addItems(Positions)

    def P7PrefCombo(self,text):
        self.P7Pref2.clear()
        if text == '상관없음':
            self.P7Pref2.addItem('상관없음')
        else:
            Positions = ['탑', '정글', '미드', '바텀', '서폿', '상관없음']
            Positions.remove(text)
            self.P7Pref2.addItems(Positions)

    def P8PrefCombo(self,text):
        self.P8Pref2.clear()
        if text == '상관없음':
            self.P8Pref2.addItem('상관없음')
        else:
            Positions = ['탑', '정글', '미드', '바텀', '서폿', '상관없음']
            Positions.remove(text)
            self.P8Pref2.addItems(Positions)

    def P9PrefCombo(self,text):
        self.P9Pref2.clear()
        if text == '상관없음':
            self.P9Pref2.addItem('상관없음')
        else:
            Positions = ['탑', '정글', '미드', '바텀', '서폿', '상관없음']
            Positions.remove(text)
            self.P9Pref2.addItems(Positions)
    
    def NotiEvent(self):
        QMessageBox.information(self,'변경사항','1. 포지션 선택에 상관없음 추가(1지망 상관없음 선택 시 2지망도 상관없음으로 고정)\n\n2. 1지망 선택 시 2지망에 해당 1지망 선택지 비활성화\n\n3. 지망 반영하지 않는 랜덤 팀 배치 버튼 추가\n\n4. 20% 확률로 각 인원의 1,2 지망이 랜덤으로 변경되게 하는 체크 박스 추가\n\n5. 팀 배정 후 중복 인원이 생기던 버그 수정\n')


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())