import sys
from PyQt5.QtWidgets import (
    QApplication, QDialog, QTabWidget, QWidget, QLabel, QPushButton,
    QLCDNumber, QCheckBox, QGroupBox, QScrollBar, QTimeEdit,
    QRadioButton, QTextBrowser, QComboBox, QLineEdit, QFrame, QMessageBox, QVBoxLayout
)
from PyQt5.QtCore import QRect, Qt, QTimer, QTime
from PyQt5.QtGui import QIcon, QFont

class Reloj(QDialog):
    def __init__(self):
        super().__init__()

        self.setGeometry(0, 0, 693, 459)
        self.setFont(QFont("Palatino Linotype"))
        self.setWindowTitle("Reloj")
        self.setWindowIcon(QIcon("2784399"))

        self.pantalla = QTabWidget(self)
        self.pantalla.setGeometry(-10, 0, 701, 461)
        self.pantalla.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.pantalla.setCurrentIndex(0)

        self.initUI()

    def initUI(self):
        self.initPomodoroTab()
        self.initConfigTab()
        self.initTaskTab()
        self.initAlarmTab()
        self.initTimerTab()
        self.initSoundTab()

    def initPomodoroTab(self):
        self.tempom = QWidget()
        self.tempom.setFocusPolicy(Qt.ClickFocus)
        self.tempom.setContextMenuPolicy(Qt.NoContextMenu)
        self.tempom.setToolTipDuration(-1)
        self.pantalla.addTab(self.tempom, "Pomodoro")

        label = QLabel(self.tempom)
        label.setGeometry(QRect(230, 20, 211, 31))
        label.setFont(QFont("Rage Italic", 20))
        label.setText("Tiempo de estudio")

        self.lcdNumber = QLCDNumber(self.tempom)
        self.lcdNumber.setGeometry(QRect(230, 60, 151, 131))
        self.lcdNumber.setLineWidth(1)
        self.lcdNumber.setDigitCount(5)
        self.lcdNumber.display("25:00")  # 25 minutes

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateLCD)

        self.pushButton = QPushButton(self.tempom)
        self.pushButton.setGeometry(QRect(480, 290, 131, 31))
        self.pushButton.setText("Descanzo")
        self.pushButton.clicked.connect(self.startBreak)

        self.pushButton_2 = QPushButton(self.tempom)
        self.pushButton_2.setGeometry(QRect(290, 290, 93, 28))
        self.pushButton_2.setText("Inicio")
        self.pushButton_2.clicked.connect(self.startPomodoro)

        self.pushButton_3 = QPushButton(self.tempom)
        self.pushButton_3.setGeometry(QRect(60, 290, 93, 28))
        self.pushButton_3.setText("Cancelar")
        self.pushButton_3.clicked.connect(self.cancelPomodoro)

        line = QFrame(self.tempom)
        line.setGeometry(QRect(210, 190, 231, 20))
        line.setFrameShape(QFrame.HLine)

        label_2 = QLabel(self.tempom)
        label_2.setGeometry(QRect(250, 230, 55, 16))
        label_2.setText("TONO")

        self.checkBox = QCheckBox(self.tempom)
        self.checkBox.setGeometry(QRect(360, 230, 81, 20))
        self.checkBox.setText("Music1")

    def startPomodoro(self):
        self.timer.start(1000)  # Update every second
        self.remaining_time = self.pomodoro_duration

    def startBreak(self):
        self.timer.start(1000)  # Update every second
        self.remaining_time = 5 * 60  # 5 minutes in seconds

    def cancelPomodoro(self):
        self.timer.stop()
        self.lcdNumber.display(f"{self.pomodoro_duration // 60:02}:{self.pomodoro_duration % 60:02}")

    def updateLCD(self):
        self.remaining_time -= 1
        if self.remaining_time < 0:
            self.timer.stop()
            QMessageBox.information(self, "Pomodoro", "Time's up!")
        else:
            minutes = self.remaining_time // 60
            seconds = self.remaining_time % 60
            self.lcdNumber.display(f"{minutes:02}:{seconds:02}")

    def initConfigTab(self):
        self.tab_2 = QWidget()
        self.pantalla.addTab(self.tab_2, "Configuracion pomodoro")

        groupBox = QGroupBox(self.tab_2)
        groupBox.setGeometry(QRect(90, 60, 511, 111))
        groupBox.setTitle("Pomodoro")

        self.timeEdit_pomodoro = QTimeEdit(groupBox)
        self.timeEdit_pomodoro.setGeometry(QRect(40, 40, 118, 22))
        self.timeEdit_pomodoro.setDisplayFormat("hh:mm")

        self.timeEdit_break = QTimeEdit(groupBox)
        self.timeEdit_break.setGeometry(QRect(190, 40, 118, 22))
        self.timeEdit_break.setDisplayFormat("mm:ss")

        label_4 = QLabel(groupBox)
        label_4.setGeometry(QRect(60, 90, 55, 16))
        label_4.setText("Pomodoro")

        label_5 = QLabel(groupBox)
        label_5.setGeometry(QRect(220, 90, 55, 16))
        label_5.setText("Descanso")

        label_3 = QLabel(self.tab_2)
        label_3.setGeometry(QRect(250, 10, 181, 16))
        label_3.setText("Configuracion Personalizada")

        self.pushButton_4 = QPushButton(self.tab_2)
        self.pushButton_4.setGeometry(QRect(50, 210, 111, 31))
        self.pushButton_4.setText("Guardar cambios")
        self.pushButton_4.clicked.connect(self.saveConfigChanges)

        self.pushButton_5 = QPushButton(self.tab_2)
        self.pushButton_5.setGeometry(QRect(520, 210, 93, 28))
        self.pushButton_5.setText("Cancelar")
        self.pushButton_5.clicked.connect(self.cancelConfigChanges)

        self.checkBox_2 = QCheckBox(self.tab_2)
        self.checkBox_2.setGeometry(QRect(60, 270, 171, 20))
        self.checkBox_2.setText("Pomodoro predifinido")

        self.pomodoro_duration = 25 * 60  # 25 minutes in seconds by default

    def saveConfigChanges(self):
        pomodoro_time = self.timeEdit_pomodoro.time()
        break_time = self.timeEdit_break.time()

        self.pomodoro_duration = pomodoro_time.hour() * 3600 + pomodoro_time.minute() * 60 + pomodoro_time.second()
        self.break_duration = break_time.minute() * 60 + break_time.second()

        QMessageBox.information(self, "Configuracion", "Cambios guardados")

    def cancelConfigChanges(self):
        QMessageBox.information(self, "Configuracion", "Cambios cancelados")

    def initTaskTab(self):
        self.tab_4 = QWidget()
        self.pantalla.addTab(self.tab_4, "Tabla de tareas")

        groupBox_2 = QGroupBox(self.tab_4)
        groupBox_2.setGeometry(QRect(79, 60, 131, 261))
        groupBox_2.setTitle("Inicio")

        groupBox_3 = QGroupBox(self.tab_4)
        groupBox_3.setGeometry(QRect(270, 60, 141, 261))
        groupBox_3.setTitle("Progreso")

        groupBox_4 = QGroupBox(self.tab_4)
        groupBox_4.setGeometry(QRect(470, 60, 131, 261))
        groupBox_4.setTitle("Finalizado")

        label_11 = QLabel(self.tab_4)
        label_11.setGeometry(QRect(280, 10, 55, 16))
        label_11.setText("TAREAS")

        self.pushButton_8 = QPushButton(self.tab_4)
        self.pushButton_8.setGeometry(QRect(90, 350, 93, 28))
        self.pushButton_8.setText("Editar")
        self.pushButton_8.clicked.connect(self.editTask)

        self.pushButton_9 = QPushButton(self.tab_4)
        self.pushButton_9.setGeometry(QRect(500, 350, 93, 28))
        self.pushButton_9.setText("Guardar")
        self.pushButton_9.clicked.connect(self.saveTask)

        self.pushButton_10 = QPushButton(self.tab_4)
        self.pushButton_10.setGeometry(QRect(300, 350, 93, 28))
        self.pushButton_10.setText("Agregar")
        self.pushButton_10.clicked.connect(self.addTask)

    def editTask(self):
        QMessageBox.information(self, "Tareas", "Editar tareas")

    def saveTask(self):
        QMessageBox.information(self, "Tareas", "Tareas guardadas")

    def addTask(self):
        QMessageBox.information(self, "Tareas", "Tarea agregada")

    def initAlarmTab(self):
        self.tab_3 = QWidget()
        self.pantalla.addTab(self.tab_3, "Alarma")

        label_7 = QLabel(self.tab_3)
        label_7.setGeometry(QRect(240, 10, 181, 41))
        label_7.setFont(QFont("MS Serif", 20))
        label_7.setText("Configuracion alarma")

        label_8 = QLabel(self.tab_3)
        label_8.setGeometry(QRect(40, 130, 201, 41))
        label_8.setFont(QFont("MS Serif", 12))
        label_8.setText("Alarma")

        label_9 = QLabel(self.tab_3)
        label_9.setGeometry(QRect(40, 270, 201, 41))
        label_9.setFont(QFont("MS Serif", 12))
        label_9.setText("Horario")

        self.pushButton_6 = QPushButton(self.tab_3)
        self.pushButton_6.setGeometry(QRect(50, 380, 93, 28))
        self.pushButton_6.setText("Editar")
        self.pushButton_6.clicked.connect(self.editAlarm)

        self.pushButton_7 = QPushButton(self.tab_3)
        self.pushButton_7.setGeometry(QRect(440, 380, 93, 28))
        self.pushButton_7.setText("Guardar")
        self.pushButton_7.clicked.connect(self.saveAlarm)

        self.timeEdit = QTimeEdit(self.tab_3)
        self.timeEdit.setGeometry(QRect(170, 130, 118, 22))
        self.timeEdit.setDisplayFormat("hh:mm AP")

        self.radioButton_3 = QRadioButton(self.tab_3)
        self.radioButton_3.setGeometry(QRect(170, 270, 95, 20))
        self.radioButton_3.setText("Lunes")

        self.radioButton_4 = QRadioButton(self.tab_3)
        self.radioButton_4.setGeometry(QRect(270, 270, 95, 20))
        self.radioButton_4.setText("Martes")

        self.radioButton_5 = QRadioButton(self.tab_3)
        self.radioButton_5.setGeometry(QRect(370, 270, 95, 20))
        self.radioButton_5.setText("Miércoles")

        self.radioButton_6 = QRadioButton(self.tab_3)
        self.radioButton_6.setGeometry(QRect(470, 270, 95, 20))
        self.radioButton_6.setText("Jueves")

        self.radioButton_7 = QRadioButton(self.tab_3)
        self.radioButton_7.setGeometry(QRect(170, 310, 95, 20))
        self.radioButton_7.setText("Viernes")

        self.radioButton_8 = QRadioButton(self.tab_3)
        self.radioButton_8.setGeometry(QRect(270, 310, 95, 20))
        self.radioButton_8.setText("Sábado")

        self.radioButton_9 = QRadioButton(self.tab_3)
        self.radioButton_9.setGeometry(QRect(370, 310, 95, 20))
        self.radioButton_9.setText("Domingo")

    def editAlarm(self):
        QMessageBox.information(self, "Alarma", "Editar alarma")

    def saveAlarm(self):
        alarm_time = self.timeEdit.time().toString("hh:mm AP")
        days_selected = []
        if self.radioButton_3.isChecked(): days_selected.append("Lunes")
        if self.radioButton_4.isChecked(): days_selected.append("Martes")
        if self.radioButton_5.isChecked(): days_selected.append("Miércoles")
        if self.radioButton_6.isChecked(): days_selected.append("Jueves")
        if self.radioButton_7.isChecked(): days_selected.append("Viernes")
        if self.radioButton_8.isChecked(): days_selected.append("Sábado")
        if self.radioButton_9.isChecked(): days_selected.append("Domingo")

        days_selected_str = ", ".join(days_selected)
        QMessageBox.information(self, "Alarma", f"Alarma guardada a las {alarm_time} para {days_selected_str}")

    def initTimerTab(self):
        self.tab = QWidget()
        self.pantalla.addTab(self.tab, "Temporizador")

        label_10 = QLabel(self.tab)
        label_10.setGeometry(QRect(250, 10, 161, 31))
        label_10.setFont(QFont("MS Serif", 20))
        label_10.setText("Temporizador")

        groupBox_5 = QGroupBox(self.tab)
        groupBox_5.setGeometry(QRect(60, 100, 561, 101))
        groupBox_5.setTitle("TIMER")

        label_12 = QLabel(groupBox_5)
        label_12.setGeometry(QRect(130, 30, 91, 31))
        label_12.setFont(QFont("MS Serif", 12))
        label_12.setText("HORAS")

        label_13 = QLabel(groupBox_5)
        label_13.setGeometry(QRect(320, 30, 91, 31))
        label_13.setFont(QFont("MS Serif", 12))
        label_13.setText("MINUTOS")

        self.scrollBar = QScrollBar(groupBox_5)
        self.scrollBar.setGeometry(QRect(50, 30, 16, 31))
        self.scrollBar.setOrientation(Qt.Vertical)

        self.scrollBar_2 = QScrollBar(groupBox_5)
        self.scrollBar_2.setGeometry(QRect(420, 30, 16, 31))
        self.scrollBar_2.setOrientation(Qt.Vertical)

        label_14 = QLabel(groupBox_5)
        label_14.setGeometry(QRect(80, 70, 91, 31))
        label_14.setFont(QFont("MS Serif", 12))
        label_14.setText("Segundos")

        self.scrollBar_3 = QScrollBar(groupBox_5)
        self.scrollBar_3.setGeometry(QRect(320, 70, 16, 31))
        self.scrollBar_3.setOrientation(Qt.Vertical)

        self.pushButton_11 = QPushButton(self.tab)
        self.pushButton_11.setGeometry(QRect(70, 230, 93, 28))
        self.pushButton_11.setText("Inicio")
        self.pushButton_11.clicked.connect(self.startTimer)

        self.pushButton_12 = QPushButton(self.tab)
        self.pushButton_12.setGeometry(QRect(300, 230, 93, 28))
        self.pushButton_12.setText("Pausa")
        self.pushButton_12.clicked.connect(self.pauseTimer)

        self.pushButton_13 = QPushButton(self.tab)
        self.pushButton_13.setGeometry(QRect(520, 230, 93, 28))
        self.pushButton_13.setText("Finalizar")
        self.pushButton_13.clicked.connect(self.stopTimer)

    def startTimer(self):
        self.timer.start(1000)
        self.remaining_time = self.scrollBar.value() * 3600 + self.scrollBar_2.value() * 60 + self.scrollBar_3.value()

    def pauseTimer(self):
        self.timer.stop()

    def stopTimer(self):
        self.timer.stop()
        QMessageBox.information(self, "Temporizador", "Temporizador finalizado")

    def initSoundTab(self):
        self.tab_5 = QWidget()
        self.pantalla.addTab(self.tab_5, "Personalizacion de sonido")

        self.comboBox = QComboBox(self.tab_5)
        self.comboBox.setGeometry(QRect(180, 50, 301, 31))
        self.comboBox.addItem("Tono 1")
        self.comboBox.addItem("Tono 2")

        self.lineEdit = QLineEdit(self.tab_5)
        self.lineEdit.setGeometry(QRect(50, 130, 151, 41))

        label_15 = QLabel(self.tab_5)
        label_15.setGeometry(QRect(60, 100, 101, 16))
        label_15.setText("Personalizar tono")

        self.pushButton_14 = QPushButton(self.tab_5)
        self.pushButton_14.setGeometry(QRect(250, 140, 93, 28))
        self.pushButton_14.setText("Guardar")
        self.pushButton_14.clicked.connect(self.saveSoundConfig)

        self.pushButton_15 = QPushButton(self.tab_5)
        self.pushButton_15.setGeometry(QRect(450, 140, 93, 28))
        self.pushButton_15.setText("Cancelar")
        self.pushButton_15.clicked.connect(self.cancelSoundConfig)

    def saveSoundConfig(self):
        selected_tone = self.comboBox.currentText()
        custom_tone = self.lineEdit.text()
        QMessageBox.information(self, "Sonido", f"Configuración guardada: {selected_tone}, {custom_tone}")

    def cancelSoundConfig(self):
        QMessageBox.information(self, "Sonido", "Configuración cancelada")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Reloj()
    window.show()
    sys.exit(app.exec_())
