# Form implementation generated from reading ui file 'guiPrincipal.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets

#########################################
from PyQt6.QtWidgets import QMainWindow

#########################################
class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(862, 779)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 861, 721))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tabWidget.setFont(font)
        self.tabWidget.setIconSize(QtCore.QSize(30, 30))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_op = QtWidgets.QLabel(self.tab)
        self.label_op.setGeometry(QtCore.QRect(490, 70, 361, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_op.setFont(font)
        self.label_op.setObjectName("label_op")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(140, 70, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.line_4 = QtWidgets.QFrame(self.tab)
        self.line_4.setGeometry(QtCore.QRect(20, 450, 811, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_6 = QtWidgets.QFrame(self.tab)
        self.line_6.setGeometry(QtCore.QRect(380, 20, 20, 351))
        self.line_6.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_6.setObjectName("line_6")
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(70, 150, 261, 131))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.bBuck = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bBuck.setFont(font)
        self.bBuck.setCheckable(True)
        self.bBuck.setAutoExclusive(False)
        self.bBuck.setAutoDefault(False)
        self.bBuck.setFlat(False)
        self.bBuck.setObjectName("bBuck")
        self.gridLayout.addWidget(self.bBuck, 0, 0, 1, 1)
        self.bFlyback = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bFlyback.setFont(font)
        self.bFlyback.setCheckable(True)
        self.bFlyback.setAutoExclusive(False)
        self.bFlyback.setAutoDefault(False)
        self.bFlyback.setFlat(False)
        self.bFlyback.setObjectName("bFlyback")
        self.gridLayout.addWidget(self.bFlyback, 0, 1, 1, 1)
        self.bBoost = QtWidgets.QPushButton(self.layoutWidget)
        self.bBoost.setSizeIncrement(QtCore.QSize(0, 2))
        self.bBoost.setBaseSize(QtCore.QSize(0, 5))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bBoost.setFont(font)
        self.bBoost.setCheckable(True)
        self.bBoost.setAutoExclusive(False)
        self.bBoost.setAutoDefault(False)
        self.bBoost.setFlat(False)
        self.bBoost.setObjectName("bBoost")
        self.gridLayout.addWidget(self.bBoost, 1, 0, 1, 1)
        self.bSepic = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bSepic.setFont(font)
        self.bSepic.setCheckable(True)
        self.bSepic.setAutoExclusive(False)
        self.bSepic.setAutoDefault(False)
        self.bSepic.setFlat(False)
        self.bSepic.setObjectName("bSepic")
        self.gridLayout.addWidget(self.bSepic, 1, 1, 1, 1)
        self.bPontoOp = QtWidgets.QPushButton(self.tab)
        self.bPontoOp.setGeometry(QtCore.QRect(250, 390, 291, 51))
        self.bPontoOp.setObjectName("bPontoOp")
        self.layoutWidget1 = QtWidgets.QWidget(self.tab)
        self.layoutWidget1.setGeometry(QtCore.QRect(460, 180, 321, 65))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_D = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_D.setFont(font)
        self.label_D.setObjectName("label_D")
        self.gridLayout_5.addWidget(self.label_D, 0, 0, 1, 1)
        self.input_duty = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.input_duty.setFont(font)
        self.input_duty.setInputMask("")
        self.input_duty.setText("")
        self.input_duty.setObjectName("input_duty")
        self.gridLayout_5.addWidget(self.input_duty, 0, 1, 1, 1)
        self.label_Vo = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_Vo.setFont(font)
        self.label_Vo.setObjectName("label_Vo")
        self.gridLayout_5.addWidget(self.label_Vo, 1, 0, 1, 1)
        self.input_Vo = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.input_Vo.setFont(font)
        self.input_Vo.setText("")
        self.input_Vo.setObjectName("input_Vo")
        self.gridLayout_5.addWidget(self.input_Vo, 1, 1, 1, 1)
        self.label_Vo_2 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_Vo_2.setFont(font)
        self.label_Vo_2.setObjectName("label_Vo_2")
        self.gridLayout_5.addWidget(self.label_Vo_2, 1, 2, 1, 1)
        self.preOutput = QtWidgets.QTextEdit(self.tab)
        self.preOutput.setGeometry(QtCore.QRect(20, 500, 811, 171))
        self.preOutput.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.preOutput.setReadOnly(True)
        self.preOutput.setObjectName("preOutput")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.bTdPadrao = QtWidgets.QCheckBox(self.tab_2)
        self.bTdPadrao.setGeometry(QtCore.QRect(30, 160, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bTdPadrao.setFont(font)
        self.bTdPadrao.setAutoExclusive(False)
        self.bTdPadrao.setObjectName("bTdPadrao")
        self.layoutWidget_4 = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget_4.setGeometry(QtCore.QRect(420, 170, 395, 35))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.CPropor = QtWidgets.QPushButton(self.layoutWidget_4)
        self.CPropor.setSizeIncrement(QtCore.QSize(0, 2))
        self.CPropor.setBaseSize(QtCore.QSize(0, 5))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.CPropor.setFont(font)
        self.CPropor.setCheckable(True)
        self.CPropor.setAutoExclusive(False)
        self.CPropor.setAutoDefault(False)
        self.CPropor.setFlat(False)
        self.CPropor.setObjectName("CPropor")
        self.horizontalLayout.addWidget(self.CPropor)
        self.CPi = QtWidgets.QPushButton(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.CPi.setFont(font)
        self.CPi.setCheckable(True)
        self.CPi.setAutoExclusive(False)
        self.CPi.setAutoDefault(False)
        self.CPi.setFlat(False)
        self.CPi.setObjectName("CPi")
        self.horizontalLayout.addWidget(self.CPi)
        self.CPd = QtWidgets.QPushButton(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.CPd.setFont(font)
        self.CPd.setCheckable(True)
        self.CPd.setAutoExclusive(False)
        self.CPd.setAutoDefault(False)
        self.CPd.setFlat(False)
        self.CPd.setObjectName("CPd")
        self.horizontalLayout.addWidget(self.CPd)
        self.CPid = QtWidgets.QPushButton(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.CPid.setFont(font)
        self.CPid.setCheckable(True)
        self.CPid.setAutoExclusive(False)
        self.CPid.setAutoDefault(False)
        self.CPid.setDefault(False)
        self.CPid.setFlat(False)
        self.CPid.setObjectName("CPid")
        self.horizontalLayout.addWidget(self.CPid)
        self.bTdCustom = QtWidgets.QCheckBox(self.tab_2)
        self.bTdCustom.setGeometry(QtCore.QRect(30, 330, 231, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bTdCustom.setFont(font)
        self.bTdCustom.setAutoExclusive(False)
        self.bTdCustom.setObjectName("bTdCustom")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(110, 130, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.customC = QtWidgets.QCheckBox(self.tab_2)
        self.customC.setGeometry(QtCore.QRect(420, 210, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.customC.setFont(font)
        self.customC.setAutoExclusive(False)
        self.customC.setObjectName("customC")
        self.layoutWidget_5 = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget_5.setGeometry(QtCore.QRect(60, 370, 261, 69))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.formLayout_2 = QtWidgets.QFormLayout(self.layoutWidget_5)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.labelTdNum = QtWidgets.QLabel(self.layoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelTdNum.setFont(font)
        self.labelTdNum.setObjectName("labelTdNum")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.labelTdNum)
        self.TdNum = QtWidgets.QLineEdit(self.layoutWidget_5)
        self.TdNum.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.TdNum.setFont(font)
        self.TdNum.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.IBeamCursor))
        self.TdNum.setInputMask("")
        self.TdNum.setText("")
        self.TdNum.setReadOnly(False)
        self.TdNum.setObjectName("TdNum")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.TdNum)
        self.labelTdDen = QtWidgets.QLabel(self.layoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelTdDen.setFont(font)
        self.labelTdDen.setObjectName("labelTdDen")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.labelTdDen)
        self.TdDen = QtWidgets.QLineEdit(self.layoutWidget_5)
        self.TdDen.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.TdDen.setFont(font)
        self.TdDen.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.IBeamCursor))
        self.TdDen.setInputMask("")
        self.TdDen.setText("")
        self.TdDen.setReadOnly(False)
        self.TdDen.setObjectName("TdDen")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.TdDen)
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(530, 130, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.line_3 = QtWidgets.QFrame(self.tab_2)
        self.line_3.setGeometry(QtCore.QRect(370, 130, 20, 331))
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.line = QtWidgets.QFrame(self.tab_2)
        self.line.setGeometry(QtCore.QRect(410, 290, 421, 20))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(580, 300, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.semFiltro = QtWidgets.QCheckBox(self.tab_2)
        self.semFiltro.setGeometry(QtCore.QRect(390, 330, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.semFiltro.setFont(font)
        self.semFiltro.setAutoExclusive(False)
        self.semFiltro.setObjectName("semFiltro")
        self.layoutWidget_6 = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget_6.setGeometry(QtCore.QRect(560, 370, 251, 69))
        self.layoutWidget_6.setObjectName("layoutWidget_6")
        self.formLayout_3 = QtWidgets.QFormLayout(self.layoutWidget_6)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.labelFiltroNum = QtWidgets.QLabel(self.layoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelFiltroNum.setFont(font)
        self.labelFiltroNum.setObjectName("labelFiltroNum")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.labelFiltroNum)
        self.fTdNum = QtWidgets.QLineEdit(self.layoutWidget_6)
        self.fTdNum.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fTdNum.setFont(font)
        self.fTdNum.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.IBeamCursor))
        self.fTdNum.setInputMask("")
        self.fTdNum.setText("")
        self.fTdNum.setReadOnly(False)
        self.fTdNum.setObjectName("fTdNum")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.fTdNum)
        self.labelFiltroDen = QtWidgets.QLabel(self.layoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelFiltroDen.setFont(font)
        self.labelFiltroDen.setObjectName("labelFiltroDen")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.labelFiltroDen)
        self.fTdDen = QtWidgets.QLineEdit(self.layoutWidget_6)
        self.fTdDen.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fTdDen.setFont(font)
        self.fTdDen.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.IBeamCursor))
        self.fTdDen.setInputMask("")
        self.fTdDen.setText("")
        self.fTdDen.setReadOnly(False)
        self.fTdDen.setObjectName("fTdDen")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.fTdDen)
        self.filtroPadrao = QtWidgets.QCheckBox(self.tab_2)
        self.filtroPadrao.setGeometry(QtCore.QRect(580, 330, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.filtroPadrao.setFont(font)
        self.filtroPadrao.setAutoExclusive(False)
        self.filtroPadrao.setObjectName("filtroPadrao")
        self.filtroCustom = QtWidgets.QCheckBox(self.tab_2)
        self.filtroCustom.setGeometry(QtCore.QRect(390, 390, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.filtroCustom.setFont(font)
        self.filtroCustom.setAutoExclusive(False)
        self.filtroCustom.setObjectName("filtroCustom")
        self.layoutWidget_7 = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget_7.setGeometry(QtCore.QRect(160, 40, 571, 65))
        self.layoutWidget_7.setObjectName("layoutWidget_7")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget_7)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_ensaio_2 = QtWidgets.QLabel(self.layoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_ensaio_2.setFont(font)
        self.label_ensaio_2.setObjectName("label_ensaio_2")
        self.gridLayout_2.addWidget(self.label_ensaio_2, 0, 0, 1, 1)
        self.bEnsaio = QtWidgets.QToolButton(self.layoutWidget_7)
        self.bEnsaio.setObjectName("bEnsaio")
        self.gridLayout_2.addWidget(self.bEnsaio, 0, 1, 1, 1)
        self.ensaioText = QtWidgets.QLineEdit(self.layoutWidget_7)
        self.ensaioText.setInputMask("")
        self.ensaioText.setText("")
        self.ensaioText.setReadOnly(True)
        self.ensaioText.setObjectName("ensaioText")
        self.gridLayout_2.addWidget(self.ensaioText, 0, 2, 1, 1)
        self.label_iv_2 = QtWidgets.QLabel(self.layoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_iv_2.setFont(font)
        self.label_iv_2.setObjectName("label_iv_2")
        self.gridLayout_2.addWidget(self.label_iv_2, 1, 0, 1, 1)
        self.bIV = QtWidgets.QToolButton(self.layoutWidget_7)
        self.bIV.setObjectName("bIV")
        self.gridLayout_2.addWidget(self.bIV, 1, 1, 1, 1)
        self.ivText = QtWidgets.QLineEdit(self.layoutWidget_7)
        self.ivText.setInputMask("")
        self.ivText.setText("")
        self.ivText.setReadOnly(True)
        self.ivText.setObjectName("ivText")
        self.gridLayout_2.addWidget(self.ivText, 1, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(190, 0, 531, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.line_2 = QtWidgets.QFrame(self.tab_2)
        self.line_2.setGeometry(QtCore.QRect(20, 110, 811, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_5 = QtWidgets.QFrame(self.tab_2)
        self.line_5.setGeometry(QtCore.QRect(20, 470, 811, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_5.setObjectName("line_5")
        self.bVRFT = QtWidgets.QPushButton(self.tab_2)
        self.bVRFT.setGeometry(QtCore.QRect(400, 430, 201, 41))
        self.bVRFT.setObjectName("bVRFT")
        self.controllerOutput = QtWidgets.QPlainTextEdit(self.tab_2)
        self.controllerOutput.setGeometry(QtCore.QRect(20, 500, 811, 171))
        self.controllerOutput.setReadOnly(True)
        self.controllerOutput.setPlainText("")
        self.controllerOutput.setObjectName("controllerOutput")
        self.layoutWidget2 = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget2.setGeometry(QtCore.QRect(550, 220, 261, 69))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget2)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_C = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_C.setFont(font)
        self.label_C.setObjectName("label_C")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_C)
        self.customCNum = QtWidgets.QLineEdit(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.customCNum.setFont(font)
        self.customCNum.setText("")
        self.customCNum.setObjectName("customCNum")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.customCNum)
        self.label_C_2 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_C_2.setFont(font)
        self.label_C_2.setObjectName("label_C_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_C_2)
        self.customCDen = QtWidgets.QLineEdit(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.customCDen.setFont(font)
        self.customCDen.setText("")
        self.customCDen.setObjectName("customCDen")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.customCDen)
        self.layoutWidget3 = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget3.setGeometry(QtCore.QRect(30, 210, 342, 100))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.layoutWidget3)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.labelTso = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelTso.setFont(font)
        self.labelTso.setObjectName("labelTso")
        self.gridLayout_4.addWidget(self.labelTso, 0, 0, 1, 1)
        self.textAcom = QtWidgets.QLineEdit(self.layoutWidget3)
        self.textAcom.setObjectName("textAcom")
        self.gridLayout_4.addWidget(self.textAcom, 0, 1, 1, 1)
        self.labelTso_2 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelTso_2.setFont(font)
        self.labelTso_2.setObjectName("labelTso_2")
        self.gridLayout_4.addWidget(self.labelTso_2, 0, 2, 1, 1)
        self.labelRapido = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelRapido.setFont(font)
        self.labelRapido.setObjectName("labelRapido")
        self.gridLayout_4.addWidget(self.labelRapido, 1, 0, 1, 1)
        self.textSpeed = QtWidgets.QLineEdit(self.layoutWidget3)
        self.textSpeed.setObjectName("textSpeed")
        self.gridLayout_4.addWidget(self.textSpeed, 1, 1, 1, 1)
        self.labelRapido_4 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelRapido_4.setFont(font)
        self.labelRapido_4.setObjectName("labelRapido_4")
        self.gridLayout_4.addWidget(self.labelRapido_4, 1, 2, 1, 1)
        self.labelRapido_2 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelRapido_2.setFont(font)
        self.labelRapido_2.setObjectName("labelRapido_2")
        self.gridLayout_4.addWidget(self.labelRapido_2, 2, 0, 1, 1)
        self.textFreq = QtWidgets.QLineEdit(self.layoutWidget3)
        self.textFreq.setObjectName("textFreq")
        self.gridLayout_4.addWidget(self.textFreq, 2, 1, 1, 1)
        self.labelRapido_3 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelRapido_3.setFont(font)
        self.labelRapido_3.setObjectName("labelRapido_3")
        self.gridLayout_4.addWidget(self.labelRapido_3, 2, 2, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_7 = QtWidgets.QLabel(self.tab_3)
        self.label_7.setGeometry(QtCore.QRect(330, 250, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.grafTd = QtWidgets.QPushButton(self.tab_3)
        self.grafTd.setGeometry(QtCore.QRect(40, 330, 221, 31))
        self.grafTd.setObjectName("grafTd")
        self.label_9 = QtWidgets.QLabel(self.tab_3)
        self.label_9.setGeometry(QtCore.QRect(260, 60, 421, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.line_7 = QtWidgets.QFrame(self.tab_3)
        self.line_7.setGeometry(QtCore.QRect(19, 189, 811, 20))
        self.line_7.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_7.setObjectName("line_7")
        self.bJVR = QtWidgets.QPushButton(self.tab_3)
        self.bJVR.setGeometry(QtCore.QRect(300, 330, 221, 31))
        self.bJVR.setObjectName("bJVR")
        self.bSensi = QtWidgets.QPushButton(self.tab_3)
        self.bSensi.setGeometry(QtCore.QRect(560, 330, 271, 31))
        self.bSensi.setObjectName("bSensi")
        self.line_8 = QtWidgets.QFrame(self.tab_3)
        self.line_8.setGeometry(QtCore.QRect(20, 440, 811, 20))
        self.line_8.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_8.setObjectName("line_8")
        self.layoutWidget4 = QtWidgets.QWidget(self.tab_3)
        self.layoutWidget4.setGeometry(QtCore.QRect(150, 130, 581, 30))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget4)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_ensaio_3 = QtWidgets.QLabel(self.layoutWidget4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_ensaio_3.setFont(font)
        self.label_ensaio_3.setObjectName("label_ensaio_3")
        self.gridLayout_3.addWidget(self.label_ensaio_3, 0, 0, 1, 1)
        self.bEnsaioMF = QtWidgets.QToolButton(self.layoutWidget4)
        self.bEnsaioMF.setObjectName("bEnsaioMF")
        self.gridLayout_3.addWidget(self.bEnsaioMF, 0, 1, 1, 1)
        self.ensaioMFText = QtWidgets.QLineEdit(self.layoutWidget4)
        self.ensaioMFText.setInputMask("")
        self.ensaioMFText.setText("")
        self.ensaioMFText.setReadOnly(True)
        self.ensaioMFText.setObjectName("ensaioMFText")
        self.gridLayout_3.addWidget(self.ensaioMFText, 0, 2, 1, 1)
        self.MFOutput = QtWidgets.QPlainTextEdit(self.tab_3)
        self.MFOutput.setGeometry(QtCore.QRect(20, 500, 811, 171))
        self.MFOutput.setReadOnly(True)
        self.MFOutput.setPlainText("")
        self.MFOutput.setObjectName("MFOutput")
        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 862, 26))
        self.menubar.setObjectName("menubar")
        self.menuArquivo = QtWidgets.QMenu(self.menubar)
        self.menuArquivo.setObjectName("menuArquivo")
        self.menuSobre = QtWidgets.QMenu(self.menubar)
        self.menuSobre.setObjectName("menuSobre")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuArquivo.menuAction())
        self.menubar.addAction(self.menuSobre.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EasyVRFT"))
        self.label_op.setText(_translate("MainWindow", "Ponto de Operação da Coleta de Dados:"))
        self.label_4.setText(_translate("MainWindow", "Classe do conversor:"))
        self.bBuck.setStatusTip(_translate("MainWindow", "Classe de conversor Buck"))
        self.bBuck.setText(_translate("MainWindow", "Buck"))
        self.bFlyback.setStatusTip(_translate("MainWindow", "Classe de conversor Flyback"))
        self.bFlyback.setText(_translate("MainWindow", "Flyback"))
        self.bBoost.setStatusTip(_translate("MainWindow", "Classe de conversor Boost"))
        self.bBoost.setText(_translate("MainWindow", "Boost"))
        self.bSepic.setStatusTip(_translate("MainWindow", "Classe de conversor SEPIC"))
        self.bSepic.setText(_translate("MainWindow", "SEPIC"))
        self.bPontoOp.setStatusTip(_translate("MainWindow", "Gerar ponto de operação ideal para coleta de dados"))
        self.bPontoOp.setText(_translate("MainWindow", "Gerar Ganho Proporcional Máximo"))
        self.label_D.setStatusTip(_translate("MainWindow", "Entrada do Duty Cicle"))
        self.label_D.setText(_translate("MainWindow", "Ciclo de Trabalho(D):"))
        self.input_duty.setStatusTip(_translate("MainWindow", "Entrada do Duty Cicle"))
        self.label_Vo.setStatusTip(_translate("MainWindow", "Tensão de saída"))
        self.label_Vo.setText(_translate("MainWindow", "Tensão de Saída(Vo):"))
        self.input_Vo.setStatusTip(_translate("MainWindow", "TensãEntrada da tensão de saída"))
        self.label_Vo_2.setStatusTip(_translate("MainWindow", "Tensão de saída"))
        self.label_Vo_2.setText(_translate("MainWindow", "[V]"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Pré-projeto"))
        self.bTdPadrao.setStatusTip(_translate("MainWindow", "Função de transferência desejada calculada"))
        self.bTdPadrao.setText(_translate("MainWindow", "Padrão de primeira ordem"))
        self.CPropor.setStatusTip(_translate("MainWindow", "Controlador Proporcional"))
        self.CPropor.setText(_translate("MainWindow", "P"))
        self.CPi.setStatusTip(_translate("MainWindow", "Controlador Proporcional Integral"))
        self.CPi.setText(_translate("MainWindow", "PI"))
        self.CPd.setStatusTip(_translate("MainWindow", "Controlador Proporcional Derivativo"))
        self.CPd.setText(_translate("MainWindow", "PD"))
        self.CPid.setStatusTip(_translate("MainWindow", "Controlador Proporcional Integral Derivativo"))
        self.CPid.setText(_translate("MainWindow", "PID"))
        self.bTdCustom.setStatusTip(_translate("MainWindow", "Função de transferência desejada definida pelo usuário"))
        self.bTdCustom.setText(_translate("MainWindow", "Definido pelo usuário"))
        self.label_5.setText(_translate("MainWindow", "Modelo de referência Td(z)"))
        self.customC.setStatusTip(_translate("MainWindow", "Controlador customizado pelo usuário"))
        self.customC.setText(_translate("MainWindow", "Outro"))
        self.labelTdNum.setStatusTip(_translate("MainWindow", "Numerador da função de transferência obtivo definido pelo usuário"))
        self.labelTdNum.setText(_translate("MainWindow", "Numerador:"))
        self.TdNum.setToolTip(_translate("MainWindow", "Formato de entrada dos dados:\n"
"[a]"))
        self.TdNum.setStatusTip(_translate("MainWindow", "Numerador da função de transferência obtivo definido pelo usuário"))
        self.labelTdDen.setStatusTip(_translate("MainWindow", "Denominador da função de transferência obtivo definido pelo usuário"))
        self.labelTdDen.setText(_translate("MainWindow", "Denominador:"))
        self.TdDen.setToolTip(_translate("MainWindow", "Formato de entrada dos dados:\n"
"[1, -b, -c]"))
        self.TdDen.setStatusTip(_translate("MainWindow", "Denominador da função de transferência obtivo definido pelo usuário"))
        self.label_2.setText(_translate("MainWindow", "Classe do controlador"))
        self.label_6.setText(_translate("MainWindow", "Filtro L(z)"))
        self.semFiltro.setStatusTip(_translate("MainWindow", "Não utilizar filtro"))
        self.semFiltro.setText(_translate("MainWindow", "Sem Filtro L=1"))
        self.labelFiltroNum.setStatusTip(_translate("MainWindow", "Numerador do filtro customizado pelo usuário"))
        self.labelFiltroNum.setText(_translate("MainWindow", "Numerador:"))
        self.fTdNum.setToolTip(_translate("MainWindow", "Formato de entrada dos dados:\n"
"[1, -a]"))
        self.fTdNum.setStatusTip(_translate("MainWindow", "Numerador do filtro customizado pelo usuário"))
        self.labelFiltroDen.setStatusTip(_translate("MainWindow", "Denominador do filtro customizado pelo usuário"))
        self.labelFiltroDen.setText(_translate("MainWindow", "Denominador:"))
        self.fTdDen.setToolTip(_translate("MainWindow", "Formato de entrada dos dados:\n"
"[1, -b, -c]"))
        self.fTdDen.setStatusTip(_translate("MainWindow", "Denominador do filtro customizado pelo usuário"))
        self.filtroPadrao.setStatusTip(_translate("MainWindow", "Utilizar o filtro padrão"))
        self.filtroPadrao.setText(_translate("MainWindow", "Filtro Padrão L=Td(1-Td)"))
        self.filtroCustom.setStatusTip(_translate("MainWindow", "Utilizar filtro customizado pelo usuário"))
        self.filtroCustom.setText(_translate("MainWindow", "Filtro customizado"))
        self.label_ensaio_2.setStatusTip(_translate("MainWindow", "Planilha com dados do ensaio da planta"))
        self.label_ensaio_2.setText(_translate("MainWindow", "Ensaio"))
        self.bEnsaio.setStatusTip(_translate("MainWindow", "Planilha com dados do ensaio da planta"))
        self.bEnsaio.setText(_translate("MainWindow", "..."))
        self.ensaioText.setStatusTip(_translate("MainWindow", "Planilha com dados do ensaio da planta"))
        self.label_iv_2.setStatusTip(_translate("MainWindow", "Planilha com dados do ensaio da planta da variável instrumentável"))
        self.label_iv_2.setText(_translate("MainWindow", "IV"))
        self.bIV.setStatusTip(_translate("MainWindow", "Planilha com dados do ensaio da planta da variável instrumentável"))
        self.bIV.setText(_translate("MainWindow", "..."))
        self.ivText.setStatusTip(_translate("MainWindow", "Planilha com dados do ensaio da planta da variável instrumentável"))
        self.label_8.setText(_translate("MainWindow", "Dados da planta (valor médio dos sinais removidos)"))
        self.bVRFT.setStatusTip(_translate("MainWindow", "Aplicar o método VRFT para os dados informados"))
        self.bVRFT.setText(_translate("MainWindow", "Projetar Controlador"))
        self.label_C.setStatusTip(_translate("MainWindow", "Controlador customizado pelo usuário"))
        self.label_C.setText(_translate("MainWindow", "Numerador:"))
        self.customCNum.setToolTip(_translate("MainWindow", "Formato de entrada dos dados:\n"
"[[1, -a], [1, -c]]"))
        self.customCNum.setStatusTip(_translate("MainWindow", "Numerador do controlador definido pelo usuário"))
        self.label_C_2.setStatusTip(_translate("MainWindow", "Controlador customizado pelo usuário"))
        self.label_C_2.setText(_translate("MainWindow", "Denominador:"))
        self.customCDen.setToolTip(_translate("MainWindow", "Formato de entrada dos dados:\n"
"[[1, -b], [1, -d]]"))
        self.customCDen.setStatusTip(_translate("MainWindow", "Denominador do controlador definido pelo usuário"))
        self.labelTso.setStatusTip(_translate("MainWindow", "Função de transferência obtivo padrão"))
        self.labelTso.setText(_translate("MainWindow", "Tempo de Acomodação"))
        self.textAcom.setStatusTip(_translate("MainWindow", "Tempo de acomodação em maçha aberta da planta"))
        self.labelTso_2.setStatusTip(_translate("MainWindow", "Função de transferência obtivo padrão"))
        self.labelTso_2.setText(_translate("MainWindow", "[ms]"))
        self.labelRapido.setStatusTip(_translate("MainWindow", "Função de transferência obtivo padrão"))
        self.labelRapido.setText(_translate("MainWindow", "x% mais rápido"))
        self.textSpeed.setToolTip(_translate("MainWindow", "Valores de [0, 100)"))
        self.textSpeed.setStatusTip(_translate("MainWindow", "Velocidade relativa desajada"))
        self.labelRapido_4.setStatusTip(_translate("MainWindow", "Função de transferência obtivo padrão"))
        self.labelRapido_4.setText(_translate("MainWindow", "[%]"))
        self.labelRapido_2.setStatusTip(_translate("MainWindow", "Função de transferência obtivo padrão"))
        self.labelRapido_2.setText(_translate("MainWindow", "Freq. de Amostragem"))
        self.textFreq.setStatusTip(_translate("MainWindow", "Frequência de amostragem do conjunto de dados"))
        self.labelRapido_3.setStatusTip(_translate("MainWindow", "Função de transferência obtivo padrão"))
        self.labelRapido_3.setText(_translate("MainWindow", "[Hz]"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Projeto do Controlador"))
        self.label_7.setText(_translate("MainWindow", "Análise dos Resultados"))
        self.grafTd.setStatusTip(_translate("MainWindow", "Gerar gráfico de Td(z) desejada e do sistema em malha fechada"))
        self.grafTd.setText(_translate("MainWindow", "Gerar Gráfico T(z)"))
        self.label_9.setText(_translate("MainWindow", "Dados de resposta em Malha Fechada"))
        self.bJVR.setStatusTip(_translate("MainWindow", "Avaliar a função de custo do método VRFT"))
        self.bJVR.setText(_translate("MainWindow", "Calcular custo J(VR)"))
        self.bSensi.setStatusTip(_translate("MainWindow", "Estimar sensibilidade do sistema"))
        self.bSensi.setText(_translate("MainWindow", "Estimar Função de Sensibilidade"))
        self.label_ensaio_3.setStatusTip(_translate("MainWindow", "Planilha com dados do ensaio da planta em malha fechada"))
        self.label_ensaio_3.setText(_translate("MainWindow", "Ensaio"))
        self.bEnsaioMF.setStatusTip(_translate("MainWindow", "Planilha com dados do ensaio da planta em malha fechada"))
        self.bEnsaioMF.setText(_translate("MainWindow", "..."))
        self.ensaioMFText.setStatusTip(_translate("MainWindow", "Planilha com dados do ensaio da planta em malha fechada"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Malha Fechada"))
        self.menuArquivo.setTitle(_translate("MainWindow", "Arquivo"))
        self.menuSobre.setTitle(_translate("MainWindow", "Sobre"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
