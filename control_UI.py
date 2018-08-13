from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QSlider, QPushButton, QLineEdit, QGridLayout
from PyQt5.QtCore import Qt
import sys
import serial

#The following line is for serial over GPIO
port = 'COM3'
ard = serial.Serial(port,9600,timeout=5)

class Slider_Control(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 500, 320)

        ELBOW_label = QLabel('Elbow')
        SHOULDER_label = QLabel('Shoulder')
        WRISTx_label = QLabel('Wrist-x')
        WRISTy_label = QLabel('Wrist-y')
        WRISTz_label = QLabel('Wrist-z')
        BASE_label = QLabel('Base')
        CRAW_label = QLabel('Craw')

        #define a slider that can control the elbow
        self.ELBOW_slider = QSlider(Qt.Horizontal, self)
        self.ELBOW_slider.setFocusPolicy(Qt.NoFocus)
        self.ELBOW_slider.setMinimum(0)
        self.ELBOW_slider.setMaximum(140)
        self.ELBOW_slider.setValue(90)
        self.ELBOW_slider.valueChanged.connect(self.ELBOW_show)
        self.ELBOW_slider.sliderReleased.connect(self.ELBOW_changed)
        # define a slider that can control the shoulder
        self.SHOULDER_slider = QSlider(Qt.Horizontal, self)
        self.SHOULDER_slider.setFocusPolicy(Qt.NoFocus)
        self.SHOULDER_slider.setMinimum(0)
        self.SHOULDER_slider.setMaximum(165)
        self.SHOULDER_slider.setValue(20)
        self.SHOULDER_slider.valueChanged.connect(self.SHOULDER_show)
        self.SHOULDER_slider.sliderReleased.connect(self.SHOULDER_changed)
        # define a slider that can control the wrist-x
        self.WRISTx_slider = QSlider(Qt.Horizontal, self)
        self.WRISTx_slider.setFocusPolicy(Qt.NoFocus)
        self.WRISTx_slider.setMinimum(0)
        self.WRISTx_slider.setMaximum(180)
        self.WRISTx_slider.setValue(87)
        self.WRISTx_slider.valueChanged.connect(self.WRISTx_show)
        self.WRISTx_slider.sliderReleased.connect(self.WRISTx_changed)
        # define a slider that can control the wrist-y
        self.WRISTy_slider = QSlider(Qt.Horizontal, self)
        self.WRISTy_slider.setFocusPolicy(Qt.NoFocus)
        self.WRISTy_slider.setMinimum(0)
        self.WRISTy_slider.setMaximum(90)
        self.WRISTy_slider.setValue(70)
        self.WRISTy_slider.valueChanged.connect(self.WRISTy_show)
        self.WRISTy_slider.sliderReleased.connect(self.WRISTy_changed)
        # define a slider that can control the wrist-z
        self.WRISTz_slider = QSlider(Qt.Horizontal, self)
        self.WRISTz_slider.setFocusPolicy(Qt.NoFocus)
        self.WRISTz_slider.setMinimum(0)
        self.WRISTz_slider.setMaximum(180)
        self.WRISTz_slider.setValue(50)
        self.WRISTz_slider.valueChanged.connect(self.WRISTz_show)
        self.WRISTz_slider.sliderReleased.connect(self.WRISTz_changed)
        # define a slider that can control the base
        self.BASE_slider = QSlider(Qt.Horizontal, self)
        self.BASE_slider.setFocusPolicy(Qt.NoFocus)
        self.BASE_slider.setMinimum(0)
        self.BASE_slider.setMaximum(180)
        self.BASE_slider.setValue(96)
        self.BASE_slider.valueChanged.connect(self.BASE_show)
        self.BASE_slider.sliderReleased.connect(self.BASE_changed)
        # define a slider that can control the craw
        self.CRAW_slider = QSlider(Qt.Horizontal, self)
        self.CRAW_slider.setFocusPolicy(Qt.NoFocus)
        self.CRAW_slider.setMinimum(0)
        self.CRAW_slider.setMaximum(58)
        self.CRAW_slider.setValue(30)
        self.CRAW_slider.valueChanged.connect(self.CRAW_show)
        self.CRAW_slider.sliderReleased.connect(self.CRAW_changed)

        self.ELBOW_num = QLabel(str(self.ELBOW_slider.value()))
        self.SHOULDER_num = QLabel(str(self.SHOULDER_slider.value()))
        self.WRISTx_num = QLabel(str(self.WRISTx_slider.value()))
        self.WRISTy_num = QLabel(str(self.WRISTy_slider.value()))
        self.WRISTz_num = QLabel(str(self.WRISTz_slider.value()))
        self.BASE_num = QLabel(str(self.BASE_slider.value()))
        self.CRAW_num = QLabel(str(self.CRAW_slider.value()))

        layout = QGridLayout()
        layout.addWidget(ELBOW_label, 1, 0)
        layout.addWidget(SHOULDER_label, 2, 0)
        layout.addWidget(WRISTx_label, 3, 0)
        layout.addWidget(WRISTy_label, 4, 0)
        layout.addWidget(WRISTz_label, 5, 0)
        layout.addWidget(BASE_label, 6, 0)
        layout.addWidget(CRAW_label, 7, 0)
        layout.addWidget(self.ELBOW_slider, 1, 1)
        layout.addWidget(self.SHOULDER_slider, 2, 1)
        layout.addWidget(self.WRISTx_slider, 3, 1)
        layout.addWidget(self.WRISTy_slider, 4, 1)
        layout.addWidget(self.WRISTz_slider, 5, 1)
        layout.addWidget(self.BASE_slider, 6, 1)
        layout.addWidget(self.CRAW_slider, 7, 1)
        layout.addWidget(self.ELBOW_num, 1, 2)
        layout.addWidget(self.SHOULDER_num, 2, 2)
        layout.addWidget(self.WRISTx_num, 3, 2)
        layout.addWidget(self.WRISTy_num, 4, 2)
        layout.addWidget(self.WRISTz_num, 5, 2)
        layout.addWidget(self.BASE_num, 6, 2)
        layout.addWidget(self.CRAW_num, 7, 2)

        self.setLayout(layout)
        self.setWindowTitle('Robotic Control')
        self.show()

    def ELBOW_show(self):
        self.ELBOW_num.setText(str(self.ELBOW_slider.value()))
    def ELBOW_changed(self):
        info = str(1) + ',' + str(self.ELBOW_slider.value())
        #print(self.ELBOW_slider.value())
        ard.write(str.encode(info))

    def SHOULDER_show(self):
        self.SHOULDER_num.setText(str(self.SHOULDER_slider.value()))
    def SHOULDER_changed(self):
        info = str(2) + ',' + str(self.SHOULDER_slider.value())
        #print(self.SHOULDER_slider.value())
        ard.write(str.encode(info))

    def WRISTx_show(self):
        self.WRISTx_num.setText(str(self.WRISTx_slider.value()))
    def WRISTx_changed(self):
        info = str(3) + ',' + str(self.WRISTx_slider.value())
        #print(self.WRISTx_slider.value())
        ard.write(str.encode(info))

    def WRISTy_show(self):
        self.WRISTy_num.setText(str(self.WRISTy_slider.value()))
    def WRISTy_changed(self):
        info = str(4) + ',' + str(self.WRISTy_slider.value())
        #print(self.WRISTy_slider.value())
        ard.write(str.encode(info))

    def WRISTz_show(self):
        self.WRISTz_num.setText(str(self.WRISTz_slider.value()))
    def WRISTz_changed(self):
        info = str(5) + ',' + str(self.WRISTz_slider.value())
        #print(self.WRISTz_slider.value())
        ard.write(str.encode(info))

    def BASE_show(self):
        self.BASE_num.setText(str(self.BASE_slider.value()))
    def BASE_changed(self):
        info = str(6) + ',' + str(self.BASE_slider.value())
        #print(self.BASE_slider.value())
        ard.write(str.encode(info))

    def CRAW_show(self):
        self.CRAW_num.setText(str(self.CRAW_slider.value()))
    def CRAW_changed(self):
        info = str(7) + ',' + str(self.CRAW_slider.value())
        #print(self.CRAW_slider.value())
        ard.write(str.encode(info))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Slider_Control()
    sys.exit(app.exec_())